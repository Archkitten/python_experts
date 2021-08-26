# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# testing testing 1 2 3

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

# aidan was here :D
# david was here too
# william was here