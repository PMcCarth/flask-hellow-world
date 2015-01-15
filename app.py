#---- Flask Hello World ----#
# import the Flask class from the Flask module #
from flask import Flask

# Create application object #
app = Flask(__name__)

# Use decorators to link the function to a url #
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string #
def hello_world():
    return "Hello, World!"

# start the development server using the run() method #
if __name__ == "__main__":
    app.run()
