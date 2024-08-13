from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key ="fghjbckjnbc;sdb,sdbksnbc bd b"

@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route("/count")
def increment():
    #session["counter"] += 1
    return redirect("/")

@app.route("/count2")
def increment2():
    session["counter"] += 1
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
    


if __name__=="__main__":  
    app.run(debug=True)