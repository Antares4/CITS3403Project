# Assessment module
## ***__init__.py***
- Initializes module blueprint 

## ***forms.py***
- WTform model for test submission 

## ***routes.py***
@route
### testSubmission 
- Take in request for new submission and assessment template 
- Not accessable to admin 
- Form validated and automarked on submit
- Successful submission reroutes to user profile page

@route
### markSubmission
- Takes request for feedback submission and compeleted assessment template
- Not accessable to user 
- Form validated and archived
- Successfule submission reroutes to admin profile page

@route
### viewSubmission
- Takes request for compeleted/marked assessment view template 
- Not accessable to admin 

