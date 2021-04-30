from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.register import bp
from app.register.forms import RegisterForm
from app.model import users
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = users()
        user.username = form.username.data
        user.email = form.email.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.joinedAt = datetime.utcnow()
        #############testing###################
        if form.username.data == "Shuang":
            user.isAdmin = True
        #########################################
        if(form.password.data == form.confirmpassword.data):
            hash_pwd = generate_password_hash(form.password.data, method="sha384")
            user.password = hash_pwd
        else:
            flash("password does not match, try again")
            return render_template("register.html", form = form)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    elif(request.method == 'POST' and not form.validate_on_submit()):
        flash('unable to register')
    return render_template('register.html', title='Register', form=form)

