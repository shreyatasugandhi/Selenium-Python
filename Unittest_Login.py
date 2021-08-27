from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import Common


class Unittest_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://newtours.demoaut.com/"

    def test_Login_test(self):
        driver = self.driver

        # open application
        driver.get(self.base_url)

        # validate title
        time.sleep(1)
        self.assertEqual("Welcome: Mercury Tours", driver.title)

        # enter username and password
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tutorial")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tutorial")

        # Click on Sign in button and verify title
        driver.find_element_by_name("login").click()
        time.sleep(4)
        self.assertEqual("Find a Flight: Mercury Tours:", driver.title)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
