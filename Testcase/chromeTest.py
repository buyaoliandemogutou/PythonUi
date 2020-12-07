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
        driverPath = r'.\driver\chromedriver.exe'
        url = 'https://cs.whdtool.com/web//manager/#/login'
        driver = setDriver('chrome', driverPath)
        driver.get(url)
        try:
            user = WebTools().Get_text('class_name')
            user = user.text
            print(user)
            if user == '控制台登录':
                WebTools().Click('xpath', '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/p')
            else:
                WebTools().WebDriverWait(3, 0.5, 'name', 'username')
            WebTools().Input('name', 'username', 'mengdou')
            WebTools().Input('password', 'name', '123456')
            WebTools().Click('xpath', '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[3]/form/div[3]/div/button')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    aitool().login()