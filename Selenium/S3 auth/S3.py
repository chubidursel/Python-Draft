from selenium import webdriver
import time
from password import my_password
from selenium.webdriver.common.keys import Keys

print("Starting")


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")


driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe",
    options=options
)

try:
    driver.get(url="https://www.vk.com/")
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("+9379992")
    time.sleep(15)

    password_input = driver.find_element_by_id("")
    password_input.clear()
    password_input.send_keys(my_password)
    time.sleep(5)
    password_input.send_keys(Keys.Enter)
    #login_button = driver.find_element_by_id("").click()
    time.sleep(5)






except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

print("Done")