from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.assessment import bp
from app.assessment.forms import submissionForm
from app.model import users, submission, answer
from app import db
from flask_login import current_user
from app.controller import getAllans


@bp.route('/testSubmission/<subjectName>', methods=['GET','POST'])
def testSubmission(subjectName):
    form = submissionForm()
    if form.validate_on_submit():
        print(int(form.Q1.data))
        sub = submission()
        sub.subject = subjectName
        sub.creater_id = current_user.get_id()
        db.session.add(sub)
        db.session.commit()

        ans1 = answer()
        ans1.answerSeq=1
        ans1.sumbittedAnswer = int(form.Q1.data)
        ans1.correctAnswer = int(form.Q1ans.data)
        submissionId = sub.id
        sa = sub.id
        return redirect(url_for('index.index', name=sa))
    return render_template('quiz/notation.html', title='Assessment', form=form)

