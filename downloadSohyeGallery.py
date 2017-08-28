import random
import urllib.request
from bs4 import BeautifulSoup

def download_web_images(url):
    name = random.randrange(1,1001)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

if __name__ == "__main__":
    req = urllib.request.Request("http://gall.dcinside.com/board/lists/?id=kimsohye");
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')


    download_web_images('http://www.hmgjournal.com/images_n/contents/170616_sohot01.jpg')


