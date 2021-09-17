# import "packages" from flask
from flask import Flask, render_template, request, Blueprint
from algorithm.image import image_data
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# connects default URL to render about.html
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/games/')
def games():
    return render_template("games.html")

@app.route('/aboutAidan/', methods=['GET', 'POST'])
def aboutAidan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutAidan.html", name=name)
    # starting and empty input default
    return render_template("aboutAidan.html", name="World")

@app.route('/aboutArch/', methods=['GET', 'POST'])
def aboutArch():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutArch.html", name=name)
    # starting and empty input default
    return render_template("aboutArch.html", name="World")

@app.route('/aboutDavid/', methods=['GET', 'POST'])
def aboutDavid():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutDavid.html", name=name)
    # starting and empty input default
    return render_template("aboutDavid.html", name="World")

@app.route('/aboutTyler/', methods=['GET', 'POST'])
def aboutTyler():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutTyler.html", name=name)
    # starting and empty input default
    return render_template("aboutTyler.html", name="World")

@app.route('/aboutWilliam/', methods=['GET', 'POST'])
def aboutWilliam():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutWilliam.html", name=name)
    # starting and empty input default
    return render_template("aboutWilliam.html", name="World")

@app.route('/video0/')
def video0():
    return render_template("minilab/video0.html")

@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("/minilab/greet.html", name=name)
    return render_template("minilab/greet.html", name="World")


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        bits = request.form.get("BITS")
        if len(bits) != 0:  # input field has content
            return render_template("minilab/binary.html", BITS=bits, MAX=((2 ** int(bits)) - 1))
    # starting and empty input default
    return render_template("minilab/binary.html", BITS=8, MAX=255)



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





@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    return render_template('rgb.html', images=image_data())



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
