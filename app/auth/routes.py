from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.auth import bp
from app.auth.forms import LoginForm
from app.model import users
from app.controller import updateLoginTime
from app import db
from flask_login import current_user, login_user




@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user,remember=form.remember_me.data)
                updateLoginTime(user)
                return redirect(url_for('index.index', name=user.username))
            else:
                flash("Invalid Password")
                return render_template('login.html', title='Sign In', form=form)
        else:
            flash("Invalid Username")
            return render_template('login.html', title='Sign In', form=form)
    elif(request.method == 'POST' and form.validate_on_submit() != True):
        flash('Empty Field')
    return render_template('login.html', title='Sign In', form=form)

