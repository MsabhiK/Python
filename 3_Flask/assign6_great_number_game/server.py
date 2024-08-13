from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)

app.secret_key = "hjdhvlsdhjvlksjvfjvksfjvldvsf"
@app.route("/")
def index():
    if "num" not in session:  # num est le numero choisi arbitrairement
        session["num"] = random.randint(1, 100)
    if "counter" not in session:  # counter est le nombre de tentatives arbitrairement
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route("/game", methods=["POST"])
def game():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)