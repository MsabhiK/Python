from flask import Flask, render_template
app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route("/")
def index():
    return render_template('index.html', row=8, col=8)

# Have another route accept a single parameter (i.e. "/<x>") 
# and render a checkerboard with x many rows, with alternating colors
@app.route("/<int:y>")
def index_col(y):
    return render_template('index.html', row=8, col=y)

#NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") 
# and render a checkerboard with x rows and y columns, with alternating colors
@app.route("/<int:x>/<int:y>")
def index_row_col(x, y):
    return render_template('index.html', row=x, col=y)

#SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") 
# and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def index_color(x, y, color1, color2):
    return render_template('index.html', row=x, col=y, couleur1=color1, couleur2=color2)


if __name__ == '__main__':
    app.run(debug=True)