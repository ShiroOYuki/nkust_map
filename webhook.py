import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import base64
import time
from  PIL import Image
import nkust_map.getText as getText
from selenium.webdriver.common.by import By
import os

class login:
    def __init__(self):
        self.url = "https://webap.nkust.edu.tw/nkust"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        self.act = "C111151115"
        self.encPwd = "QmFieTA1MTg="
        # self.act = "C111151125"
        # self.encPwd = "YWFhNzA4NTU="
    
    def run(self):
        # soup = bs(r.content, "lxml") # lxml 是 Python 的其中一個物件樹解析器(速度最快的)
        driver = webdriver.Chrome("./src/chromedriver.exe")
        driver.get(self.url)
        driver.implicitly_wait(10)
        time.sleep(2)
        actInput = driver.find_element("id", "uid")
        pwdInput = driver.find_element("id", "pwd")
        verifyInput = driver.find_element("id", "etxt_code")
        loginBtn = driver.find_element("id", "chk")
        verifyCodeUnderText = driver.find_element(By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[4]/td[3]/strong/small")
        verifyCodeImg = driver.find_element("id", "verifyCode")
        
        # location = verifyCodeImg.location   
        # x = location['x']
        # y = location['y']-13
        location = verifyCodeUnderText.location   
        x = location['x']
        y = location['y']-40
        w = x + 87
        h = y + 40
        time.sleep(2)
        driver.save_screenshot("screenshot.png")
        image = Image.open("screenshot.png")
        image = image.crop((x, y, w, h)).resize((870, 400), Image.ANTIALIAS)
        image = image.convert('L')
        image = image.point(lambda x: 0 if x < 150 else 255, '1')
        image.save("verify.png")
        verifyCode = getText.get()
        print(verifyCode)
        actInput.send_keys(self.act)
        pwdInput.send_keys(self.pwd_decode(self.encPwd))
        time.sleep(3)
        verifyInput.send_keys(verifyCode)
        loginBtn.click()
        time.sleep(2)
        
        # get class
        frame_element = driver.find_element(By.ID, "Lmenu")
        driver.switch_to.frame(frame_element)
        element = driver.find_element(By.XPATH, "/html/body/div/div/div/span/table/tbody/tr[1]/td[2]/table[1]/tbody/tr/td[2]/span")
        element.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH, "/html/body/div/div/div/span/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[1]/td[2]/table[2]/tbody/tr[9]/td[2]/table/tbody/tr/td/div")
        element.click()
        time.sleep(1)
        driver.switch_to.default_content()
        frame_element = driver.find_element(By.XPATH, "/html/frameset/frameset/frame[2]")
        driver.switch_to.frame(frame_element)
        element = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[5]/td/input")
        element.click()
        time.sleep(1)
        
        classes = [self.act]
        time_code = ["M", 1, 2, 3, 4, "A", 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for td in range(2, 9):
            for tr in range(2, 17):
                item = driver.find_element(By.XPATH, f"/html/body/table/tbody/tr[{tr}]/td[{td}]")
                
                if item.text != " ":
                    info = item.text.split("\n")[:3]
                    class_name = info[0]
                    teacher = info[1]
                    addr = info[2]
                    if addr == "":
                        addr = None
                    classes.append({"time": f"{time_code[td-1]}-{time_code[tr-2]}", "name": class_name, "teacher": teacher, "addr": addr})
                else:
                    classes.append({"time": f"{time_code[td-1]}-{time_code[tr-2]}", "name": None, "teacher": None, "addr": None})
        driver.close()
        
        for i in classes:
            print(i)
        os.system("pause")
        return classes
    
    def pwd_decode(self, enc):
        return base64.b64decode(enc).decode("utf-8")
        
if __name__ == '__main__':
    l = login()
    l.run()