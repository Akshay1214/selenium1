from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time

path = "//india.eclerx.com/ctrxdata/ARRDATA/Akshay.Deokar/Desktop/JN/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.flipkart.com/")

time.sleep(5)

xButton = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/button').click()

searchBar = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchBar.send_keys('Chess')

searchButton = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
searchButton.click()

time.sleep(5)