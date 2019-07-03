#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_microservices(url):
    option = webdriver.FirefoxOptions()
    option.add_argument('-headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--start-maximized')
    driver = webdriver.Firefox(executable_path='/home/wangyang/Downloads/geckodriver', options=option)


    driver.get(url)
    wait = WebDriverWait(driver, 50)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "card-img-top")))
    driver.find_element_by_class_name('card-img-top').click()
    time.sleep(3)
    print("1.Check out the details of the goods successfully")

    
    wait = WebDriverWait(driver, 100)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "alert-link")))
    driver.find_element_by_class_name('alert-link').click()
    time.sleep(1)
    handles = driver.window_handles

    driver.switch_to.window(handles[1])
    wait = WebDriverWait(driver, 100)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-info.btn-lg.ml-3")))
    driver.find_element_by_class_name('btn.btn-info.btn-lg.ml-3').click()
    time.sleep(3)
    print("2.Check out advertisement and add cart successfully")

    driver.switch_to.window(handles[0])
    wait = WebDriverWait(driver, 100)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-info.btn-lg.ml-3")))
    driver.find_element_by_class_name('btn.btn-info.btn-lg.ml-3').click()
    time.sleep(3)
    print("3.Add cart successfully")


    wait = WebDriverWait(driver, 50) \
         .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary")))
    driver.find_element_by_css_selector("Button.btn.btn-primary").click()
    time.sleep(3)
    print("4.Checkout successfully")
    print("5.Your order is complete! ")
    print("============================")

if __name__ == '__main__':

    url = "http://ad79bcb0f949e11e9a35102cce2aac0b-865086301.ap-southeast-1.elb.amazonaws.com:80/"
    test_microservices(url)








