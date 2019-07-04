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
    firefox_binary = FirefoxBinary('./firefox/')
    driver = webdriver.Firefox(executable_path='./geckodriver', options=option,firefox_binary=firefox_binary)

    driver.get(url)
    wait = WebDriverWait(driver, 50)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "card-img-top")))
    print("frontend success")
    driver.find_element_by_class_name('card-img-top').click()
    time.sleep(3)

    #/product/L9ECAV7KIM
    wait = WebDriverWait(driver, 50)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-info.btn-lg.ml-3")))
    print("product success")
    driver.find_element_by_class_name('btn.btn-info.btn-lg.ml-3').click()
    time.sleep(3)

    #/cart
    wait = WebDriverWait(driver, 50) \
         .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-secondary")))
    print("cart success")
    wait = WebDriverWait(driver, 50) \
         .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary")))
    driver.find_element_by_class_name("btn.btn-primary").click()
    time.sleep(3)

    wait = WebDriverWait(driver, 50) \
         .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary")))
    print("cart/checkout success")
    time.sleep(3)

    driver.get(url)
    wait = WebDriverWait(driver, 50)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "alert-link")))
    time.sleep(3)
    print("frontend success by url")
    
    driver.get("http://ad79bcb0f949e11e9a35102cce2aac0b-865086301.ap-southeast-1.elb.amazonaws.com/product/L9ECAV7KIM")
    wait = WebDriverWait(driver, 50)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-info.btn-lg.ml-3")))
    time.sleep(3)
    print("product success by url")

    driver.get("http://ad79bcb0f949e11e9a35102cce2aac0b-865086301.ap-southeast-1.elb.amazonaws.com/cart")
    wait = WebDriverWait(driver, 50) \
         .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-secondary")))
    time.sleep(3)
    print("cart success by url")

    #driver.get("http://ad79bcb0f949e11e9a35102cce2aac0b-865086301.ap-southeast-1.elb.amazonaws.com/cart/checkout")
    #wait = WebDriverWait(driver, 50) \
    #     .until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary")))
    #time.sleep(3)

if __name__ == '__main__':

    url = "http://ad79bcb0f949e11e9a35102cce2aac0b-865086301.ap-southeast-1.elb.amazonaws.com:80/"
    test_microservices(url)

