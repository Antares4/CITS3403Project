import unittest
import os
from app.assessment.forms import submissionForm
from app.model import users, submission, answer
from app.controller import *
from  app import initapp, db
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

    def test_register(self):
        
        valid_usr = users()
        valid_usr.username = "dummy"
        valid_usr.firstname = "d"
        valid_usr.lastname = "y"
        valid_usr.email = "dummy@outlook.com"

        invalid_usr = users()
        invalid_usr.username = None
        invalid_usr.firstname ="invalid"
        invalid_usr.lastname ="last" 
        invalid_usr.email = None
        valid_password = "12345qwerty?><:"

        invalid_password = ""


        self.assertTrue(createUser(valid_usr, valid_password))
        self.assertFalse(createUser(valid_usr, invalid_password))
        self.assertFalse(createUser(invalid_usr, valid_password))
    
    def test_remove_user(self):
        user_id = 0
        submission1 = submission()
        submission1.creater_id = 1

        submission2 = submission()
        submission2.creater_id = 1

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
        removeUser(1)
        self.assertIsNone(users.query.filter_by(id=1).first())
        self.assertIsNone(submission.query.filter_by(creater_id=1).first())
        self.assertIsNone(answer.query.filter_by(submissionId=1).first())
    
    def test_ranking(self):
        guang=users()
        guang.username='guang'
        guang.firstname='guang'
        guang.lastname='gs'
        guang.email='asdfdf@gmail.com'
        guang.password = 'hashed2'
        guang.noteHighScore = 2
        guang.isAdmin=False
        db.session.add(guang)
        db.session.commit()
        print(users.query.all()[2].id)
        self.assertEqual(getNoteRanking(3), 2)

class submissionModelCase(unittest.TestCase):
    def setUp(self):
        self.app=initapp(testConfig)
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()

        submission1 = submission()
        submission1.creater_id = 1

        submission2 = submission()
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



if __name__=='__main__':
    unittest.main(verbosity=2)

