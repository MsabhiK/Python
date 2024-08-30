from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja
#from flask_app.models.ninja import Ninja
#from flask_app.models.dojo import Dojo



@app.route('/ninjas')
def ninjas():
    
    return render_template("ninja.html", dojos= dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

#@app.route('/ninjas/edit/<int:id>')
#def edit(id):
 #   data ={"id":id}
  #  ninja = Ninja.get_one(data)
   # return render_template("edit_ninja_id.html", ninja=ninja)

#@app.route("/ninja/update", methods=['POST'])
#def update():
   # data = request.form
   # ninja.Ninja.update(data)
    #return redirect("/dojos")

@app.route('/ninjas/edit/<ninja_id>')
def edit_page(ninja_id):
    print("in edit route for ninja id: ", ninja_id)
    ninja_obj = ninja.Ninja.get_one(ninja_id)
    return render_template("edit_ninja_id.html", ninja=ninja_obj)

@app.route('/ninjas/delete/<ninja_id><dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    print("Deleting ninja with id: ", ninja_id)
    data = {"ninja_id":ninja_id}
    ninja.Ninja.destroy(ninja_id)
    return redirect(f"/dojos/{dojo_id}")

@app.route('/ninjas/update', methods = ["POST"])
def update_ninja():
    print("in update we update ninja with data: ", request.form)
    data = request.form
    ninja.Ninja.update(data)
    return redirect(f'/dojos/{request.form["dojo_id"]}')



#@app.route('/ninja/delete/<int:id>')
#def delete(id):
 #   data ={"id":id}
  #  Ninja.destroy(data)
   # return redirect('/dojos')
