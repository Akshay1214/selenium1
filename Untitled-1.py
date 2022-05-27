from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time
import openpyxl
import sqlite3
import pandas as pd
import csv

path = "//india.eclerx.com/ctrxdata/ARRDATA/Akshay.Deokar/Desktop/JN/chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
browser.get("https://www.amazon.in/")
browser.maximize_window()

input_search = browser.find_element(by=By.XPATH, value="//*[@id='twotabsearchtextbox']")
input_search.send_keys('Samsung Phones')
sleep(2)
search_button = browser.find_element(by=By.XPATH, value="//*[@id='nav-search-submit-button']")
search_button.click()
samsung_category = browser.find_element(by=By.XPATH, value="//*[@id='p_89/Samsung']/span/a/div/label/i")
samsung_category.click()

phone_names = browser.find_elements(by=By.XPATH, value="//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
phone_prices = browser.find_elements(by=By.XPATH, value="//span[contains(@class, 'a-price-whole')]")

phone_details,price_details = [], []
print("Names Of Phones")

for name in phone_names:
    phone_details.append(name.text)

print("Phone Prices")

for price in phone_prices:
    price_details.append(price.text)

final_details = zip(phone_details,price_details)

print("Data Fetched.")

wb = openpyxl.Workbook()
sh1 = wb.active

for y in list(final_details):
    sh1.append(y)

wb.save("Final_Data.csv")

print("Data saved in your current directory.")

browser.quit()

connection = sqlite3.connect('simple_data.db')

cursor = connection.cursor()

create_table = CREATE TABLE Mobile_phone_details ( 
    Mobile_Name TEXT NOT NULL,
    Price INTEGER );

cursor.execute(create_table)

file = open('Final_Data.csv')
contents = csv.reader(file)

insert_records = INSERT INTO Mobile_phone_details (Mobile_Name, Price VALUES(?, ?))

cursor.executemany(insert_records, contents)

select_all = SELECT * FROM Mobile_phone_details
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connection.commit()
connection.close()










