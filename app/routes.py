from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'peter'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    user = {'username': 'peter'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # if request.method == 'POST':
    #     # do stuff when the form is submitted
    #     # redirect to end the POST handling
    #     # the redirect can be to the same route or somewhere else
    #     return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('welcome.html', title='Home', user=user, posts=posts)

@app.route('/form', methods =["GET","POST"])
def form():
    if request.method == "GET":
        flash("submit success")
        return render_template('form.html')
    else:
        flash("submit form")
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    elif(request.method == 'POST' and form.validate_on_submit() != True):
        flash('empty field')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/a')
def a():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/quiz')
def quiz():
    return  render_template('quiz.html')

@app.route('/c1page1')
def c1page1():
    return render_template('content/chapter1/c1page1.html')
@app.route('/c1page2')
def c1page2():
    return render_template('content/chapter1/c1page2.html')
@app.route('/c1page3')
def c1page3():
    return render_template('content/chapter1/c1page3.html')


@app.route('/notes')
def notes():
    return render_template("content.html")

