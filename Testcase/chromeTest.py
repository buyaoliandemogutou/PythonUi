import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base.setDriver import setDriver
from Common import log
from Base.findElement import WebTools

log = log.Logger().get_logger()


class aitool():
    def login(self):
        # driverPath = r'.\Driver\chromedriver.exe'
        # driver = setDriver('chrome', driverPath)
        url = 'https://jqdev.jqsoft.vip/#/login'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(4)
        try:
            # user = WebTools().Get_text('class_name')
            # user = user.text
            # print(user)
            # if user == '控制台登录':
            #     WebTools().Click('class_name', 'el-input__inner')
            # else:
            #     WebTools().WebDriverWait(3, 0.5, 'name', 'username')
            # WebTools().Input('xpath', '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div/div/input', 'admin')
            # WebTools().Input('xpath', '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div/input', '123')
            # WebTools().Click('xpath', '//*[@id="app"]/div/div[2]/div[2]/form/div[3]/div/button')
            # WebTools().Element('xpath', '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div/div/input').sendkey('admin')
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div/div/input').send_keys(
                'admin')
            WebTools().Input('xpath', '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div/input', '123')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    aitool().login()
