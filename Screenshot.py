from selenium import webdriver
import time

# initialise Webdriver for firefox driver
driver = webdriver.Firefox()

# Open URL in browser
driver.get("http://newtours.demoaut.com/")

# find username textbox and type valid username
driver.find_element_by_name("userName").send_keys("tutorial")

# find password textbox and type valid password
driver.find_element_by_name("password").send_keys("tutorial")

# Click on 'Sign In' button to log into the application
driver.find_element_by_name("login").click()
time.sleep(3)

####### Screen shot ###
driver.save_screenshot("D:\Work\Freelance\Trainings\Selenium\Selenium_Python\Project\UST\SIUA_Proect\Screenshot\screenshot.png")

driver.get_screenshot_as_file("D:\Work\Freelance\Trainings\Selenium\Selenium_Python\Project\UST\SIUA_Proect\Screenshot\screenshot1.png")

# Close current window
driver.close()


# close webdriver instance
driver.quit()