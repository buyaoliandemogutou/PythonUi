from selenium import webdriver
from common.log import MyLog

log = MyLog().get_log()
logger = log.get_logger()
def setDriver(name, driverPath):
    try:
        if name.lower() == 'firefox':
            driver = webdriver.Firefox(driverPath)
            driver.maximize_window()
            logger.info('浏览器启动正常')
            return driver
        elif name.lower() == 'chrome':
            driver = webdriver.Chrome(driverPath)
            driver.maximize_window()
            logger.info('浏览器启动正常')
            return driver
        elif name.lower() == 'ie':
            driver = webdriver.Ie(driverPath)
            driver.maximize_window()
            logger.info('浏览器启动正常')
            return driver
        else:
            print('Not found this browser')
            log.info('Not found this browser')
    except Exception as e:
        print('启动浏览器异常')
        log.info('启动浏览器异常')

if __name__ == "__main__":
    name = 'chrome'
    path = '..\driver\chromedriver.exe'
    driver = setDriver(name, path)
    driver.get('https://cs.whdtool.com/web//manager/#/login')
    driver.maximize_window()