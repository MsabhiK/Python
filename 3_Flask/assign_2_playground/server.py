from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/play')

@app.route("/play")
def level_1():
    return render_template("index.html", num=3, color="blue")

@app.route("/play/<int:count>")
def level_2(count):
    return render_template("index.html", num=count, color="blue")

@app.route("/play/<int:count>/<couleur>")
def level_3(count, couleur):
    return render_template("index.html", num=count, color=couleur)


if __name__ == '__main__':
    app.run(debug=True)