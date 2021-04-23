from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.index import bp

@bp.route('/')
@bp.route('/index/<user>')
def index(user=None):
    return render_template('index.html', use=user)

@bp.route('/a')
def a():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@bp.route('/quiz')
def quiz():
    return  render_template('quiz.html')

# @bp.route('/c1page1')
# def c1page1():
#     return render_template('content/chapter1/c1page1.html')
# @bp.route('/c1page2')
# def c1page2():
#     return render_template('content/chapter1/c1page2.html')
# @bp.route('/c1page3')
# def c1page3():
#     return render_template('content/chapter1/c1page3.html')

# @bp.route('/c1page4')
# def c1page4():
#     return render_template('content/chapter1/c1page4.html')


@bp.route('/demo')
def demo():
    return render_template('sample.html')


@bp.route('/notes/<chapter>/<page>')
def notes(chapter, page):
    route_cp = "content/{}/{}.html".format(chapter,page)
    return render_template(route_cp)

