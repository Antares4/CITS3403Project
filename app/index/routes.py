from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.index import bp
from app.forms import LoginForm

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/form', methods =["GET","POST"])
def form():
    if request.method == "GET":
        flash("submit success")
        return render_template('form.html')
    else:
        flash("submit form")
        return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    elif(request.method == 'POST' and form.validate_on_submit() != True):
        flash('empty field')
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/a')
def a():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@bp.route('/quiz')
def quiz():
    return  render_template('quiz.html')

@bp.route('/c1page1')
def c1page1():
    return render_template('content/chapter1/c1page1.html')
@bp.route('/c1page2')
def c1page2():
    return render_template('content/chapter1/c1page2.html')
@bp.route('/c1page3')
def c1page3():
    return render_template('content/chapter1/c1page3.html')

@bp.route('/c1page4')
def c1page4():
    return render_template('content/chapter1/c1page4.html')


@bp.route('/demo')
def demo():
    return render_template('sample.html')


@bp.route('/notes')
def notes():
    return render_template("content.html")

