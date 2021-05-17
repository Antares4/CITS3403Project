from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from flask_login import current_user, login_required, logout_user
from app.index import bp
from app.controller import getUserById, getAdminProfile, getUserProfile, processNoteScore, processKeyScore, getKeyRanking,getNoteRanking
from app import db
from app.model import submission
from config import Config
from app.model import users
import json

#route to home page
@bp.route('/')
@bp.route('/index/<name>')
def index(name=None):
    return render_template('index.html', use=name)
    
#route to content pages
@bp.route('/notes/<chapter>/<page>')
@login_required 
def notes(chapter, page):
    route_cp = "content/{}/{}.html".format(chapter,page)
    return render_template(route_cp)

#logout route
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))

#profile route
@bp.route('/profile/<userId>')
@login_required
def profile(userId):
    usr = getUserById(userId)
    #admin
    if usr.isAdmin:
        page = request.args.get('page', 1, type=int)
        info = getAdminProfile(page, userId)
        return render_template("profile/adminprofile.html",data=info)
    #user
    else:
        page = request.args.get('page', 1, type=int)
        info = getUserProfile(page, userId)
        return render_template("profile/userprofile.html",data=info, key=dict(getKeyRanking=getKeyRanking, getNoteRanking=getNoteRanking))

#AJAX request from timed note quiz
@bp.route('/timedNote')
def timedNote():
    score = request.args.get('score', 0, type=int)
    userId = request.args.get('user', 0, type=int)
    result = processNoteScore(userId, score)
    jsonObj = json.dumps(result)
    return jsonObj

#AJAX request from timed key quiz
@bp.route('/timedKey')
def timedKey():
    score = request.args.get('score', 0, type=int)
    userId = request.args.get('user', 0, type=int)
    result = processKeyScore(userId, score)
    jsonObj = json.dumps(result)
    return jsonObj
