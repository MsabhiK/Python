from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

app.secret_key ="hvlkdfhjvlkdfjldfj,b:,j:gfnhgjh"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods = ["POST"])
def survey():
    session["fullname"]= request.form["fullname"]
    session["sex"]= request.form["sex"]
    session["location"]= request.form["location"]
    session["language"]= request.form["language"]
    session["comments"]= request.form["comments"]
    return redirect("/displays")

@app.route("/displays")
def displays():
    if ("fullname" in session) and ("sex" in session) and ("location" in session) and ("language" in session) and ("comments" in session):
        fullname=session["fullname"]
        sex=session["sex"]
        location=session["location"]
        language=session["language"]
        comments=session["comments"]
    return render_template("displays.html", fullname=fullname, sex=sex, location=location, language=language, comments=comments)


if __name__ == '__main__':
    app.run(debug=True)