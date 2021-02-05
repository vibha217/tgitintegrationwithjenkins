import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="./Resources/chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(3)
print(driver.title)
driver.find_element_by_id("twotabsearchtextbox").send_keys("mobiles")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)
mobileList = driver.find_elements_by_css_selector("div[data-component-type='s-search-result']")
print("The List of Numbers of Mobile in a single Page is :"+str(len(mobileList)))

for mobile in mobileList:
    print(mobile.text)
    print("\n")

    driver.close()
