#Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.
#

from selenium import webdriver
import time

print("Starting")

url = 'https://www.youtube.com/'

driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
    #driver.get(url="https://coinmarketcap.com/")
    #time.sleep(5)

    #driver.get_screenshot_as_file('1.png')
    #time.sleep(3)

    driver.refresh()
    time.sleep(2)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

print("Done")