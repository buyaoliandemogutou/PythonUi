from selenium import webdriver
from common.log import MyLog


class InitDriver:
    def __init__(self, browser: str):
        self.logger = MyLog().get_log().get_logger()
        if browser.lower() == 'chrome':
            self.driver = webdriver.chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.firefox()
        elif browser.lower() == 'ie':
            self.driver = webdriver.Ie()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        else:
            self.logger.error('不支持的浏览器类型:{}'.format(browser))
            raise Exception('不支持的浏览器类型:{}'.format(browser))
            # 浏览器最大化
        self.driver.maximize_window()
        # 隐式等待-一般写10即可
        self.driver.implicitly_wait(20)
