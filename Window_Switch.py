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

        driver.get("xhtmlTest.html")
        current = driver.current_window_handle
        driver.find_element_by_link_text("Open new window").click()
        assert driver.title == "XHTML Test Page"
        handles = driver.window_handles
        handles.remove(current)
        driver.switch_to.window(handles[0])
        assert driver.title == "We Arrive Here"
        driver.get("iframes.html")
        handle = driver.current_window_handle
        driver.find_element_by_id("iframe_page_heading")
        driver.switch_to.frame(driver.find_element(By.ID, "iframe1"))
        assert driver.current_window_handle == handle

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
