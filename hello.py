# hello.py (root dir of repo)

from flask import Flask

app = Flask(__name__)   #app variable now has flash application in it

# route: a URL path to visit
# route function names should be unique hello_world() vs about()

@app.route("/")         #app "decoration" ... defining certain routes through webapp
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"
