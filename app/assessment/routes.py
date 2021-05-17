from flask import Flask, request, url_for, redirect, render_template, flash, jsonify
from app.assessment import bp
from app.assessment.forms import submissionForm, markingForm
from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_required
from app.controller import getSubmissionById, getAnswerForSub, feedbackAssessment, createSubmission, autoMark

#route for creating submission 
@bp.route('/testSubmission/<difficulty>', methods=['GET','POST'])
@login_required 
def testSubmission(difficulty):
    #admin not accessable
    if current_user.isAdmin:
        return False
    form = submissionForm()
    #generate route with given difficulty
    route_assessment = "quiz/{}.html".format(difficulty)
    #form validates on submit
    if form.validate_on_submit():
        #create submission
        sub = createSubmission(current_user.id, difficulty, form)
        if sub:
            #automark
            autoMark(sub)
        else: 
            print("createSubmission failed")
            return render_template(route_assessment, title='Assessment', form=form)
        return redirect(url_for('index.profile', userId=current_user.id))
    #form does not validate on submit
    elif request.method == 'POST' and not form.validate_on_submit():
        flash("no empty fields")
        return render_template(route_assessment, title='Assessment', form=form)
    #defult
    return render_template(route_assessment, title='Assessment', form=form)

#route for admin to provide feedback to submission
@bp.route('/markSubmission/<toBeMarked>', methods=['GET','POST'])
@login_required 
def markSubmission(toBeMarked):
    #user not visible
    if not current_user.isAdmin:
        return redirect(url_for('index.index'))
    else:
        #get the submission to be marked
        this_sub = getSubmissionById(int(toBeMarked))
        diff = this_sub.difficulty
        #generate route
        route_mark = "quiz/{}.html".format(diff)
        #generate marking form
        form = markingForm()
        user_responses = getAnswerForSub(int(toBeMarked))
        if form.validate_on_submit():
            if feedbackAssessment(this_sub, form, user_responses):
                return redirect(url_for('index.profile', userId=current_user.id))
            else:
                print("submission failed")
                return render_template(route_mark, title='Marking', form=form, responses=user_responses)
        return render_template(route_mark, title='Marking', form=form, responses=user_responses)


#route for viewing submission
@bp.route('/viewSubmission/<subId>', methods=['GET','POST'])
@login_required 
def viewSubmission(subId):
    #not visible to admin
    if current_user.isAdmin:
        return redirect(url_for('index.index'))
    else:
        this_sub = getSubmissionById(int(subId))
        total_mark = this_sub.totalmark
        print(total_mark)
        user_responses = getAnswerForSub(int(subId))
        diff = this_sub.difficulty
        route_mark = "quiz/{}.html".format(diff)
        return render_template(route_mark, title='ViewSubmission', form=False, responses=user_responses, total=total_mark)

