from flask_bcrypt import Bcrypt
from flask_app import app
from flask import session , request , render_template , redirect
from flask_app.models.user import User

app.secret_key ="hghjvnkvfddvbhkopmlkjhg"
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register' , methods=['POST'])
def register():
    data = request.form
    if not User.validate_register(data):
        return redirect('/')
    data = {
        "fullname": request.form["fullname"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])  # Hashed password using bcrypt.generate_password_hash() method
        # "password": bcrypt.check_password_hash(request.form["password"], hashed_password)  # For checking password hash
        # "password": request.form["password"]  # For storing password as plain text
    }
    id = User.register(data)
    session["user_id"] = id
    session["user_fullname"] = request.form["fullname"]
    return redirect('/dashboard')
    

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("dashboard.html", user=user)


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    if not User.validate_login(data):
        return redirect('/')
    user = User.get_by_email(data)
    if not user:
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        return redirect('/')
    session['user_id'] = user.id
    session['user_fullname'] = user.fullname
    # Redirect to the protected route
    return redirect('/dashboard')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")