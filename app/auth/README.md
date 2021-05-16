# Authentication module 
## ***__init__.py***
- Initializes module blueprint

## ***forms.py***
- WTform model for login 

## ***routes.py***
@route
### login
- Takes login request with authentication form
- Form validated on submit 
- Successful submission redirect to home page
- Invlalid username or password error raised on Unsuccessful submit
