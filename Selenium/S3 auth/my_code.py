from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("Starting")

word = input("write the word: ")

options = webdriver.ChromeOptions()
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="/!!PROJECTS/Selenium/driver/chromedriver.exe",
    #options=options
)


driver.get(url="https://dictionary.cambridge.org/")
time.sleep(2)
email_input = driver.find_element_by_id("searchword")

email_input.send_keys(word)
time.sleep(5)


# ------------PRESS KEYS------------
email_input.send_keys(Keys.ENTER)
#login_button = driver.find_element_by_class_name("bo iwc iwc-40 hao lb0 cdo-search-button lp-0").click()
time.sleep(10)

driver.close()
driver.quit()

print("Done")