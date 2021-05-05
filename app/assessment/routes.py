from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.assessment import bp
from app.assessment.forms import submissionForm, markingForm
from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_required
from app.controller import getSubmissionById, getAnswerForSub


@bp.route('/testSubmission/<difficulty>', methods=['GET','POST'])
@login_required 
def testSubmission(difficulty):
    if current_user.isAdmin:
        print("u fed up")
    form = submissionForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("validated")
        sub = submission()
        sub.difficulty = difficulty
        sub.creater_id = current_user.get_id()
        db.session.add(sub)
        db.session.commit()
        
        ans1 = answer()
        ans1.answerSeq=1
        ans1.submittedAnswer = form.Q1.data
        ans1.submissionId = sub.id

        ans2 = answer()
        ans2.answerSeq=2
        ans2.submittedAnswer = form.Q2.data
        ans2.submissionId = sub.id
        
        ans3 = answer()
        ans3.answerSeq=3
        ans3.submittedAnswer = form.Q3.data
        ans3.submissionId = sub.id

        ans4 = answer()
        ans4.answerSeq=4
        ans4.submittedAnswer = form.Q4.data
        ans4.submissionId = sub.id

        ans5 = answer()
        ans5.answerSeq=5
        ans5.submittedAnswer = form.Q5.data
        ans5.submissionId = sub.id

        db.session.add(ans1)
        db.session.add(ans2)
        db.session.add(ans3)
        db.session.add(ans4)
        db.session.add(ans5)
        db.session.commit()

        return redirect(url_for('index.index'))
    route_assessment = "quiz/{}.html".format(difficulty)
    return render_template(route_assessment, title='Assessment', form=form)


@bp.route('/markSubmission/<toBeMarked>', methods=['GET','POST'])
@login_required 
def markSubmission(toBeMarked):
    if not current_user.isAdmin:
        return redirect(url_for('index.index'))
    else:
        form = markingForm()
        this_sub = getSubmissionById(int(toBeMarked))
        user_responses = getAnswerForSub(int(toBeMarked))
        if form.validate_on_submit():
            for item in user_responses:
                if item.answerSeq == 1:
                    item.feedback = form.F1.data
                elif item.answerSeq == 2:
                    item.feedback = form.F2.data
                elif item.answerSeq == 3:
                    item.feedback = form.F3.data
                elif item.answerSeq == 4:
                    item.feedback = form.F4.data
                elif item.answerSeq == 5:
                    item.feedback = form.F5.data
            db.session.commit()
            return redirect(url_for('index.index'))
        user_responses = getAnswerForSub(int(toBeMarked))
        diff = this_sub.difficulty
        route_mark = "quiz/{}.html".format(diff)
        return render_template(route_mark, title='Marking', form=form, responses=user_responses)



@bp.route('/viewSubmission/<subId>', methods=['GET','POST'])
@login_required 
def viewSubmission(subId):
    if current_user.isAdmin:
        return redirect(url_for('index.index'))
    else:
        this_sub = getSubmissionById(int(subId))
        user_responses = getAnswerForSub(int(subId))
        diff = this_sub.difficulty
        route_mark = "quiz/{}.html".format(diff)
        return render_template(route_mark, title='ViewSubmission', form=False, responses=user_responses)

