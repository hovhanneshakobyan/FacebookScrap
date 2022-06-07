#!/usr/bin/python3

from selenium.webdriver.common.action_chains import ActionChains as A
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import pyautogui
import random
import pyperclip
import codecs
import urllib
import json



def init_web_driver():
    browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
    sleep(1)
    return browser

def get_page(browser):
    browser.get("https://www.facebook.com/")
    sleep(1)

def log_in(browser):
    #Your facebook login
    browser.find_element_by_id('email').send_keys("#there")
    sleep(1)
    #Your password
    browser.find_element_by_id('pass').send_keys("#there")
    sleep(1)
    browser.find_element_by_id('pass').send_keys(Keys.ENTER)
    sleep(3)

def find_user_account(browser): 
    #account that you want to scrap
    browser.get("")
    sleep(2)

def find_scroll(browser):
    browser.execute_script("window.scrollBy(0,1500)","")
    sleep(7)
    browser.execute_script("window.scrollBy(0,500)","")
    sleep(5)
#def find_publisher(browser):
    #publisher = browser.find_element_by_class_name("nc684nl6")
    #publisher = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2/span/a/strong/span")
    #sleep(4)
    #publisher_name = publisher.text
    #print(publisher_name)
    #asd = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/span/div/div").text
    #sleep(2)
    #print(asd)

#def find_likes(browser):
    #likes_list = []
    #likes = browser.find_elements_by_()
    #for like in likes: 
        #print(like.text)
        #likes_list.append(like.text)
    #print(likes_list)

def find_picture(browser):
    anchor = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/video")
    elem = browser.find_element_by_tag_name('video')
    #print("aaaaaa")
    sleep(7)
    video =elem.get_attribute('src')
    print(video)
    #src = anchor.get_attribute("scr")
    #print(src)

def find_video_src(browser):
    video = browser.find_element_by_class_name("k4urcfbm")
    sleep(10)
    source = video.get_attribute("src")
    print(source)

def find_likes(browser): 
    names_lis = browser.find_elements_by_class_name("lrazzd5p")
    #print(nams_lis.text)
    #print(len(names_lis))
    sleep(5)
    for name in names_lis:
        print(name.text)

    
    #a = browser.find_element_by_class_name("j83agx80")
    #print (type(a))
    #friends = browser.find_elements_by_class_name("q9uorilb")
    #sleep(5)
    #print(friends)
    
    #a = browser.find_element_by_class_name("oajrlxb2").text
    #print(a)
    
    #for friend in friends:
        #name = browser.find_element_by_tag_name('a')
        #print(name.text)
    
    #list1 = [1,2,3,4,5,6,7,8,9,10]
    #coment = random.choice(list1)
    #qarers = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/span/div/a")
    #sleep(5)
    #for qarer in qarers:
        #sleep(4)
        #browser.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[{coment}]/div/div/div[2]/div[1]/div/div/div/span/div/a") 
   
def find_comments(browser):
    
    likes = browser.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/span/div/a")
    for like in likes:
        sleep(3)
        print(likes)

def find_click(browser):
    #browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/span/span/span[1]/span/span/div/img")
    pyautogui.moveTo(780 ,540 ,duration =2)
    sleep(1)
    pyautogui.click()
    sleep(2)
    pyautogui.click()
    pyautogui.moveTo(938 , 624 ,duration=1)
    pyautogui.click()    


def find_aaas(browser):
    browser.execute_script("window.scrollBy(0,1500)","")

def find_lik(browser):
    a = browser.find_elements_by_css_selector("html#facebook._9dls body._6s5d._71pn._-kb div#mount_0_0_2O div div div.rq0escxv.l9j0dhe7.du4w35lb div div div.__fb-light-mode.l9j0dhe7.tkr6xdv7 div.rq0escxv.l9j0dhe7.du4w35lb div.j83agx80.cbu4d94t.h3gjbzrl.l9j0dhe7 .oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p")
    print(a)


def main():
    browser = init_web_driver()
    get_page(browser)
    log_in(browser)
    find_user_account(browser)
    find_scroll(browser)
    #find_publisher(browser)
    #find_likes(browser)
    #find_picture(browser)
    #find_video_src(browser)
    #find_likes(browser)
    #find_comments(browser)
    find_click(browser)
    find_aaas(browser)
    find_lik(browser)
if __name__== "__main__":
    main()
