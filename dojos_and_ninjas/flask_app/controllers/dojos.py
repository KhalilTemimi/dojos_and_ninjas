from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    dojos=Dojo.get_all()
    return render_template('dojo.html',dojos =dojos)

@app.route('/create_dojo', methods=['post'])
def new_dojo():
    print(request.form)
    Dojo.create(request.form)
    return redirect('/')

@app.route('/add_ninja')
def new_ninja():
    dojos=Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)