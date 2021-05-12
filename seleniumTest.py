import unittest
import os, time
from app.model import users, submission, answer
from app import initapp, db
from selenium import webdriver

class testConfig():
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "text.db")

class SystemTest(unittest.TestCase):
    driver = None
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')

        if not self.driver:
            self.skipTest("browser not ready")
        else:
            app = initapp(testConfig)
            self.app_context=app.app_context()
            self.app_context.push()
            db.init_app(app)
            db.create_all()
            self.driver.maximize_window()
            self.driver.get("http://localhost:5000")
    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.remove()
    def test_test(self):
        s = self.driver.find_element_by_id("login")
        s.click()
        

if __name__=='__main__':
    unittest.main(verbosity=2)

