# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import Common


class MoveToElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://newtours.demoaut.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_moveaction(self):

        driver = self.driver

        Common.Login(driver, "shreyata", "password123")
        Common.OpenBlog(driver)

    def test_Login(self):

        driver = self.driver

        Common.Login(driver, "shreyata", "password123")



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

