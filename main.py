from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import urllib.request, urllib.error
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import threading

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless=new")
options.add_argument('--log-level=200')
LOGGER.setLevel(logging.CRITICAL)
user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '+'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
options.add_argument('user-agent=%s'%user_ag)

url = "https://note.com/moyashi5561/n/nb7ade54eae4b"
count = 0
def like(url):
    global count
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(2)
    humidity = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/main/div[1]/article/div[1]/div[1]/div/div[1]/div[1]/div/span/span/span/button").click()
    driver.quit()
    count = count + 1
    print(f"success: {count}")
URL = input("URL:")
num = input("いいね回数:")
for a in range(int(num)):
    like(URL)
