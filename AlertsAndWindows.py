from telnetlib import EC
from selenium.webdriver.support.expected_conditions import new_window_is_opened
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import unittest, time

from selenium.webdriver.support.wait import WebDriverWait


class AlertsAndWindow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.thetestroom.com/webapp/index.html"

    def test_Login_test(self):
        driver = self.driver

        # open application
        driver.get(self.base_url)

        ##### Windows #####
        self.assertEqual("Zoo Adoption | Home", driver.title)
        handle1 = driver.current_window_handle

        driver.find_element(By.LINK_TEXT, "Terms").click()

        try:
            WebDriverWait(driver, 10).until(EC.new_window_is_opened(handle1))
        except TimeoutException :
            print "Time out! Window didn't open."

        assert driver.title == "Terms of the site"
        handle2 = driver.window_handles
        #driver.close(handle2)
        handle2.remove(handle1)
        driver.switch_to.window(handle2[0])
        assert driver.title == "Zoo Adoption | Home"

        driver.find_element_by_link_text("CONTACT").click()
        time.sleep(10)
        driver.find_element_by_id("submit_message")
        time.sleep(1)

        #### Alerts #####
        alert_text = Alert(driver).text
        self.assertEqual("Name field is empty", alert_text)
        Alert(driver).accept()




    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
