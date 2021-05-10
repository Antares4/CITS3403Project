from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from flask_login import current_user, login_required, logout_user
from app.index import bp
from app.controller import getAllSubmissions, getAllUsers, getUserById, howManySubmissions, howManyUsers, getNoteRanking, getKeyRanking
from app import db
from app.model import submission
from config import Config
from app.model import users
import json

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
        all_sub = getAllSubmissions().paginate(page, 5, False)
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
        page = request.args.get('page', 1, type=int)
        my_sub = submission.query.filter_by(creater_id=userId).order_by(submission.createdAt.desc()).paginate(page, 5, False)
        ###########
        if my_sub.has_next:
            next_sub_page = url_for('index.profile', page=my_sub.next_num, userId=userId) 
        else:
            next_sub_page = None
        if my_sub.has_prev:
            prev_sub_page = url_for('index.profile', page=my_sub.prev_num, userId=userId) 
        else:
            prev_sub_page = None
        info = {
            'subs'  : my_sub.items,
            'noteRank' : getNoteRanking(int(userId)),
            'keyRank' : getKeyRanking(int(userId)),
            '_links': {
                'sub_prev' : prev_sub_page,
                'sub_next' : next_sub_page, 
            }
        }
        return render_template("profile/profile.html",data=info)


@bp.route('/timedNote')
def timedNote():
    score = request.args.get('score', 0, type=int)
    userId = request.args.get('user', 0, type=int)
    this_user = getUserById(userId)
    if this_user.noteHighScore < score:
        this_user.noteHighScore = score
        db.session.commit()
        result = {
            'record': True,
            'HighScore': score,
            'ranking': getNoteRanking(userId),
            'score': score
        }
        print("result is",result)
    else:
        result = {
            'record': False,
            'HighScore': this_user.noteHighScore,
            'ranking': getNoteRanking(userId),
            'score': score
        }
        print("result is",result)
    db.session.commit()
    jsonObj = json.dumps(result)
    return jsonObj


@bp.route('/timedKey')
def timedKey():
    score = request.args.get('score', 0, type=int)
    userId = request.args.get('user', 0, type=int)
    this_user = getUserById(userId)
    if this_user.KeyHighScore < score:
        this_user.KeyHighScore = score
        db.session.commit()
        result = {
            'record': True,
            'HighScore': score,
            'ranking': getKeyRanking(userId),
            'score': score
        }
        print("result is",result)
    else:
        result = {
            'record': False,
            'HighScore': this_user.KeyHighScore,
            'ranking': getKeyRanking(userId),
            'score': score
        }
        print("result is",result)
    db.session.commit()
    jsonObj = json.dumps(result)
    return jsonObj
