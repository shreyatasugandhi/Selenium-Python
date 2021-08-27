from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# initialise Webdriver for firefox driver
driver = webdriver.Firefox()

# open URL
driver.get("https://www.facebook.com/")

# locate by ID
driver.find_element_by_id("email").send_keys("test@abc.com")
driver.find_element(By.ID, "email").send_keys("test@abc.com")

# locate by name
driver.find_element(By.NAME, "pass").send_keys("test123")

# locate by class name
driver.find_element_by_id("email").clear()
driver.find_element(By.CLASS_NAME, "inputtext").send_keys("test@abc.com")

# locate by link text
driver.find_element(By.LINK_TEXT, "Forgot account?").click()
time.sleep(3)


# locate by partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, "I can't identify").click()
time.sleep(5)

# # locate by partial link text (another example)
# driver.get("http://newtours.demoaut.com/")
# driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()
# time.sleep(5)
# assert "Register: Mercury Tours" in driver.title


# locate by Tag name
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.find_element(By.TAG_NAME, "button").click()


###### locate by CSS ######
# Only ID  ==> #id
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("test@abc.com")

# # Tag + ID ==> tag#id
# element = driver.find_element(By.CSS_SELECTOR, "input#pass")
# element.clear()
# element.send_keys("test123")
#
# # Tag + Class ==> tag.class
# email = driver.find_element(By.CSS_SELECTOR, "input.inputtext")
# email.clear()
# email.send_keys("selenium@xyz.com")
#
# # Tag + Class + Attribute ==> tag.class[attribute=value]
# pass1 = driver.find_element(By.CSS_SELECTOR, "input.inputtext[name='pass']")
# pass1.clear()
# pass1.send_keys("pass123")
#
# # Tag + Attribute ==> tag[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("First Name")
#
#
# # Tag + ID + Attribute ==> tag#id[attribute]
# driver.find_element(By.CSS_SELECTOR, "input#u_0_6[aria-label='Mobile number or email']").send_keys("axy@abc.com")


####### XPath #########
# Using XPath - text box
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("First Name")




# Using XPath with class and index -- select a date
date = Select(driver.find_element(By.XPATH, ".//*[@class='_5dba'][2]"))
date.select_by_visible_text("5")
date.select_by_index(5)
date.select_by_value("7")

# # XPath with contains
# driver.find_element(By.XPATH, ".//button[contains(text(), 'Create Account')]").click()
#
# # XPath with contains for imgs
# driver.find_element(By.XPATH, "//img[contains(@src,'851565_602269956474188_918638970_n.png')]").click()
#
# # XPath with value -- Login button
# driver.get("http://newtours.demoaut.com/")     ### opening new tours site
# time.sleep(2)
# driver.find_element(By.NAME, "userName").send_keys("tutorial")
# driver.find_element_by_name("password").send_keys("tutorial")
# driver.find_element(By.XPATH, "//*[@value='Login']").click()
# time.sleep(3)
#
# # XPath with value -- radio button
# driver.find_element(By.XPATH, "//*[@value='oneway']").click()
#
# # moving back to facebook
# driver.get("http://www.facebook.com/")
# time.sleep(2)
#
# # XPath with select for select box
# Select(driver.find_element(By.XPATH, "//select[@aria-label='Day']")).select_by_visible_text("5")
#
# # Xpath with 2 attribute
# driver.find_element(By.XPATH, "//*[@type='password'][@tabindex='2']").send_keys("pass123")
# time.sleep(2)

# Close all windows and webdriver
driver.quit()