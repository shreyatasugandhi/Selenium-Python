WebDriverWait(driver, 10).EC.presence_of_element_located((By.ID, "username"))


WebDriverWait(driver, 20).until(wait.title_contains("Welcome"))


WebDriverWait(driver, 10).until(EC.element_to_be_selected(("oneway")))



wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'username')))