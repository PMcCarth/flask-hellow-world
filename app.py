#---- Flask Hello World ----#
# import the Flask class from the Flask module #
from flask import Flask

# Create application object #
app = Flask(__name__)

# error handling #
app.config["DEBUG"] = True

# Use decorators to link the function to a url #
@app.route("/")
@app.route("/hello")
@app.route("/test/<search_query>")
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404
def search(search_query):
    return search_query

# define the view using a function, which returns a string #
def hello_world():
    return "Hello, World!"

# start the development server using the run() method #
if __name__ == "__main__":
    app.run()
