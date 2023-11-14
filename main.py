import requests
import html5lib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.FirefoxOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)



#get user input for the URL
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
url = input("Enter your URL: ")
driver.get(url)
btn = driver.find_elements(By.XPATH, "//div[@class='panel']")
#for bt in btn:
#    bt.click()
#    print(bt.text)

points = btn[-1]
points.click()
driver.implicitly_wait(3)
#time.sleep(3)
new_item = driver.find_elements(By.XPATH, "//div[@class='hidden-print p24_poi']")
# for div in new_item:
#     print(div.text)
# print(points.text)
page_source = driver.page_source
print(page_source)

#soup = BeautifulSoup(page_source, 'html5lib')
#print(soup.prettify())
#find the suburb if it isn't a direct address
#suburb = soup.findAll('div', attrs={'class': 'p24_mBM'})[2].text
#print(suburb)
#find points of interest
#points = soup.find('div', attrs={'id': 'accordian-points-of-interest'})
#points = soup.find('div', attrs={'class': 'row'})


#pointsArr = [points.text for point in points]
#print(points.text)
