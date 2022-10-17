from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time

PATH = 'C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(7)


#link = driver.find_element_by_link_text('Python Programming')
#link.click()

driver.quit()