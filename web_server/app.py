from pathlib import Path
import json

from sanic_auth import Auth, User
from sanic import Sanic, response


app = Sanic(__name__)
app.config.AUTH_LOGIN_ENDPOINT = 'login'

json_file = Path(__file__).parent / 'user_data.json'

with open(json_file) as json_file:
    user_data = json.load(json_file)


session = {}
@app.middleware('request')
async def add_session(request):
    request.ctx.session = session

auth = Auth(app)


LOGIN_FORM = '''
<h2>Please sign in</h2>
<p>{}</p>
<form action="" method="POST">
  <input class="username" id="name" name="username"
    placeholder="username" type="text" value=""><br>
  <input class="password" id="password" name="password"
    placeholder="password" type="password" value=""><br>
  <input id="submit" name="submit" type="submit" value="Sign In">
</form>
'''


@app.route('/login', methods=['GET', 'POST'])
async def login(request):
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user_data["username"] and password == user_data["password"]:
            user = User(id=1, name=username)
            auth.login_user(request, user)
            return response.redirect('/success')
        message = 'invalid username or password'
    return response.html(LOGIN_FORM.format(message))


@app.route('/success')
@auth.login_required(user_keyword='user')
async def success(request, user):
    return response.text("You logged in successfully - now you can post messages")


@app.route('/post')
@auth.login_required(user_keyword='user')
async def post(request, user):
    return response.text("POST")


@app.route('/')
async def test(request):
    content = 'Welcome! Please <a href="/login">Login</a>'
    return response.html(content)


@app.route('/logout')
async def test(request):
    auth.logout_user(request)
    return response.redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
