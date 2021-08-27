# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains



class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://newtours.demoaut.com/"

    def test_slidertest(self):
        driver = self.driver
        driver.get("http://www.thetestroom.com/webapp/contact.html")
        self.assertEqual("Contact", driver.title)

        # Using Action Class
        slidebar = driver.find_element_by_id("slider-1")
        slider = driver.find_element_by_xpath(".//*[@id='slider-1']/a")

        move = ActionChains(driver)
        move.move_by_offset(40, 0).click(slidebar)

        # move on a horizontal slider
        slide = move.click_and_hold(slider).move_by_offset(34, 0).release()
        slide.perform()

        #move.drag_and_drop_by_offset(slider, 34, 0)
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
