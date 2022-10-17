from selenium import webdriver
import time

print("Starting")


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

# disable  webdriver mode
#https://peter.sh/experiments/chromium-command-line-switches/
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\!!PROJECTS\\Selenium\\driver\\chromedriver.exe",
    options=options
)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

print("Done")