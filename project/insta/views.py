from django.shortcuts import render,redirect
# import datetime
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time, urllib.request
from selenium.webdriver.common.by import By
from django.contrib.auth import authenticate
# import requests
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.




def adminlogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(request,username=uname,password=pwd)
        print(user,"hhh")
        if user:
            if user.is_staff==1:
                login(request,user)
                return redirect('hm')
        messages.error(request, 'Incorrect username or Password', extra_tags='text-danger')
    return render(request,'sign-in.html')

# logout button
def logoutUser(request):
    logout(request)
    return redirect('adminlogin')

# home, after login shows searchbox for whose account should be checked
@login_required(login_url='login')
def home(request):
    cat=Category.objects.all()
    search=Searchid.objects.all()
    if request.method=="POST":
        userid=request.POST['userid']
        cats=request.POST['category']
        request.session['fav_color'] = userid
        request.session['category'] = cats
        return logins(request,userid)
    context={'cat':cat,'search':search}
    return render(request,'dashboard.html',context)

# Create your views here.
@login_required(login_url='login')
def logins(request,userid):
    print(userid)
    if request.method=="POST":
        # uname=request.POST['uname']
        # pwd=request.POST['pwd']
        uname="abhinavchandra2604"
        pwd="ABHInavchandra1708580a"
        # user=authenticate(request,username=uname,password=pwd)
        PATH = r"C:\Users\ACER\OneDrive\Desktop\New folder\New folder\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        username = driver.find_element("name",'username')
        password = driver.find_element("name",'password')
        username.clear()
        password.clear()
        username.send_keys(uname)
        time.sleep(2)
        password.send_keys(pwd)
        time.sleep(3)
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #save your login info?
        time.sleep(5)
        urls=driver.current_url
        
        # try:
        #     notnow = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
        # except:
        # #turn on notif
        #     time.sleep(10)
        #     notnow2 = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
        # time.sleep(10)
        # #searchbox
        # if urls!="https://www.instagram.com/":
        caat = request.session['category']
        while (urls!="https://www.instagram.com/accounts/onetap/?next=%2F"):
            time.sleep(5)
            urls=driver.current_url
            if urls=="https://www.instagram.com/":
                break
        driver.get(f"https://www.instagram.com/{userid}/{caat}/")
        time.sleep(5)
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
        if caat=="followers":
            scroll=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        elif caat=="following":
            scroll=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        time.sleep(5)
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
        
        # print(users)
        # print(user)
        #print(f"{line} follower list done!!! {line}")
        # hit close button    
        if caat=="followers":
            close=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()
        elif caat=="following":
            close=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()
        time.sleep(4)   

        #convert list to string
        # converting = driver.converting(names)
        # print(f"{line} convert list to string  Done!!! {line}")
        list3=zip(users,user)
        # for i,j in list3:
        #     print(i,j)
        # urllib.request.urlretrieve(download_url,f'{i}.jpg'.format(shortcode),'project\insta\static\media'f'{i}.jpg')
        download_url = ''
        time.sleep(4)
        shortcode = driver.current_url.split("/")[-2]
        # with open('list.txt', 'a') as f:
        #     #line

        categ=Category.objects.get(types=caat)
        # print(search.id,categ.id)
        try:
            search=Searchid.objects.get(userid=userid)
            print(search.id)
            seid=search.id
            print(seid)
        except:
            # print(search)
            searchnew=Searchid.objects.create(userid=userid)
            print(searchnew)
            seid=searchnew.id
            print(seid)
            

        pre=insta.objects.filter(accound=userid)
        print(pre)
        if pre == None:
            print('none')
            for i,j in list3:
                download_url =j
                urllib.request.urlretrieve(download_url,f'C:/Users/ACER/OneDrive/Desktop/working projects/insta/project/insta/static/media/{i}.jpg')
                dps=f'{i}.jpg'
                insta.objects.create(username=i,dp=dps,accound=userid,category=categ)
        else:
            print("not empty")
            for i,j in list3:
                print(i,j)
                ins=insta.objects.filter(username=i,accound=userid)
                print(ins)
                if ins.exists():   
                    print('old')
                    print(i,userid)
                    try :
                        instass= insta.objects.get(username=i,accound=userid,category=categ)
                        print(instass)
                    except:
                        dps=f'{i}.jpg'
                        print(i,userid)
                        insta.objects.create(username=i,accound=userid,category=categ,dp=dps)
                        # instass=insta.objects.get(username=i,accound=userid)
                        # instass=insta.objects.get(username=i,accound=userid)
                        # instass.category=categ.id
                        # instass.save()
                        print(f'old id addedcategory:{categ.types}({categ})')
                        # insta.objects.create(username=i,dp=dps,accound=userid,category=categ.id)
                else:
                    print('found new follower')
                    download_url =j
                    urllib.request.urlretrieve(download_url,f'C:/Users/ACER/OneDrive/Desktop/working projects/insta/project/insta/static/media/{i}.jpg')
                    dps=f'{i}.jpg'
                    insta.objects.create(username=i,dp=dps,accound=userid,category=categ)
                    print('old')
            print('for completed successfully')
        # return render(request,'fetch')
        return redirect('fetch')
    # print("not gone to next step")
    # return redirect('hm')

def viewlist(request,pk):
    se=Searchid.objects.get(id=pk)
    instas=insta.objects.filter(accound=se.userid)
    search=Searchid.objects.all()
    context = {'instas': instas,'search':search}
    return render(request,"viewfetchlist.html",context)

def view_fetch(request):
    pk = request.session['fav_color']
    print('view fetch called')
    instas=insta.objects.filter(accound=pk)
    cn=len(instas)
    for i in range(0,cn):
        instas=insta.objects.filter(accound=pk)[i]
        print(instas.answer)
        if instas.answer==None:
            new=i
            break
    print(new,instas)
    now=new
    print(instas)
    if request.method=="POST":
        data=request.POST
        print('post called')
        question=data['button']
        print(question)
        if question!='userid':
            now=data['index']
            print(question,now)
            # count=len(insta.objects.filter(accound=pk))
            # print(count)
            index = getnum(now,cn)

            if index==None:
                return redirect('hm')
            print(index)

            if question=="Skip":
                print('skip working')
                for i in range(index,cn):
                    instas=insta.objects.filter(accound=pk)[i]
                    print(instas.answer)
                    if instas.answer==None:
                        new=i
                        break
                index=new
                # instas=insta.objects.filter(accound=pk)[index]
                context = {'instas': instas,'now':index}
                return render(request,"viewfetch.html",context)
            else:
                print('not skiped')
                now=int(now)
                instas=insta.objects.filter(accound=pk)[now]
                print(question)
                print(instas.question)
                instas.question = "who is this person to you"
                instas.answer = question
                instas.save()
                print('datas saved')
                for i in range(index,cn):
                    instas=insta.objects.filter(accound=pk)[i]
                    print(instas.answer)
                    if instas.answer==None:
                        new=i
                        break
                index=new
                context = {'instas': instas,'now':index}
            return render(request,"viewfetch.html",context)
        else:
            pk=request.session['userid']
            instas=insta.objects.filter(accound=pk)
            cn=len(instas)
            for i in range(0,cn):
                instas=insta.objects.filter(accound=pk)[i]
                print(instas.answer)
                if instas.answer==None:
                    new=i
                    break
            print(i,instas)
            now=new
    context = {'instas': instas,'now':now}
    return render(request,"viewfetch.html",context)
    

def getnum(now,count):
    print('getnum called with values:',now,count)
    now=int(now)
    count=int(count)-1
    print(now,count)
    if count > now: 
        numb=now+1
        print(now,numb)
        return numb
    else:
        return None

    


    

def instalogin(request):
    global uname
    print(uname)
    global pwd
    