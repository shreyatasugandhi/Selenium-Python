from selenium import webdriver

# # initialise Webdriver for firefox driver
# driver = webdriver.Firefox()

# # initialise Webdriver for firefox driver
# driver = webdriver.Ie()


# initialise Webdriver for firefox driver
driver = webdriver.Chrome()


# Open URL in browser
driver.get("http://newtours.demoaut.com/")

# find username textbox and type valid username
driver.find_element_by_name("userName").send_keys("tutorial")

# find password textbox and type valid password
driver.find_element_by_name("password").send_keys("tutorial")

# Click on 'Sign In' button to log into the application
driver.find_element_by_name("login").click()


# Close current window
driver.close()


# close webdriver instance
driver.quit()