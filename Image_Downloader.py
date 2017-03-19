import random
import urllib.request


def download_image_url(url):
    name = random.randrange(1, 1000000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

url = input("Enter URL: ")
download_image_url(url)
