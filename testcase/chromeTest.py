import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.setDriver import setDriver
from common import log
from base.find_element import WebTools

log = log.Logger().get_logger()


class aitool():
    def login(self):
        # driverPath = r'.\Driver\chromedriver.exe'
        # driver = setDriver('chrome', driverPath)
        url = 'https://jqdev.jqsoft.vip/#/login'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div/div/input')))
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
            element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div/input')
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div/input')))
            element.send_keys('123')
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div/label/span[1]/span')))
            driver.find_element(By.XPATH,
                                '//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div/label/span[1]/span').click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[3]/div/button')))
            driver.find_element(By.XPATH,
                                '//*[@id="app"]/div/div[2]/div[2]/form/div[3]/div/button').click()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    aitool().login()
