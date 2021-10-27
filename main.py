# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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

@app.route('/games/sleepingsimulator/', methods=['GET', 'POST'])
def sleepingsimulator():
    return render_template("sleepingsimulator.html",)

@app.route('/games/rockpaper/')
def rockpaper():
    return render_template("rockpaper.html")

@app.route('/games/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/games/whackamole/')
def whackamole():
    return render_template("whackamole.html")

@app.route('/games/blackscreen/')
def blackscreen():
    return render_template("blackscreen.html")

@app.route('/games/terminal/', methods=['GET', 'POST'])
def terminal():
    # submit button has been pushed
    if request.form:
        commandInputPY = request.form.get("commandInput")
        if commandInputPY == "echo":  # input field has content
            return render_template("/terminal.html", commandOutput=commandInputPY)
        elif commandInputPY == "viewport":  # viewport
            return render_template("/terminal.html", commandOutput="G1 G2 G3 G4")
    return render_template("terminal.html", commandOutput="Unknown command.")


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


@app.route('/LogicG/')
def LogicGates():
    return render_template("minilab/LogicG.html")


@app.route('/colorcodes/', methods=['GET', 'POST'])
def colorcodes():
    return render_template("minilab/colorcodes.html",
                           BITS=8,
                           imgBulbOn="/static/assets/bulb_on.jpg",
                           imgBulbOff="/static/assets/bulb_off.png")


@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("/minilab/greet.html", name=name)
    return render_template("minilab/greet.html", name="World")


@app.route('/tpt8extracredit/', methods=['GET', 'POST'])
def tpt8extracredit():
    # submit button has been pushed
    if request.form:
        n = request.form.get("num")
        if len(str(n)) != 0:
            n = int(n)
            if n <= 100:
                l = []
                for i in range(n):
                    l.append(i)
                return render_template("/minilab/week8tptextracredit.html",
                                       l=l,
                                       n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l[::2]))))
            else:
                l = []
                for i in range(0, n, 2):
                    l.append(i)
                if n % 2 == 1:
                    return render_template("/minilab/week8tptextracredit.html",
                                       l='[0, 1, 2, 3, 4, 5, ..., ' + str(l[-3]) + ', ' + str(l[-2] - 1) + ', ' + str(l[-2]) + ', ' + str(l[-1] - 1) + ', ' + str(l[-1]) + ']',
                                       n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l))))
                if n % 2 == 0:
                    return render_template("/minilab/week8tptextracredit.html",
                                           l='[0, 1, 2, 3, 4, 5, ..., ' + str(l[-3] + 1) + ', ' + str(l[-2]) + ', ' + str(l[-2] + 1) + ', ' + str(l[-1]) + ', ' + str(l[-1] + 1) + ']',
                                           n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l))))
        else:
            return render_template("/minilab/week8tptextracredit.html",
                                   l=[],
                                   n=0)
    return render_template("/minilab/week8tptextracredit.html",
                           l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           n=2)


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        bits = request.form.get("BITS")
        bulb = request.form.get("BULB")
        if len(bits) != 0:  # input field has content
            if bulb == "BULB1":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on.jpg",
                                       imgBulbOff="/static/assets/bulb_off.png",
                                       BITS=int(bits))
            elif bulb == "BULB2":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on1.jpg",
                                       imgBulbOff="/static/assets/bulb_off1.jpg",
                                       BITS=int(bits))
            return render_template("minilab/binary.html",
                                   BITS=int(bits),
                                   imgBulbOn="/static/assets/bulb_on.jpg",
                                   imgBulbOff="/static/assets/bulb_off.png")
        if len(bits) == 0:
            if bulb == "BULB1":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on.jpg",
                                       imgBulbOff="/static/assets/bulb_off.png",
                                       BITS=8)
            elif bulb == "BULB2":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on1.jpg",
                                       imgBulbOff="/static/assets/bulb_off1.jpg",
                                       BITS=8)
            return render_template("minilab/binary.html",
                                   BITS=8,
                                   imgBulbOn="/static/assets/bulb_on.jpg",
                                   imgBulbOff="/static/assets/bulb_off.png")
    # starting and empty input default
    return render_template("minilab/binary.html",
                           BITS=8,
                           imgBulbOn="/static/assets/bulb_on.jpg",
                           imgBulbOff="/static/assets/bulb_off.png")


# connects /kangaroos path to render kangaroos.html
# @app.route('/kangaroos/')
# def kangaroos():
#     return render_template("kangaroos.html")
#
#
# @app.route('/walruses/')
# def walruses():
#     return render_template("walruses.html")
#
#
# @app.route('/hawkers/')
# def hawkers():
#     return render_template("hawkers.html")


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    web = True
    return render_template('minilab/rgb.html', images=image_data(path, None, web))


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
