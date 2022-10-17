# my computer >>> proxy server >>> web

from selenium import webdriver
import time


print("Starting")


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")

# set PROXY
#https://free-proxy-list.net/
# IP adress + port
options.add_argument("--proxy-server=52.201.218.80:8000")

# set Proxy with authorisation
#U need to import another library and add dict with password

url = 'https://www.ipaddress.my//'
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