from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    
    return render_template("ninja.html", dojos= dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas/edit/<int:id>')
def edit(id):
    data ={"id":id}
    ninja = Ninja.get_one(data)
    return render_template("edit_ninja_id.html", ninja=ninja)

@app.route("/ninja/update", methods=['POST'])
def update():
    data = request.form
    Ninja.update(data)
    return redirect('/dojos')

@app.route('/ninja/delete/<int:id>')
def delete(id):
    data ={"id":id}
    Ninja.destroy(data)
    return redirect('/dojos')
