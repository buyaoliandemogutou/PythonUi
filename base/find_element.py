from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common.log import MyLog

logger = MyLog().get_log().get_logger()


class WebTools:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()


    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退
    def back(self):
        self.driver.back()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 切换窗口
    def current_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    # 输入
    def input(self, type, value, inputvalue):
        try:
            if type != '' and value != '' and inputvalue != '':
                self.find_element(type, value).send_keys(inputvalue)
            elif type == '' or value == '' or inputvalue == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：' + type + value + inputvalue)
        except Exception as e:
            print('输入失败' + format(e))
            logger.info('输入失败' + format(e))

    # 点击
    def click(self, type, value):
        try:
            if type != '' and value != '':
                self.find_element(type, value).click()
            elif type == '' or value == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：' + type + value)
        except Exception as e:
            print('输入失败' + format(e))
            logger.info('输入失败' + format(e))

    # 点击
    def clear(self, type, value):
        try:
            if type != '' and value != '':
                self.find_element(type, value).clear()
            elif type == '' or value == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：' + type + value)
        except Exception as e:
            print('输入失败' + format(e))
            logger.info('输入失败' + format(e))

    # 获取输入框的值
    def get_attribute(self, type, value):
        value1 = self.find_element(type, value).get_attribute()
        return value1

    # 获取元素的值
    def get_text(self, type, value):
        value1 = self.find_element(type, value).text
        return value1

    # 显性等待
    def web_driver_wait(self, MaxTime, Mintime, type, value):
        # element = self.find_element(type, value)
        WebDriverWait(self.driver, MaxTime, Mintime).until(EC.visibility_of_element_located((type, value)))

    # 鼠标移动点击机制
    def move_action(self, type, value):
        try:
            to = self.find_element(type, value)
            webdriver.ActionChains(self.driver).click(to).perform()
        except Exception as e:
            print('鼠标移动失败' + format(e))
            logger.info('鼠标移动失败' + format(e))

    # 查找元素
    def find_element(self, type, path):
        try:
            if type.lower() == 'xpath':
                element = self.driver.find_element(By.XPATH, path)
            elif type.lower() == 'id':
                element = self.driver.find_element(By.ID, path)
            elif type.lower() == 'class_name':
                element = self.driver.find_element(By.CLASS_NAME, path)
            elif type.lower() == 'name':
                element = self.driver.find_element(By.NAME, path)
            elif type.lower() == 'tag_name':
                element = self.driver.find_element(By.TAG_NAME, path)
            elif type.lower() == 'link_text':
                element = self.driver.find_element(By.LINK_TEXT, path)
            elif type.lower() == '':
                print('输入的值为空')
                logger.info('输入的值为空')
            return element
        except Exception as e:
            print('输入值不正确：' + format(e))
            logger.info('输入值不正确：' + format(e))

    # 层级查找元素
    def get_level_element(self, by, ele, ch_by, ch_ele):
        element = self.find_element(by, ele)

        ch_element = None
        try:
            if ch_by == 'id':
                ch_element = element.find_element(By.ID, ch_ele)
            elif ch_by == 'name':
                ch_element = element.find_element(By.NAME, ch_ele)
            elif ch_by == 'css':
                ch_element = element.find_element(By.CSS_SELECTOR, ch_ele)
            elif ch_by == 'class':
                ch_element = element.find_element(By.CLASS_NAME, ch_ele)
            else:
                ch_element = element.find_element(By.XPATH, ch_ele)
        except Exception as e:
            print('输入值不正确：' + format(e))
            logger.info('输入值不正确：' + format(e))
        return ch_element
