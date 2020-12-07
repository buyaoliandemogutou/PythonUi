from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Common.log import MyLog

logger = MyLog().get_log().get_logger()
class WebTools(object):
    def __init__(self, driver:webdriver.Remote = None):
        self.driver = driver

    #浏览器前进操作
    def forward(self):
        self.driver.forward()

    #浏览器后退
    def back(self):
        self.driver.back()
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    #切换窗口
    def Current_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    #输入
    def Input(self, type, value, inputvalue):
        try:
            if type != '' and value != '' and inputvalue != '':
                WebTools.Element(type, value).send_keys(inputvalue)
            elif type == '' or value == '' or inputvalue == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：'+type+value+inputvalue)
        except Exception as e:
            print('输入失败'+format(e))
            logger.info('输入失败'+format(e))

    #点击
    def Click(self, type, value):
        try:
            if type != '' and value != '':
                WebTools.Element(type, value).click()
            elif type == '' or value == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：'+type+value)
        except Exception as e:
            print('输入失败'+format(e))
            logger.info('输入失败'+format(e))

    # 点击
    def Clear(self, type, value):
        try:
            if type != '' and value != '':
                WebTools.Element(type, value).clear()
            elif type == '' or value == '':
                print('输入的值不能为空')
                logger.info('输入的值不能为空：' + type + value)
        except Exception as e:
            print('输入失败' + format(e))
            logger.info('输入失败' + format(e))

    #获取输入框的值
    def Get_attribute(self, type, value):
        value1 = WebTools.Element(type, value).get_attribute()
        return value1

    # 获取元素的值
    def Get_text(self, type, value):
        value1 = WebTools.Element(type, value).text
        return value1

    #显性等待
    def WebDriverWait(self, MaxTime, Mintime, type, value):
        element = WebTools.Element(type, value)
        WebDriverWait(self.driver, MaxTime, Mintime).until(EC.presence_of_all_elements_located(element))

    #鼠标移动点击机制
    def Move_action(self, type, value):
        try:
            to = WebTools.Element(type, value)
            webdriver.ActionChains(self.driver).click(to).perform()
        except Exception as e:
            print('鼠标移动失败'+format(e))
            logger.info('鼠标移动失败'+format(e))
    
    #查找元素
    def Element(self, type, path):
        try:
            if type.lower() == 'xpath':
                element = self.driver.find_element_by_xpath(path)
                return element
            elif type.lower() == 'class_name':
                element = self.driver.find_element_by_class_name(path)
                return element
            elif type.lower() == 'id':
                element = self.driver.find_element_by_id(path)
                return element
            elif type.lower() == 'name':
                element = self.driver.find_element_by_name(path)
                return element
            elif type.lower() == 'tag_name':
                element = self.driver.find_element_by_tag_name(path)
                return element
            elif type.lower() == 'link_text':
                element = self.driver.find_element_by_link_text(path)
                return element
            elif type.lower() == '':
                print('输入的值为空')
                logger.info('输入的值为空')
        except Exception as e:
            print('输入值不正确：'+format(e))
            logger.info('输入值不正确：'+format(e))
