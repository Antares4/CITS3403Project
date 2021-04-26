from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.auth import bp
from app.auth.forms import LoginForm
from app.model import users
from app import db
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                return redirect(url_for('index.index', name=user.username))
            else:
                flash("invalid Password")
                return render_template('login.html', title='Sign In', form=form)
        else:
            flash("invalid username")
            return render_template('login.html', title='Sign In', form=form)
    elif(request.method == 'POST' and form.validate_on_submit() != True):
        flash('empty field')
    return render_template('login.html', title='Sign In', form=form)
