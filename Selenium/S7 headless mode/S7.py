from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("Starting")


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

#---------HEADLESS method------------
options.add_argument("--headless")
#options.headless=True


driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe",
    options=options
)

try:
    print("Opening page")
    driver.get("https://soundcloud.com/")
    time.sleep(5)
    print("Accepting cookie")
    accepr_cookie = driver.find_element_by_id("onetrust-accept-btn-handler").click()
    time.sleep(5)
    print("I wish we can play music but idk how to do it!!!")
    #search_music = driver.find_element_by_name("q")
    #search_music.send_keys("Red Hot Chilli")

    music = driver.find_element_by_class_name("playableTile__playButton audibleTile__playButton g-z-index-content").click()
    #time.sleep(55)

    #time.sleep(9)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

print("Done")