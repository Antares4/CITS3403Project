from datetime import date
import unittest
import os
from app.model import users, submission, answer
from app.assessment.forms import markingForm, submissionForm
from app.controller import *
from app import initapp, db




class testConfig():
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "text.db")

class userControlCase(unittest.TestCase):
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
        peter.set_password("admin")
        peter.isAdmin=True
        
        shuang=users()
        shuang.username='shuang'
        shuang.firstname='shuang'
        shuang.lastname='zheng'
        shuang.email='2234990@gmail.com'
        shuang.set_password("asdfasdfefefe")
        shuang.noteHighScore = 3
        shuang.KeyHighScore = 2
        shuang.isAdmin=False

        db.session.add(peter)
        db.session.add(shuang)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_ranking(self):
        guang=users()
        guang.username='guang'
        guang.firstname='guang'
        guang.lastname='gs'
        guang.email='asdfdf@gmail.com'
        guang.set_password("asdfasdf")
        guang.noteHighScore = 30
        guang.KeyHighScore = 100
        guang.isAdmin=False
        db.session.add(guang)

        mark=users()
        mark.username='mark'
        mark.firstname='mark'
        mark.lastname='mark'
        mark.email='mark@gmail.com'
        mark.set_password("ahfueabh")
        mark.noteHighScore = 20
        mark.KeyHighScore = 200
        mark.isAdmin=False
        db.session.add(mark)

        esther=users()
        esther.username='esther'
        esther.firstname='esther'
        esther.lastname='esther'
        esther.email='esther@gmail.com'
        esther.set_password("ahfdfeeueabh")
        esther.noteHighScore = 11
        esther.KeyHighScore = 23
        esther.isAdmin=False
        db.session.add(esther)
        db.session.flush()

        usrid = users.query.filter_by(username="mark").first().id

        self.assertEqual(getNoteRanking(usrid), 2)
        self.assertEqual(getKeyRanking(usrid), 1)
        self.assertFalse(getNoteRanking(100))
        self.assertFalse(getKeyRanking(100))
        self.assertTrue(getNoteList()[0].noteHighScore >= getNoteList()[1].noteHighScore)
        self.assertTrue(getKeyList()[0].noteHighScore >= getNoteList()[1].noteHighScore)

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
        peter.set_password("hashed")
        peter.noteHighScore = 10
        peter.isAdmin=True
        
        shuang=users()
        shuang.username='shuang'
        shuang.firstname='shuang'
        shuang.lastname='zheng'
        shuang.email='2234990@gmail.com'
        shuang.set_password("asdfefefe")
        shuang.noteHighScore = 3
        shuang.isAdmin=False

        db.session.add(peter)
        db.session.add(shuang)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_update_login_time(self):
        juston=users()
        juston.username='juston'
        juston.firstname='juston'
        juston.lastname='juston'
        juston.email='juston@gmail.com'
        juston.set_password("hhhhhhh")
        juston.noteHighScore = 0
        juston.isAdmin=False
        db.session.add(juston)
        db.session.flush()
        self.assertTrue(updateLoginTime(juston))

    def test_user_check_password(self):
        password_user = users()
        password_user.set_password("banana")
        self.assertTrue(password_user.check_password("banana"))
        self.assertFalse(password_user.check_password("apple"))

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
        bob.set_password("rese")
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

        self.assertTrue(removeUser(3))
        self.assertIsNone(users.query.filter_by(id=3).first())
        self.assertIsNone(submission.query.filter_by(creater_id=3).first())
        self.assertIsNone(answer.query.filter_by(submissionId=1).first())
        self.assertIsNone(answer.query.filter_by(submissionId=2).first())


class submissionModelCase(unittest.TestCase):
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
        peter.set_password("hd")
        peter.noteHighScore = 10
        peter.isAdmin=True

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
        answer3.submissionId=1

        answer4 = answer()
        answer4.answerSeq=4
        answer4.submissionId=1

        answer5 = answer()
        answer5.answerSeq=5
        answer5.submissionId=1

        answer6 = answer()
        answer6.answerSeq=1
        answer6.submissionId=2

        db.session.add(submission1)
        db.session.add(submission2)
        db.session.add(answer1)
        db.session.add(answer2)
        db.session.add(answer3)
        db.session.add(answer4)
        db.session.add(answer5)
        db.session.add(answer6)
        db.session.add(peter)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_create_submission(self):
        valid_creater = 1
        invalid_creater = 100
        valid_difficulty = "intro"
        invalid_difficulty = "easy"

        with self.app.test_request_context():
            valid_form = submissionForm()
        valid_form.Q1.data = "i have no idea what i am doing"
        valid_form.Q2.data = "shoud've written this earlier"
        valid_form.Q3.data = "more bug in unittest"
        valid_form.Q4.data = "this should pass"
        valid_form.Q5.data = "f"

        with self.app.test_request_context():
            invalid_form = submissionForm()
        invalid_form.Q1.data = None
        invalid_form.Q2.data = 123
        invalid_form.Q3.data = True
        invalid_form.Q4.data = users()
        invalid_form.Q5.data = "users() for respect"

        self.assertIsInstance(createSubmission(valid_creater,valid_difficulty,valid_form),submission)
        self.assertRaises(ValueError, createSubmission,invalid_creater,valid_difficulty,valid_form)
        self.assertRaises(ValueError, createSubmission,valid_creater,invalid_difficulty,valid_form)
        self.assertRaises(TypeError, createSubmission,valid_creater,valid_difficulty,invalid_form)
    
    def test_give_feedback(self):
        sample_sub = submission.query.filter_by(id=1).first()

        res = answer.query.filter_by(submissionId=1).all()
        invalid_res = [1,2,3,4,5]
        with self.app.test_request_context():
            valid_form = markingForm()
        valid_form.F1.data = "comprehensive unit test "
        valid_form.F2.data = "10 out of 10 for testing"
        valid_form.F3.data = "CSS is the best language"
        valid_form.F4.data = "ababababababa"
        valid_form.F5.data = "Errrrrrrrrrrrrrrrrrr"

        with self.app.test_request_context():
            invalid_form = markingForm()
        invalid_form.F1.data = 1234
        invalid_form.F2.data = markingForm()
        invalid_form.F3.data = True
        invalid_form.F4.data = self
        invalid_form.F5.data = ".............."

        self.assertTrue(feedbackAssessment(sample_sub,valid_form,res))
        self.assertFalse(feedbackAssessment(None,valid_form,res))
        self.assertRaises(TypeError, feedbackAssessment,sample_sub,valid_form,invalid_res)
        self.assertRaises(TypeError,feedbackAssessment,sample_sub,invalid_form, res)

    def test_get_submissions(self):
        answer8 = answer()
        answer8.answerSeq=2
        answer8.submissionId=2
        db.session.add(answer8)
        db.session.commit()
        self.assertTrue(getSubmissionById(2))
        self.assertEqual(getSubmissionById(1).creater_id, 1)
        self.assertEqual(getAnswerForSub(2)[1].answerSeq, answer8.answerSeq)
        self.assertEqual(getAnswerForSub(1)[2].answerSeq, 3)

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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(userControlCase('test_ranking'))
    suite.addTest(userModelCase('test_update_login_time'))
    suite.addTest(userModelCase('test_user_check_password'))
    suite.addTest(userModelCase('test_register'))
    suite.addTest(userModelCase('test_remove_user'))
    suite.addTest(submissionModelCase('test_create_submission'))
    suite.addTest(submissionModelCase('test_give_feedback'))
    suite.addTest(submissionModelCase('test_get_submissions'))
    suite.addTest(submissionModelCase('test_automark'))
    return suite

if __name__=='__main__':
    unittest.main(verbosity=2)

