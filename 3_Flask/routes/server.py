from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,helloworld!"

@app.route("/message")
def message():
    return "How are you my friend?"

@app.route("/message/<name>")
def display_name(name):
    print(name)
    return f"I'm fin Mr {name}"

@app.route("/id_user/<id>/<username>") #id was taked like string
def display_user(id, username):
    return f"ID: {id} ---------- USERNAME: {username}"

@app.route("/convert_int/<int:num>")  # num is converted to integer value
def convert_int(num):
    result = num + (num * 1.2)
    return f"RESULT is: {result}"



if __name__=="__main__":  
    app.run(debug=True)