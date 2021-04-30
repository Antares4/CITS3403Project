from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from flask_login import current_user, login_required, logout_user
from app.index import bp
from app.controller import getAllSubmissions, getAllUsers, getUserById, howManySubmissions, howManyUsers
from app import db
from config import Config
from app.model import users

@bp.route('/')
@bp.route('/index/<name>')
def index(name=None):
    return render_template('index.html', use=name)

@bp.route('/demo')
def demo():
    return render_template('sample.html')

@bp.route('/notes/<chapter>/<page>')
@login_required 
def notes(chapter, page):
    route_cp = "content/{}/{}.html".format(chapter,page)
    return render_template(route_cp)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))

@bp.route('/profile/<userId>')
@login_required
def profile(userId):
    usr = getUserById(userId)
    if usr.isAdmin:
        page = request.args.get('page', 1, type=int)
        all_sub = getAllSubmissions().paginate(page, 2, False)
        ###########
        if all_sub.has_next:
            next_sub_page = url_for('index.profile', page=all_sub.next_num, userId=userId) 
        else:
            next_sub_page = None
        if all_sub.has_prev:
            prev_sub_page = url_for('index.profile', page=all_sub.prev_num, userId=userId) 
        else:
            prev_sub_page = None
        #######
        all_user = getAllUsers()
        info = {
            'subs'  : all_sub.items,
            'usrs'  : all_user,
            'subCount' : howManySubmissions(),
            'usrCount' : howManyUsers(),
            '_links': {
                'sub_prev' : prev_sub_page,
                'sub_next' : next_sub_page, 
            }
        }
        return render_template("profile/profile.html",data=info)
    else:
        my_sub = usr.getSubmissions(usr)
        print(my_sub)
        return render_template("profile/profile.html",subs=my_sub)

@bp.route('/a')
def a():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)
