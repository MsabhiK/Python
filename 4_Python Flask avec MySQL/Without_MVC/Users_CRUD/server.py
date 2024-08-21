from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/users")

###1/ GET ALL#########################
@app.route('/users')
def all_users():
    # call the get all classmethod to get all users
    users=User.get_all()
    print(users)
    return render_template("users.html",  users=User.get_all())

#2/ CREATE NEW ####################
@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

#3/ UPDATE ############################
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={"id":id}
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)

@app.route("/user/update", methods=['POST'])
def update():
    data = request.form
    User.update(data)
    return redirect("/users")

#4/ DELETE ############################
@app.route('/user/delete/<int:id>')
def delete(id):
    data ={"id": id}
    User.delete(data)
    return redirect('/')

@app.route("/user/search", methods=['POST'])
def search_ID():
    data = { "id": request.form["id"] }
    
    return redirect('/user/show/<int:id>')



@app.route('/user/show/<int:id>')
def show(id):
    data ={"id":id}
    user = User.get_one(data)
    return render_template("show_user.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)