import time

def Login(self, driver, user="steve", passwd="Student@123"):
    driver.get("http://lmsupgrade.mentor-global.com/login/index.php")
    self.assertEqual("Mentor Global Learning Solutions: Log in to the site", driver.title)
    driver.find_element_by_id("username").click()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_id("loginbtn").click()
    time.sleep(3)
    self.assertEqual("Mentor Global Learning Solutions", driver.title)

def OpenBlog(self, driver):
    driver.find_element_by_xpath(".//*[@id='inst4']/div/div[4]/ul/li/ul/li[2]/p").click()
    # driver.find_element_by_xpath(".//*[@id='inst4']/div/div[4]/ul/li/ul/li[2]/ul/li[1]/p/a/span").click()
    time.sleep(3)
    self.assertEqual("Mentor Global Learning Solutions", driver.title)
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    self.assertEqual("Mentor Global Learning Solutions: Log in to the site", driver.title)
