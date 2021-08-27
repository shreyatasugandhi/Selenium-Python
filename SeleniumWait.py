from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import unittest, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumWait(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://newtours.demoaut.com/"

    def test_Login_test(self):
        driver = self.driver

        # open application
        driver.get(self.base_url)

        # Explicit wait
        try:
            element = WebDriverWait(driver, 10).until(
                EC.title_contains("Welcome: Mercury Tours")
            )
        except TimeoutException:
            self.fail("Loading timeout expired")


        # enter username and password
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tutorial")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tutorial")

        # Click on Sign in button and verify title
        driver.find_element_by_name("login").click()
        #self.assertEqual("Find a Flight: Mercury Tours:", driver.title)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
