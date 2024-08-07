from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO WORLD!"

@app.route("/dojo")
def display_dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say(name):
    return f"HI, {name.capitalize()}!" # .capitalize rend le 1er lettre en majuscule

@app.route("/repeat/<int:count>/<string:name>")
def repeat(count, name):
    result = ""
    for i in range (0, count):
        result += f"<p>{name.capitalize()}</p>"
    return result

if __name__ == '__main__':
    app.run(debug=True)
