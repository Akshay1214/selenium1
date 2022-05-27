from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time

path = "//india.eclerx.com/ctrxdata/ARRDATA/Akshay.Deokar/Desktop/JN/chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
browser.get("https://www.amazon.in/")
browser.maximize_window()

input_search = browser.find_element(by=By.XPATH, value="//*[@id='twotabsearchtextbox']")
input_search.send_keys('Smartphones under 10000')
sleep(2)
search_button = browser.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")

search_button.click()
sleep(2)

result = []
for i in range(10):
    print('Scraping page', i+1)
    products = browser.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
    print(products)
    for product in products:
        result.append(product.text)
    next_button = browser.find_element(By.CLASS_NAME, 's-pagination-next').click()
    sleep(2)
    







