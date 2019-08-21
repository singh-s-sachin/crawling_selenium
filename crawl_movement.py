from selenium import webdriver
import pandas as pd
import database
import time
import os
def crwal(page,location):
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    driver = webdriver.Chrome()
    driver.get(page)
    time.sleep(8)
    cookiebtn=driver.find_element_by_xpath("//div[@class='close-cookie']")
    cookiebtn.click()
    time.sleep(2)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(2)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(2)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(2)
    lst=driver.find_elements_by_xpath("//input[@aria-autocomplete='list']")
    lst[1].click()
    popup=driver.find_elements_by_xpath("//ul[@role='listbox']/li")
    popup[location].click()
    time.sleep(5)
    time.sleep(2)
    #data=driver.find_element_by_xpath("//button[@class='ce ae b5 ag bz az ay bc an ep eq er es et d9 eu ev cr cs b4 ew ex ey ez f0 f1 f2 f3 f4 f5 f6 f7 cc c9 ca cb d0 eo cf f8 f9 fa']")
    #data.click()
    #time.sleep(3)
    downloadbtn=driver.find_element_by_xpath("//button[@class='bt ae ah bn f1 dj f2 f3 cv cw c1 f4 f5 f6 cd ca cb cc b3 c6 ci bv f7 f8 f9 fa fb fc fd fe ff fg fh fi fj da f0 ch fk fl fm']")
    downloadbtn.click()
    if location==21:
        time.sleep(20)
    else:
        time.sleep(3)
    data=driver.find_element_by_xpath("//button[@class='btn btn--link hard--left push-tiny--right']")
    data.click()
    time.sleep(3)
    text_area = driver.find_element_by_id('firstName')
    text_area.send_keys("Iuahuiwfiawnxui")
    text_area = driver.find_element_by_id('lastName')
    text_area.send_keys("Wxhjvfgpd")
    text_area = driver.find_element_by_id('email')
    text_area.send_keys("j@j.com")
    text_area = driver.find_element_by_id('role')
    text_area.send_keys("Analyst")
    text_area = driver.find_element_by_id('plannedUsage')
    text_area.send_keys("Analysis")
    purpose=driver.find_element_by_xpath("//div[@class='ay d9 da db dc c2 dd co de df dg d7 dh bp']")
    purpose.click()
    purpose=driver.find_element_by_xpath("//li[@class='b3 c6 ci bv cg c7 c2 c1 di jg cv cw cc jd je fe fd bq']")
    purpose.click()
    time.sleep(1)
    change=driver.find_element_by_xpath("//button[@type='submit']")
    change.click()
    time.sleep(3)
    close_button=driver.find_element_by_xpath("//button[@aria-label='Close']")
    close_button.click()
    print("DATA IS DOWNLOADED SUCCESSFULLY")
    driver.quit()
    print("Processing...")
    time.sleep(1)
    database.show_data()
    delete_file()
def delete_file():
    os.chdir('/home/sachin/Downloads')
    os.remove('Travel_Times.csv')