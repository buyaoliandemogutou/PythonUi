import time

from selenium import webdriver
from Common.log import MyLog
logger = MyLog().get_log().get_logger()
class test:
    def setDriver(self):
        try:
            driverPath = '..\Driver\chromedriver.exe'
            driver = webdriver.Chrome(driverPath)
            driver.get('https://jqdev.jqsoft.vip/#/login')
            time.sleep(1000)
            logger.info('成功打开地址')
            driver.maximize_window()
        except Exception as e:
            print(e)
            logger.info(e)

if __name__ == '__main__':
    test().setDriver()


