from flask import Flask
app = Flask(__name__)
#
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}<b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_underline
# @make_emphasis
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye_world():
    return "<p>Bye!</p>"

@app.route("/username/<name>")
def say_hello(name):
    return f"<p>Hello {name}</p>"

if __name__ == "__main__":
    app.run(debug=True)