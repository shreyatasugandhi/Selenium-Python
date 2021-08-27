from selenium import webdriver
import unittest, time


class Unittest_testFile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://newtours.demoaut.com/"

    def Test123(self):
        driver = self.driver

        # Oepn URL
        driver.get(self.base_url)

        # enter username
        driver.find_element_by_name("userName").send_keys("tutorial")

        # enter password
        driver.find_element_by_name("password").send_keys("tutorial")

        # click on  Sign In
        driver.find_element_by_name("login").click()

        time.sleep(5)

        # validate next page
        print (driver.title)
        assert "Find a Flight: Mercury Tours:" in driver.title

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
