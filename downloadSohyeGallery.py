import random
import urllib.request as url
from bs4 import BeautifulSoup as BS
import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_web_images(url):
    name = random.randrange(1,1001)
    full_name = str(name) + ".jpg"
    url.urlretrieve(url, "./img/" + full_name)


if __name__ == "__main__":

    driver = webdriver.Chrome("C:\selenium\chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    bs = BS(driver.page_source, 'html5lib')

    bstring  = str(bs)

    f = open("./crawlWebpage.html", "wb")
    f.write(bstring.encode())
    f.close()

    driver.quit()



