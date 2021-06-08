# PLZ_Exercise
## MagicList
In addition of a resular list functionality, MagicList can append to a list by setting values:

for example:

magic = MagicList()
magic[0] = 10
magic[1] = 20

In addition, you can also append a dataclass to MagicList if this attached to init.

for example:

@dataclass
class Person:
  age: int = 1

magic = MagicList(cls_type=Person)
magic[0].age = 10

Limitations:
You must keep the list's sequentiality in MagicList.
Trying to skip indexes will raise IndexError.

## Web Server
This web server is based on Sanic framework.

It has very basic functioniliy:
- main page('/'): Welcome text
- login page('/login') Login with user and password attached in JSON file
- logout page('/logout') Discard the authentication
- success page('/success') You will route to this page after successful login
- post page('/post') This page requires login


