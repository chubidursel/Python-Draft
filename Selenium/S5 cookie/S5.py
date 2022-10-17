from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pickle


print("Starting")


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")


driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe",
    options=options
)

try:
    driver.get(url="https://id.vk.com/")
    time.sleep(15)
    email_input = driver.find_element_by_name("login")
    email_input.clear()
    email_input.send_keys("+9379992")
    time.sleep(15)

#-------------cookie---------
    pickle.dump(driver.get_cookie(), open(f"{vk_phone}_cookies", "wb"))

#-------------coment code above and than use cookies---------
    driver.get("https://id.vk.com/")
    time.sleep(5)

    for cookies in pickle.load(open(f"{vk_phone}_cookies", "rb")):
        driver.add_cookie(cookies)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

print("Done")