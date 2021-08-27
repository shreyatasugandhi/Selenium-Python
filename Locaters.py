from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# initialise Webdriver for firefox driver
driver = webdriver.Firefox()

# open URL
driver.get("https://www.facebook.com/")

# locate by ID
driver.find_element_by_id("email").send_keys("test@abc.com")

# locate by name
driver.find_element_by_name("pass").send_keys("test123")

# locate by class name
driver.find_element_by_id("email").clear()
driver.find_element_by_class_name('inputtext').send_keys("test@abc.com")

# locate by link text
driver.find_element_by_link_text("Forgot account?").click()
time.sleep(3)

# locate by partial link text
driver.find_element_by_partial_link_text("I can't identify").click()
time.sleep(5)

# locate by partial link text (another example)
driver.get("http://newtours.demoaut.com/")
driver.find_element_by_partial_link_text("Register").click()
time.sleep(5)
assert "Register: Mercury Tours" in driver.title

# locate by Tag name
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.find_element_by_tag_name("button").click()

###### locate by CSS ######
# Only ID  ==> #id
driver.find_element_by_css_selector("#email").send_keys("test@abc.com")

# Tag + ID ==> tag#id
element = driver.find_element_by_css_selector("input#pass")
element.clear()
element.send_keys("test123")

# Tag + Class ==> tag.class
email = driver.find_element_by_css_selector("input.inputtext")
email.clear()
email.send_keys("selenium@xyz.com")

# Tag + Class + Attribute ==> tag.class[attribute=value]
pass1 = driver.find_element_by_css_selector("input.inputtext[name='pass']")
pass1.clear()
pass1.send_keys("pass123")

# Tag + Attribute ==> tag[attribute=value]
driver.find_element_by_css_selector("input[name='firstname']").send_keys("Shreyata")

# Tag + ID + Attribute ==> tag#id[attribute]
driver.find_element_by_css_selector("input#u_0_6[aria-label='Mobile number or email']").send_keys("axy@abc.com")


####### XPath #########
# Using XPath - text box
fname = driver.find_element_by_xpath("//input[@name='firstname']")
fname.clear()
fname.send_keys("First Name")

# Using XPath with class and index -- select a date
date = Select(driver.find_element_by_xpath(".//*[@class='_5dba'][2]"))
date.select_by_visible_text("5")
time.sleep(2)
date.select_by_index(1)
time.sleep(2)
date.select_by_value("7")

# XPath with contains
driver.find_element_by_xpath(".//button[contains(text(), 'Create Account')]").click()

# XPath with contains for imgs
driver.find_element_by_xpath(".//img[contains(@src, '851565_602269956474188_918638970_n.png')]").click()

# XPath with value -- Login button
driver.get("http://newtours.demoaut.com/")     ### opening new tours site
time.sleep(2)
driver.find_element_by_name("userName").send_keys("tutorial")
driver.find_element_by_name("password").send_keys("tutorial")

driver.find_element_by_xpath("//*[@value='Login']").click()
time.sleep(3)

# XPath with value -- radio button
driver.find_element_by_xpath("//*[@value='oneway']").click()


# IP = "10.56.88.55"
# port = "8888"
# driver.get("http://" + IP + ":" + port + "/")
#

# moving back to facebook
driver.get("https://www.facebook.com/")
time.sleep(2)


# XPath with select for select box
Select(driver.find_element_by_xpath("//select[@aria-label='Day']")).select_by_visible_text("5")

# Xpath with 2 attribute
driver.find_element_by_xpath("//*[@type='password'][@tabindex='2']").send_keys("pass123")
time.sleep(2)


# Close all windows and webdriver
driver.quit()