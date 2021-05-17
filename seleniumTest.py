import unittest
import os, time
from app.model import users, submission, answer
from app import initapp, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
DRIVER = SECRET_KEY = os.environ.get('DRIVER') or './chromedriver.exe'
class testConfig():
    basedir=os.path.abspath(os.path.dirname(__file__))
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")

class SystemTest(unittest.TestCase):
    driver = None
    def setUp(self):
        self.driver = webdriver.Chrome(DRIVER)

        if not self.driver:
            self.skipTest("browser not ready")
        else:
            app = initapp(testConfig)
            self.app_context=app.app_context()
            self.app_context.push()
            db.init_app(app)
            db.create_all()

            peter=users()
            peter.username='fefe'
            peter.firstname='sdsfs'
            peter.lastname='shejg'
            peter.email='adsfea32f@student.uwa.edu.au'
            peter.set_password("adminnnn")
            peter.isAdmin=True
            
            shuang=users()
            shuang.username='name'
            shuang.firstname='shuang'
            shuang.lastname='zheng'
            shuang.email='2234990@gmail.com'
            shuang.set_password("goodmorning")
            shuang.noteHighScore = 3
            shuang.KeyHighScore = 2
            shuang.isAdmin=False

            db.session.add(peter)
            db.session.add(shuang)
            db.session.commit()

            self.driver.maximize_window()
            self.driver.get("http://localhost:5000")
    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.remove()
            db.drop_all()
    def test_register(self):
        valid_username = "juston"
        valid_password = "qwertyuiop123456#@!/"
        valid_cfmpassword = "qwertyuiop123456#@!/"
        valid_firstname = "juston"
        valid_lastname = "saton"
        valid_email = "juston_saton.real@valid-email.com"
        first_user = users.query.filter_by(username="fefe").first()
        self.assertIsInstance(first_user,users)
        empty_string = ""
        too_long_string = """qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        """
        invalid_username1 = "fefe"
        invalid_password = "abc"
        invalid_cfmpassword = "qertyuiop123456#@!/"
        invalid_email1 = "abcadsfasdf"
        invalid_email2 = "123abc@123.com"
        invalid_email3 = "123abc@aaa.c"
        self.driver.get("http://localhost:5000/register")
        self.driver.implicitly_wait(3)
        username = self.driver.find_element_by_id("regUsrName")
        password = self.driver.find_element_by_id("regPwd")
        cfmpassword = self.driver.find_element_by_id("regCfmPwd")
        firstname = self.driver.find_element_by_id("regFirst")
        lastname = self.driver.find_element_by_id("regLast")
        email = self.driver.find_element_by_id("regEmail")
        submit = self.driver.find_element_by_id("submit")
        
        username.send_keys(valid_username)
        password.send_keys(valid_password)
        cfmpassword.send_keys(valid_cfmpassword)
        firstname.send_keys(valid_firstname)
        lastname.send_keys(valid_lastname)
        email.send_keys(valid_email)
        submit.click()
        
        self.driver.implicitly_wait(4)
        time.sleep(2)
        ##
        header = self.driver.find_element_by_id("headtitle")
        self.assertEqual(header.get_attribute("innerHTML"),"Sign In")

        self.driver.get("http://localhost:5000/register")

        username = self.driver.find_element_by_id("regUsrName")
        password = self.driver.find_element_by_id("regPwd")
        cfmpassword = self.driver.find_element_by_id("regCfmPwd")
        firstname = self.driver.find_element_by_id("regFirst")
        lastname = self.driver.find_element_by_id("regLast")
        email = self.driver.find_element_by_id("regEmail")
        submit = self.driver.find_element_by_id("submit")

        username.send_keys(valid_username)
        password.send_keys(invalid_password)
        cfmpassword.send_keys(invalid_cfmpassword)
        firstname.send_keys(too_long_string)
        lastname.send_keys(empty_string)
        email.send_keys(invalid_email1)
        submit.click()
        
        self.driver.implicitly_wait(4)
        time.sleep(2)
        ##
        warnings = self.driver.find_elements(By.CLASS_NAME, "warning")
        self.assertEqual(warnings[0].get_attribute("innerHTML"),"[Password must be between 6 to 80 characters long.]")
        self.assertEqual(warnings[1].get_attribute("innerHTML"),"[Password must match.]")
        self.assertEqual(warnings[2].get_attribute("innerHTML"),"[Firstname cannot exceed 130 characters]")
        self.assertEqual(warnings[3].get_attribute("innerHTML"),"[This field is required]")
        self.assertEqual(warnings[4].get_attribute("innerHTML"),"[Invalid Email]")


        username.clear()
        username.send_keys(invalid_username1)
        password.clear()
        password.send_keys(valid_password)
        cfmpassword.clear()
        cfmpassword.send_keys(valid_cfmpassword)
        firstname.clear()
        firstname.send_keys(valid_firstname)
        lastname.clear()
        lastname.send_keys(valid_lastname)
        email.clear()
        email.send_keys(valid_email)
        submit.click()

        warnings = self.driver.find_elements(By.CLASS_NAME, "warning")
        self.assertEqual(warnings[0].get_attribute("innerHTML"),"[Please enter a different username.]")

    def test_login(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.implicitly_wait(4)
        test_user = users.query.filter_by(username="fefe").first()
        self.assertIsInstance(test_user,users)

        test_username = test_user.username
        test_password = "adminnnn"

        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_id("submit")

        username.send_keys(test_username)
        password.send_keys(test_password)
        submit.click()
        time.sleep(2)
        logout = self.driver.find_element_by_link_text("LOGOUT")
        self.assertIsNotNone(logout)

    def test_submission(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.implicitly_wait(1)
        test_user = users.query.filter_by(username="name").first()
        self.assertIsInstance(test_user,users)

        test_username = test_user.username
        test_password = "goodmorning"

        username = self.driver.find_element_by_id("loginname")
        password = self.driver.find_element_by_id("loginpwd")
        submit = self.driver.find_element_by_id("submit")

        username.send_keys(test_username)
        password.send_keys(test_password)
        submit.click()
        hoverElement = self.driver.find_element_by_id("assessment")
        action = ActionChains(self.driver)
        action.move_to_element(hoverElement).perform()
        intro = self.driver.find_element_by_link_text("INTRO")
        intro.click()
        self.driver.implicitly_wait(4)
        textbox = self.driver.find_elements(By.CLASS_NAME, "response")
        textbox[0].send_keys("G")
        textbox[1].send_keys("G")
        textbox[2].send_keys("G")
        textbox[3].send_keys("G")
        textbox[4].send_keys("G")
        submit_assess = self.driver.find_element_by_id("submit")
        submit_assess.click()
        header = self.driver.find_element_by_id("currentname")
        self.assertEqual(header.get_attribute("innerHTML"),test_username)
        time.sleep(2)




if __name__=='__main__':
    unittest.main(verbosity=2)

