from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

def runshot(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    with open("/home/yatish609/Documents/SubShot/Filtered_Subdomains/Filtered_subdomains.txt","r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print(content)
    count = 0
    for i in content:
        url = i
        driver.get(url)
        driver.save_screenshot("/home/yatish609/Documents/SubShot/images/" + str(count) + ".png")
        count = count + 1