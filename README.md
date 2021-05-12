# CITS3403Project
Sidenote music learning webapp written for [CITS3403-Project](https://teaching.csse.uwa.edu.au/units/CITS3403/) semester 1, 2021.

## Features
Sidenote support online interactive learning of basic music theory where a users can complete formative assessments to reflect on their learning progress.

- A list of **learning modules** were avalible for ![Registed Users](https://img.shields.io/badge/-User-yellow.svg) to complete. 
- Summative assessments are provided to assess level of understanding through **marks** and possibly manual **feedback**. 

## Design 
### Code structure 
```
app/                                      <--Main App Module-->
      assessment/                         <--Package User Assessment-->
                __init__.py               ---initialize blueprint for assessment module---
                forms.py                  ---assessment form---
                routes.py                 ---assessment submission/feedback/view routes---
      auth/                               <--Package User Login-->
                __init__.py               ---initialize blueprint for login module--- 
                forms.py                  ---login form---
                routes.py                 ---authentication view route---
      index/                              <--Package Main functionality-->
                __init__.py               ---initialize blueprint for index module---
                routes.py                 ---User view routes---
      register/                           <--Package Register-->
                __init__.py               ---initialize blueprint for register module---
                forms.py                  ---register form---
                routes.py                 ---register view route---
      static/                             
                css/    
                          base.css        ---probvide base styling---
                js/
                          note.js         ---Note rendering functionality useing VexFlow---
                          assessment.js   ---Note rendering for assessment module useing VexFlow---
                          timer.js        ---Timed test functionality---
                          formattime.js   ---Reformat utc time---
      templates/                          <--Templates-->
                content/                   
                imports/
                profile/
                quiz/
                ....html
      __init__.py                         ---Blueprint registration and creating app onject---
      controller.py                       ---CURD and Ajax response---
      model.py                            ---user and submission model---
config.py                                 ---configuration---
sidenote.py                               ---Application---
test.py                                   ---Unittest---
    
```

### User types 
