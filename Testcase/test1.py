from selenium import webdriver
from Common.log import MyLog
logger = MyLog().get_log().get_logger()
class test:
    def setDriver(self):
        try:
            driver = webdriver.Chrome(r'..\driver\chromedriver.exe')
            driver.get('https://cs.whdtool.com/web//manager/#/login')
            logger.info('成功打开地址')
        except Exception as e:
            logger.info(e)

if __name__ == '__main__':
    test().setDriver()


