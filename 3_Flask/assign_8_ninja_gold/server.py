from flask import Flask, render_template, session, request, redirect
import random, datetime
app = Flask(__name__)

app.secret_key ="hjhfghjehjeherhjehvehjegjhvfhveuj"

@app.route("/")
def home():
   # message ="<ul><li>Bonjour</li></ul>"
    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
        session["count"] = 0
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process_money():
    session["count"] += 1
    current_time=datetime.datetime.now()
    choise = request.form["building"]
    match choise:
        case "farm":
            credit = random.randint(10, 20)
        case "cave":
            credit = random.randint(5, 10)
        case "house":
            credit = random.randint(2, 5)
        case "casino":
            credit = random.randint(-50, 50)

    #if request.form["building"] == "farm":
        #credit= random.randint(10, 20)
    #elif request.form["building"] == "cave":
        #credit= random.randint(5, 10)
    #elif request.form["building"] == "house":
        #credit= random.randint(2, 5)
    #elif request.form["building"] == "casino":
        #credit= random.randint(-50, 50)
    
    session["gold"] += credit
    if credit <0:
        session["activities"].insert(0,f"<p style='color: red;'> Earned: {credit} golds of the {request.form["building"]}! at ({current_time}) </p>")
    elif credit > 0:
        session["activities"].insert(0,f"<p style='color: green;'> Earned: {credit} golds of the {request.form["building"]}! at ({current_time}) </p>")
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)