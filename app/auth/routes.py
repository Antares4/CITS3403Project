from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.auth import bp
from app.auth.forms import LoginForm
from app.model import users
from app import db
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        user = users.query.filter_by(username=form.username.data).first()
        username=form.username.data
        if user:
            return redirect(url_for('index.index', user=username))
        else:
            ## register
            user = users()
            user.name = form.username.data
            flash("name saved")
        
    elif(request.method == 'POST' and form.validate_on_submit() != True):
        flash('empty field')
    return render_template('login.html', title='Sign In', form=form)
