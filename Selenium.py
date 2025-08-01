from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class browserManage:
    def __init__(self):
        try:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)
        except Exception as e:
            print(f'The exception caught is {e}')
            self.driver=None
    
    def open_url(self,url):
        if self.driver:
            try:
                self.driver.get(url)
                print(f'Opened {url}')
            except Exception as e:
                print(f'Error in opening {e}')
    
    def close_url(self):
        if self.driver:
            time.sleep(10)
            self.driver.quit()
            print("Browser closed")

class WebElementHelper:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def find_element(self,by,value):
        try:
            return self.wait.until(EC.presence_of_element_located((by,value)))
        except Exception as e:
            print(e)
            return None
        
    def enter_text(self,by,value,text):
        try:
            ele=self.find_element(by,value)
            if ele:
                ele.clear()
                ele.send_keys(text)
                print("Text entered")
        except:
            print("Failed to enter")

    def click_ele(self,by,value):
        try:
            ele=self.wait.until(EC.element_to_be_clickable(by,value))
            ele.click()
            print("Element clicked")
        except:
            print("Not clicked")
    
    def get_text(self,by,value):
        try:
            ele=self.find_element(by,value)
            if ele:
                print(f'Text from element {ele}')
                return ele.text
        except:
            print("Failed to get text")
            return ""
    
    def is_visible(self,by,value):
        try:
            self.wait.until(EC.visibility_of_element_located(by,value))
            print('Element is visible')
            return True
        except:
            print("Element is not visible")
            return False

browser=browserManage()
browser.open_url(" https://www.google.com")

helper=WebElementHelper(browser.driver)
helper.is_visible(By.NAME,"q")
helper.enter_text(By.NAME,"q","Netflix")

time.sleep(5)

helper.click_ele(By.XPATH, "(//input[@name='btnK'])[1]")

time.sleep(5)

helper.get_text(By.XPATH, "(//h3)[1]")

time.sleep(5)

helper.find_element(By.LINK_TEXT, "Images")

time.sleep(5)

browser.close_url()