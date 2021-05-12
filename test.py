import unittest
import os
from app.model import users, submission, answer
from app.controller import *
from  app import initapp, db
from datetime import datetime

class testConfig():
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "text.db")

class userModelCase(unittest.TestCase):
    def setUp(self):
        self.app=initapp(testConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        peter=users()
        peter.username='p'
        peter.firstname='sdsfs'
        peter.lastname='shejg'
        peter.email='adsfea3232f@student.uwa.edu.au'
        peter.password = 'hashed'
        peter.noteHighScore = 10
        peter.isAdmin=True
        
        shuang=users()
        shuang.username='shuang'
        shuang.firstname='shuang'
        shuang.lastname='zheng'
        shuang.email='2234990@gmail.com'
        shuang.password = 'hashed'
        shuang.noteHighScore = 3
        shuang.isAdmin=False

        db.session.add(peter)
        db.session.add(shuang)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_Update_login_time(self):
        juston=users()
        juston.username='juston'
        juston.firstname='juston'
        juston.lastname='juston'
        juston.email='juston@gmail.com'
        juston.password = 'hashed7'
        juston.noteHighScore = 0
        juston.isAdmin=False
        db.session.add(juston)
        db.session.commit()
        self.assertTrue(updateLoginTime(juston))


    def test_register(self):

        invalid_Email = "wqwertyuiop"
        valid_password = "12345qwerty?><:"
        invalid_password = ""

        valid_usr = users()
        valid_usr.username = "dummy"
        valid_usr.firstname = "d"
        valid_usr.lastname = "y"
        valid_usr.email = "dummy@outlook.com"

        invalid_usr1 = users()
        invalid_usr1.username = None
        invalid_usr1.firstname ="invalid"
        invalid_usr1.lastname ="last" 
        invalid_usr1.email = None

        invalid_usr2 = users()
        invalid_usr2.username = "None"
        invalid_usr2.firstname = None
        invalid_usr2.lastname ="last" 
        invalid_usr2.email = invalid_Email


        self.assertTrue(createUser(valid_usr, valid_password))
        self.assertFalse(createUser(valid_usr, invalid_password))
        self.assertFalse(createUser(invalid_usr1, valid_password))
        self.assertFalse(createUser(invalid_usr2, valid_password))
    
    def test_remove_user(self):

        bob=users()
        bob.username='bob'
        bob.firstname='bob'
        bob.lastname='bob'
        bob.email='bob@gmail.com'
        bob.password = 'pas'
        bob.noteHighScore = 10
        bob.isAdmin=False

        db.session.add(bob)
        db.session.commit()

        usrid = users.query.filter_by(username="bob").first().id
        submission1 = submission()
        submission1.creater_id = usrid
        submission1.difficulty = "intro"
        db.session.add(submission1)
        db.session.commit()

        submission2 = submission()
        submission2.creater_id = usrid
        submission2.difficulty = "intro"
        db.session.add(submission2)
        db.session.commit()

        answer1 = answer()
        answer1.answerSeq=1
        answer1.submissionId=1

        answer2 = answer()
        answer2.answerSeq=2
        answer2.submissionId=1

        answer3 = answer()
        answer3.answerSeq=1
        answer3.submissionId=2


        db.session.add(answer1)
        db.session.add(answer2)
        db.session.add(answer3)
        db.session.commit()

        removeUser(3)

        self.assertIsNone(users.query.filter_by(id=3).first())
        self.assertIsNone(submission.query.filter_by(creater_id=3).first())
        self.assertIsNone(answer.query.filter_by(submissionId=1).first())
        self.assertIsNone(answer.query.filter_by(submissionId=2).first())

    def test_ranking(self):
        guang=users()
        guang.username='guang'
        guang.firstname='guang'
        guang.lastname='gs'
        guang.email='asdfdf@gmail.com'
        guang.password = 'hashed2'
        guang.noteHighScore = 30
        guang.isAdmin=False
        db.session.add(guang)
        db.session.commit()

        mark=users()
        mark.username='mark'
        mark.firstname='mark'
        mark.lastname='mark'
        mark.email='mark@gmail.com'
        mark.password = 'hashed3'
        mark.noteHighScore = 20
        mark.isAdmin=False
        db.session.add(mark)
        db.session.commit()

        usrid = users.query.filter_by(username="mark").first().id
        self.assertEqual(getNoteRanking(usrid), 2)

class submissionModelCase(unittest.TestCase):
    def setUp(self):
        self.app=initapp(testConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()

        submission1 = submission()
        submission1.difficulty = "intermediate"
        submission1.creater_id = 1

        submission2 = submission()
        submission2.difficulty = "difficult"
        submission2.creater_id = 2

        answer1 = answer()
        answer1.answerSeq=1
        answer1.submissionId=1

        answer2 = answer()
        answer2.answerSeq=2
        answer2.submissionId=1

        answer3 = answer()
        answer3.answerSeq=3
        answer3.submissionId=2

        db.session.add(submission1)
        db.session.add(submission2)
        db.session.add(answer1)
        db.session.add(answer2)
        db.session.add(answer3)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_get_submissions(self):

        answer4 = answer()
        answer4.answerSeq=3
        answer4.submissionId=1
        db.session.add(answer4)
        db.session.commit()
        self.assertTrue(getSubmissionById(2))
        self.assertEqual(getSubmissionById(1).creater_id, 1)
        self.assertEqual(getAnswerForSub(1)[2].answerSeq, answer4.answerSeq)
        self.assertEqual(getAnswerForSub(2)[0].answerSeq, 3)

    def test_automark(self):
        tobemarked = submission()
        tobemarked.id = 10
        tobemarked.difficulty = "intermediate"
        tobemarked.creater_id = 1
        db.session.add(tobemarked)
        db.session.commit()

        ans1 = answer()
        ans1.answerSeq=1
        ans1.submissionId=10
        ans1.submittedAnswer = "The answer is C sharp and note value is quaver"

        ans2 = answer()
        ans2.answerSeq=2
        ans2.submissionId=10
        ans2.submittedAnswer = "Compound Triple"

        ans3 = answer()
        ans3.answerSeq=3
        ans3.submissionId=10
        ans3.submittedAnswer = "10"

        ans4 = answer()
        ans4.answerSeq=4
        ans4.submissionId=10
        ans4.submittedAnswer = "b flat"

        ans5 = answer()
        ans5.answerSeq=5
        ans5.submissionId=10
        ans5.submittedAnswer = "C#, G, E"

        db.session.add(ans1)
        db.session.add(ans2)
        db.session.add(ans3)
        db.session.add(ans4)
        db.session.add(ans5)
        db.session.commit()
        
        sub = submission.query.filter_by(id=10).first()
        ans_lst = answer.query.filter_by(submissionId=10).all()

        autoMark(sub)
        for item in ans_lst:
            print("anslist",item.markreceived)
        self.assertEqual(sub.totalmark,2)
        self.assertTrue(ans_lst[0].markreceived)
        self.assertTrue(ans_lst[1].markreceived)
        self.assertFalse(ans_lst[2].markreceived)
        self.assertFalse(ans_lst[3].markreceived)
        self.assertFalse(ans_lst[4].markreceived)
if __name__=='__main__':
    unittest.main(verbosity=2)

