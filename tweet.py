# coding:utf-8
import time
import datetime
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')

username = "kuma__san__dayo"
password = "megu0804"
tweet_text = "Test Tweet"

options = Options()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://x.com/login")

time.sleep(5)

username_field = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username_field.send_keys(username, Keys.ENTER)

time.sleep(1)

password_field = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_field.send_keys(password, Keys.ENTER)

time.sleep(3)

def tweet():
    now = datetime.datetime.now(JST)
    t = now.time().strftime('%X')
    tweet_field = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    tweet_field.send_keys(tweet_text + " "+  t)
    tweet_field.send_keys(Keys.COMMAND + Keys.ENTER)

def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

schedule(60, tweet, False)

