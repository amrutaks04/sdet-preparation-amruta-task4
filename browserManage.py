from selenium import webdriver
import time

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


browser=browserManage()
browser.open_url("https://www.netflix.com")
browser.close_url()