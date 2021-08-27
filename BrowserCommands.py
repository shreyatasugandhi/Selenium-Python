from selenium import webdriver
import time

# initialise Webdriver for firefox driver
driver = webdriver.Firefox()

# Maximize window
driver.maximize_window()

# Open URL in browser
driver.get("http://facebook.com/")

# click link
driver.find_element_by_link_text("Forgot account?").click()
driver.implicitly_wait(3)

# browser back
driver.back()

# broser forward
driver.forward()

# refresh browser
driver.refresh()

# print title of browser
print (driver.title)

# print current url
print (driver.current_url)

# get name of the browser
print (driver.name)


# submit the form
driver.get("http://newtours.demoaut.com/")
time.sleep(4)

# Close current window
driver.close()

# close webdriver instance
driver.quit()
