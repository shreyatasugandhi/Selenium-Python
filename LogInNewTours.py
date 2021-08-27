from selenium import webdriver
import time

# initiate webdriver for firefox
driver = webdriver.Firefox()

# Oepn URL
driver.get("http://newtours.demoaut.com/")

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

# Quit webdriver
driver.quit()