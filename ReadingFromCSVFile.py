import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import Common

class Browse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://careergrab.ionface.com/"

        filename = 'test.csv'
        row_number = 1
        with open(filename, 'rb') as f:
            testdata = csv.reader(f)
            testdata = list(testdata)
            self.username = testdata[row_number][0]
            self.password = testdata[row_number][1]

    def test_browse(self):
        driver = self.driver

        # open application
        driver.get(self.base_url)

        # validate title
        time.sleep(1)
        self.assertEqual("Welcome: Mercury Tours", driver.title)

        # enter username and password

        for row_number in range(len(self.username) and len(self.password)):
            driver.find_element_by_name("userName").clear()
            driver.find_element_by_name("userName").sen0d_keys(self.username)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(self.password)
            driver.find_element_by_id("id_password").clear()
            driver.set_page_load_timeout

        driver.find_element_by_name("login").click()
        time.sleep(4)
        self.assertEqual("Find a Flight: Mercury Tours:", driver.title)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)