from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/driver/chromedriver.exe")
driver.maximize_window();

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("PT Sumber Alfaria Trijaya")
driver.find_element_by_name("bntK").click()
driver.find_element_by_name("submit").click()