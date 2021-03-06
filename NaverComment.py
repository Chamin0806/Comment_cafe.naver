from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import schedule
from bs4 import BeautifulSoup
import pyautogui as pm

mainUrl = 'https://cafe.naver.com/your_naver_cafe_link'
classUrl = [
    'https://cafe.naver.com/your_naver_cafe_link/1233',
    'https://cafe.naver.com/your_naver_cafe_link/3343',
    'https://cafe.naver.com/your_naver_cafe_link/5623',
    'https://cafe.naver.com/your_naver_cafe_link/2323',
    'https://cafe.naver.com/your_naver_cafe_link/1783',
    '123',
    '123'
]

commentText = [
    "3번 ㅇㅇㅇ 출석입니다.",
    "출석",
    "출석",
    "출석",
    "3번 ㅇㅇㅇ 출석",
    "출석",
    "출석"
]



    
def Login(url,comment):
    driver = webdriver.Chrome('chromedriver')

    driver.get(mainUrl)
    driver.implicitly_wait(3)

    # 로그인 버튼
    login_btn = driver.find_element_by_class_name('gnb_txt')
    login_btn.click()
    time.sleep(1)

    # id, pw 검색
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    driver.implicitly_wait(3)

    # id
    tag_id.click()
    pyperclip.copy('Your ID')
    tag_id.send_keys(Keys.CONTROL, 'v')
    driver.implicitly_wait(3)

    # pw
    tag_pw.click()
    pyperclip.copy('Your PW')
    tag_pw.send_keys(Keys.CONTROL, 'v')
    driver.implicitly_wait(3)

    # 로그인
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(1)

    driver.get(url) #classUrl로 넘어감
    time.sleep(3)


    driver.switch_to.frame('cafe_main')
    commentBox = driver.find_element_by_class_name("comment_inbox_text")
    commentBox.click()
    time.sleep(1)
    pyperclip.copy(comment)
    commentBox.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    comment_btn = driver.find_element_by_class_name("register_box")
    comment_btn.click()
    time.sleep(10)
    driver.close()
    print("출석체크가 완료 되었습니다.")    
    




schedule.every().day.at("08:40").do(Login,classUrl[0],commentText[0]) #1교시
schedule.every().day.at("09:40").do(Login,classUrl[1],commentText[1]) #2교시
schedule.every().day.at("10:40").do(Login,classUrl[2],commentText[2]) #3교시
schedule.every().day.at("11:40").do(Login,classUrl[3],commentText[3]) #4교시
schedule.every().day.at("13:40").do(Login,classUrl[4],commentText[4]) #5교시
schedule.every().day.at("14:40").do(Login,classUrl[5],commentText[5]) #6교시
schedule.every().day.at("15:40").do(Login,classUrl[6],commentText[6]) #7교시

while True:
    schedule.run_pending()
    time.sleep(1)
