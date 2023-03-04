from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
from selenium.webdriver.common.by import By
import requests
# line = "#"*15

PATH = r"C:\Users\ACER\OneDrive\Desktop\New folder\New folder\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

#login
time.sleep(10)
username = driver.find_element("name",'username')
password = driver.find_element("name",'password')
username.clear()
password.clear()
username.send_keys("abhi_26_04")
password.send_keys("ABHInavchandra1708580a")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


#save your login info?
time.sleep(10)
notnow = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(10)
notnow2 = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
time.sleep(10)
# #searchbox

driver.get("https://www.instagram.com/abhi_26_04/following/")
time.sleep(10)
# searchbox = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']")
# searchbox.clear()
# searchbox.send_keys("sha_roo_k")
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# # # follow
# # profileh=driver.find_element(By.CSS_SELECTOR,"div[class='_aaav']").click()
# # time.sleep(4)
# # profi=driver.find_element(By.CSS_SELECTOR,"div[href='/abhinavchandra2604/']").click()
scroll=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
time.sleep(10)
# height variable
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(4)
        # scroll down and retrun the height of scroll (JS script)
    ht =driver.execute_script(""" 
    arguments[0].scrollTo(0, arguments[0].scrollHeight);
    return arguments[0].scrollHeight; """, scroll)

# list follower name
time.sleep(4)
#print(f"{line} Scroll Buttom  Done!!! {line}")
links = scroll.find_elements(By.CSS_SELECTOR,'a')

time.sleep(4)
users={}

for i in links:
    if i.get_attribute('href'):
        
        users.update({i.get_attribute('href').split("/")[3]:[]})
        
    else:
        continue
users=list(users)
link=scroll.find_elements(By.TAG_NAME,'img')
time.sleep(4)
user=list()
for i in link:
    if i.get_attribute('src'):
        
        user.append(i.get_attribute('src'))
    else:
        continue
time.sleep(4)
# names = [name.text for name in links if name.text != '']
# need to filter empty string so we used name.text instead of name
#print(names)
print(users)
print(user)
#print(f"{line} follower list done!!! {line}")
# hit close button    
close=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()
time.sleep(4)   

#convert list to string
# converting = driver.converting(names)
# print(f"{line} convert list to string  Done!!! {line}")
list3=zip(users,user)
# for i,j in list3:
#     print(i,j)


time.sleep(4)
with open('list.txt', 'a') as f:
    #line
    for i,j in list3:
        f.write(i +' '+ j+ '\n')

# with open('list.txt', 'a') as f:
# #line
#     f.write(f"{line} {type} {line} \n")
#     for i in names:
#         f.write(i + '\n')
#self.quiting()

# #scroll

# scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
# match=False
# while(match==False):
#     last_count = scrolldown
#     time.sleep(2)
#     scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#     if last_count==scrolldown:
#         match=True

# #posts
# posts = []
# links = driver.find_elements(By.TAG_NAME,'a')
# for link in links:
#     post = link.get_attribute('href')
#     if '/p/' in post:
#       posts.append(post)

# print(posts)


# #get videos and images
# download_url = ''
# for post in posts:	
# 	driver.get(post)
# 	shortcode = driver.current_url.split("/")[-2]
# 	time.sleep(4)
# 	if driver.find_element(By.CSS_SELECTOR,"img[style='object-fit: cover;']") is not None:
# 		download_url = driver.find_element(By.CSS_SELECTOR,"img[style='object-fit: cover;']").get_attribute('src')
# 		urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
# 	else:
# 		download_url = driver.find_element(By.CSS_SELECTOR,"video[type='video/mp4']").get_attribute('src')
# 		urllib.request.urlretrieve( download_url, '{}.mp4'.format(shortcode))
# 	time.sleep(3)