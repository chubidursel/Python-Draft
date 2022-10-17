#https://peter.sh/experiments/chromium-command-line-switches/
# working with Chrome driver we can pass a lot of different options to optimize work

#USER-AGENT = it's a string of text that is unique for each software or browser on the internet and holds the technical information about your device and operating system.
# User-agent is present in the HTTP headers when the browser wants to connect with the webserver.

from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
print("Starting")

#add OPTIONS
options = webdriver.ChromeOptions()
#--------------u can choseee any name as u want----------
#options.add_argument("user-agent=SalamBaurim")
#--------------mobile chrome > user-agent----------
#options.add_argument("Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
#--------------random user angent----------
'''''
user_agent_list = [
    'Whats uppp',
    'second agent',
    'Dan-Ban'
]
options.add_argument(f"user-agent={random.choice(user_agent_list)}")
'''''
#--------------fake user-agent----------
useragent = UserAgent()
options.add_argument(f"user-agent={useragent.random}")


url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe",
    options=options
)

try:
    driver.get(url=url)
    time.sleep(15)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

print("Done")