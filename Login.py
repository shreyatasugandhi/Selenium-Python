from selenium import webdriver

# initiate webdriver
driver = webdriver.Firefox()

# open URL in browser
driver.get("https://www.facebook.com/")

# enter email id
driver.find_element_by_id("email").send_keys("email.id@abc.com")

# enter password
driver.find_element_by_name("pass").send_keys("password123")

# click on 'LogIn' button
driver.find_element_by_id("u_0_o").click()


# locate by link text
driver.find_element_by_link_text("Forgot account?").click()


# Close browser
#driver.close()

# quit webdriver instance
#driver.quit()