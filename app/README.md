# MCV architecture
## Model 
Contains two main entities `user` / `submission` of the application and a sub entities `answers`.
### `users`
- Each `users` instance represents a registered users. 
### `submissions`
- Each `submissions` instance represents one submission been made by a registered `user`
### `answer`
- Each `answer` instance represens one answer that belongs to a specific submission
---
## controller
Contains CURD operations and user/submission control function.
```
- createUser(user,password) // creates user: returns `true` on successful user creation, `false` on unsuccessful creation.  
- removeUser(userId) // deletes user and submission by this user: returns `true` on successful user deletion, `false` on unsuccessful deletion.   
- updateLoginTime(user) //updates user login time: returns `true` on successful user login time update, `false` on unsuccessful update.   
- feedbackAssessment(sub,form,responses) //inserts marker feedback into database: returns `true` on successful feedback submission, `false` on unsuccessful submission.  
- autoMark(submission) //auto marks a submission: returns `true` on successful automark, `false` on unsuccessful automark.   
- createSubmission(sid, difficulty, form) // inserts new a submission to database: returns created submission instance. 
- howManySubmissions() // returns (int) - total amount of submission in the database 
- howManyUsers() // returns (int) - total amount of users in the database
- getAllSubmissions() // returns (submission) - all submission object
- getAllUsers() // returns (users) - all user object 
- getUserById(userId) // returns (users) - user with the given id
- getSubmissionById(sub_id) // returns (submission) - submission with the given id
- getAnswerForSub(sub_id) // returns (answer) - list of answer belonging to the given submission id
- getNoteRanking(userid) // returns (int) - ranking of user with given id in the note timed quiz pool 
- getKeyRanking(userid) // returns (int) - ranking of user with given id in the key timed quiz pool
- getAdminProfile(page, userId) // returns (dict) - dictionary containing all submission, all users, user/submission count and page links
- getUserProfile(page, userId) // returns (dict) - dictionary containing all current user submission, note/key ranking of current user, list of top players of key/note pool and page links.
- processNoteScore(userId,score) // returns (dict) - dictionary containing new record, highest achieved score, current ranking and score for this attempt of the current player in the note pool
- processKeyScore(userId,score):// returns (dict) - dictionary containing new record, highest achieved score, current ranking and score for this attempt of the current player in the key pool
- getNoteList() // return (users) - top 7 players in the note timed test pool
- getKeyList() //  return (users) - top 7 players in the key timed test pool
```
---
## View 
-- View is not inplimented in this app as template rendering is handled by flask routing and jinja 
