from selenium import webdriver

# initiate webdriver
driver = webdriver.Firefox()

# open URL in browser
driver.get("https://www.facebook.com/")



# Close browser
#driver.close()

# quit webdriver instance
driver.quit()