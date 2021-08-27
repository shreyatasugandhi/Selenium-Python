from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Assertions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://newtours.demoaut.com/"

    def test_Login_test(self):
        driver = self.driver

        # open application
        driver.get(self.base_url)
        self.assertEqual("Welcome: Mercury Tours", driver.title)

        # enter username and password
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("tutorial")



        ### Assert value
        self.assertEqual("tutorial", driver.find_element_by_name("userName").get_attribute("value"))

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tutorial")
        # Click on Sign in button and verify title
        driver.find_element_by_name("login").click()
        # Explicit wait
        try:
            element = WebDriverWait(driver, 20).until(
                EC.title_contains("Find a Flight: Mercury Tours:")
            )
        except TimeoutException:
            self.fail("Loading timeout expired")

        ### Assertions ####
        self.assertEqual("Find a Flight: Mercury Tours:", driver.title)
        self.assertTrue(driver.find_element_by_xpath("//input[@value='roundtrip']").is_selected())

        self.assertTrue(self.is_element_present(By.NAME, "findFlights"))


        #### Verify ####
        try:
            self.assertEqual("Round Trip   One Way", driver.find_element_by_xpath("//td[2]/b/font").text)
        except AssertionError as e:
            print ("Expected = Assertion Failed" "Where Actual = " +
                   e)



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True



    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
