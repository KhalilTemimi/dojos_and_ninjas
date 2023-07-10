from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja


@app.route('/create_ninja', methods=['post'])
def ninja():
    print(request.form)
    Ninja.new_ninja(request.form)
    return redirect('/')

@app.route('/show_dojo/<int:id>')
def get_by_id(id):
    dojo = Ninja.get_by_dojo({'dojo_id':id})
    return render_template('dojo_show.html', dojo=dojo)