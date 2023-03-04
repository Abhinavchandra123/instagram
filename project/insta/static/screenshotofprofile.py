import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
from selenium.webdriver.common.by import By
import requests
# line = "#"*15

PATH = r"C:\Users\ACER\OneDrive\Desktop\New folder\New folder\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
def __init__(self,username,password):
    #login
    time.sleep(10)
    username = driver.find_element("name",'username')
    password = driver.find_element("name",'password')
    username.clear()
    password.clear()
    username.send_keys("abhi_26_04")
    password.send_keys("ABHInavchandra1708580a")
    login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def closepopup():
    #save your login info?
    time.sleep(10)
    notnow = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
    #turn on notif
    time.sleep(10)
    notnow2 = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
    time.sleep(10)
def following():
    # #searchbox
    driver.get("https://www.instagram.com/abhi_26_04/following/")
    time.sleep(14)
    # scroll
    scroll=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
    time.sleep(10)

    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(10)
            # scroll down and retrun the height of scroll (JS script)
        ht =driver.execute_script(""" 
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight; """, scroll)
    time.sleep(4)
    posts = []
    links = scroll.find_elements(By.CSS_SELECTOR,'a')
    for i in links:
        if i.get_attribute('href'):
            
            posts.append(i.get_attribute('href'))
            
        else:
            continue
def openprofile(posts):
    print(posts)
    download_url = ''
    for post in posts:
        time.sleep(8)
        

        driver.get_screenshot_as_file(f'./screenshot_name{int(time.time())}.png')
        driver.get(post)
        
        shortcode=driver.current_url.split("/")[-2]
        time.sleep(5)
    
	# if driver.find_element(By.CSS_SELECTOR,"img[style='object-fit: cover;']") is not None:
	# 	download_url = driver.find_element(By.CSS_SELECTOR,"img[style='object-fit: cover;']").get_attribute('src')
	# 	urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
        
	# else:
	# 	download_url = driver.find_element(By.CSS_SELECTOR,"video[type='video/mp4']").get_attribute('src')
	# 	urllib.request.urlretrieve( download_url, '{}.mp4'.format(shortcode))
	# time.sleep(3)
