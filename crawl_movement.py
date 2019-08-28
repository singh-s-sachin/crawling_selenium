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
    #cookiebtn=driver.find_element_by_xpath("//div[@class='close-cookie']")
    #cookiebtn.click()
    time.sleep(2)
    btn=driver.find_element_by_xpath("//a[@class='dq b9 ai cs dr ds dt du dv dw dx dy dz e0 e1']")
    btn.click()
    time.sleep(15)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(2)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(2)
    change=driver.find_element_by_xpath("//button[@class='btn btn--primary']")
    change.click()
    time.sleep(5)
    #zone=driver.find_elements_by_xpath("//div[@class='as eu at bj ff cl']")
    #zone[2].click()
    zone=driver.find_elements_by_xpath("//span[@class='ff cl ft fu fv ai ao fw fg gl fx gm br']")
    zone=zone[1].text
    zone.replace()
    if zone[-1]=='s':
        zone=zone[:-1]
    print(zone)
    downloadbtn=driver.find_element_by_xpath("//button[@class='d9 ao b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd be bf bg as da at db hi hj hk hl dg dh di dj dk hm bu bv bw ca hh ci hn ho hp']")
    downloadbtn.click()
    time.sleep(3)
    change=driver.find_elements_by_xpath("//li[@class='tabs__item']")
    change[1].click()
    table=driver.find_elements_by_xpath("//table[@class='table table--striped table--small flush--bottom']/tbody/tr/td")
    if len(table)!=0:
        print(len(table))
        change=table[0].find_element_by_xpath("//a/small")
        change.click()
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
        purpose=driver.find_element_by_xpath("//div[@class='er an ca ag ah dp cs fg g1 g2 gl fx gm br']")
        purpose.click()
        purpose=driver.find_elements_by_xpath("//div[@class='bt de dc dd df d2 cl']/div/ul/li")
        purpose[0].click()
        change=driver.find_element_by_xpath("//button[@type='submit']")
        change.click()
        #close_button=driver.find_element_by_xpath("//button[@aria-label='Close']")
        #close_button.click()
        file=str(location)+"-"+zone.lower()+"-2019-1-All-HourlyAggregate.csv"
        file1=str(location)+"-"+zone.lower()+"s-2019-1-All-HourlyAggregate.csv"
        print("Downloading")
        #time.sleep(30)
        download_wait(file,file1)
        print("DATA IS DOWNLOADED SUCCESSFULLY")
        driver.quit()
        print("Processing...")
        
        database.show_data(file,file1,location)
    else:
        driver.quit()
    delete_file(file,file1)
def delete_file(file,file1):
    os.chdir('/home/sachin/Downloads')
    if os.path.exists(file):
        os.remove(file)
    else:
        os.remove(file1)
def download_wait(file,file1):
    file_path="/home/sachin/Downloads/"+file
    file_path1="/home/sachin/Downloads/"+file1
    print(file_path, file_path1)
    while not os.path.exists(file_path) and not os.path.exists(file_path1):
        time.sleep(1)