from selenium import webdriver
import pandas as pd
import web
import time
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
driver = webdriver.Chrome()
driver.get(web.page)
time.sleep(5)
timeout=20
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
time.sleep(3)
travel_time=driver.find_elements_by_xpath("//span")
print("Average time : ")
min_val=travel_time[0].text
print(min_val)
sec_val=travel_time[2].text
print(sec_val)
time.sleep(2)
data=driver.find_element_by_xpath("//button[@class='ce ae b5 ag bz az ay bc an ep eq er es et d9 eu ev cr cs b4 ew ex ey ez f0 f1 f2 f3 f4 f5 f6 f7 cc c9 ca cb d0 eo cf f8 f9 fa']")
data.click()
time.sleep(3)
downloadbtn=driver.find_elements_by_xpath("//button[@class='btn btn--link hard--left push-tiny--right']")
downloadbtn[0].click()
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
purpose=driver.find_element_by_xpath("//div[@class='bj cz d0 d1 d2 c2 d3 ch d4 d5 d6 cx d7 bw']")
purpose.click()
purpose=driver.find_element_by_xpath("//div[@id='bui-12']")
time.sleep(1)
purpose.click()
time.sleep(1)
change=driver.find_element_by_xpath("//button[@type='submit']")
change.click()

time.sleep(3)
driver.quit()
print("DATA IS DOWNLOADED SUCCESSFULLY")
time.sleep(1)
print("Processing...")
time.sleep(3)










#invisible=ce ae af bn ah az ay bc an hr hs ht hu et d9 eu ev cr cs b4 ew ex ey ez f0 f1 f2 cc c9 ca cb hb kl

#visible=ce ae af bn ah az ay bc an hr hs ht hu et d9 eu ev cr cs b4 ew ex ey ez f0 f1 f2 kr hb f5 f6 f7 cc c9 ca cb