from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from flask_login import current_user, login_required, logout_user
from app.index import bp
from app.controller import getAllSubmissions, getSubmissionById, getAllUserResponse

@bp.route('/')
@bp.route('/index/<name>')
def index(name=None):
    return render_template('index.html', use=name)

@bp.route('/a')
def a():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@bp.route('/demo')
def demo():
    return render_template('sample.html')


@bp.route('/notes/<chapter>/<page>')
def notes(chapter, page):
    route_cp = "content/{}/{}.html".format(chapter,page)
    return render_template(route_cp)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))

@bp.route('/profile')
@login_required
def profile():
    if current_user.isAdmin:
        all_sub = getAllSubmissions()
        return render_template("profile/profile.html",subs=all_sub)
    else:
        my_sub = getAllUserResponse(current_user.id)
        return render_template("profile/profile.html",subs=my_sub)
