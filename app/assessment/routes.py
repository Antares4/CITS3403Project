from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.assessment import bp
from app.assessment.forms import submissionForm
from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_required
from app.controller import getSubmissionById


@bp.route('/testSubmission/<difficulty>', methods=['GET','POST'])
@login_required 
def testSubmission(difficulty):
    if current_user.isAdmin:
        print("u fed up")
    form = submissionForm()
    if form.validate_on_submit():
        sub = submission()
        sub.difficulty = difficulty
        sub.creater_id = current_user.get_id()
        db.session.add(sub)
        db.session.commit()
        #
        ans1 = answer()
        ans1.answerSeq=1
        ans1.sumbittedAnswer = form.Q1.data
        ans1.submissionId = sub.id


        ans2 = answer()
        ans2.answerSeq=2
        ans2.sumbittedAnswer = form.Q2.data
        ans2.submissionId = sub.id

        db.session.add(ans1)
        db.session.add(ans2)
        db.session.commit()

        return redirect(url_for('index.index'))
    return render_template('quiz/intermediate.html', title='Assessment', form=form)


@bp.route('/testSubmission/<toBeMarked>', methods=['GET','POST'])
@login_required 
def markSubmission(toBeMarked):
    if not current_user.isAdmin:
        return redirect(url_for('index.index'))
    else:
        form = markingForm()
        if form.validate_on_submit():
            return redirect(url_for('index.index'))
        else:
            this_sub = getSubmissionById(toBeMarked)
            user_responses = getAllUserResponse(this_sub)
            diff = this_sub.difficulty
            route_mark = "quiz/{}.html".format(diff)
            return render_template(route_mark, title='Marking', form=form, responses=user_responses)

