import os
import configparser

class ReadConfig():
    def set_config(self, config_path):
        try:
            # config_path = '..\TestFile\config.ini'
            config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
            config.read(config_path, encoding='utf-8')
            return config
        except Exception as e:
            print(e)

    def get_http(self, name, config_path):
        try:
            config = ReadConfig().set_config(config_path)
            value = config.get('HTTP', name)
            return value
        except Exception as e:
            print(e)

    def get_email(self, name, config_path):
        try:
            config = ReadConfig().set_config(config_path)
            value = config.get('EMAIL', name)
            return value
        except Exception as e:
            print(e)

    def get_iniemail(self, name):
        try:
            config = ReadConfig().set_config('../TestFile/config.ini')
            value = config.get('EMAIL', name)
            return value
        except Exception as e:
            print(e)

    def get_mysql(self, name, config_path):
        try:
            config = ReadConfig().set_config(config_path)
            value = config.get('DATABASE', name)
            return value
        except Exception as e:
            print(e)

    def get_userData(self, token, config_path):
        try:
            config = ReadConfig().set_config(config_path)
            token = config.get('USER', token)
            return token
        except Exception as e:
            print(e)

    def set_value(self, option, value, config_path):
        try:
            config = ReadConfig().set_config(config_path)
            config.set('USER', option, value)
            config.write(open(config_path, "w"))
        except Exception as e:
            print(e)

if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl', '../TestFile/config.ini'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off', '../TestFile/config.ini'))
    ReadConfig().set_value('test', '222', '../TestFile/config.ini')
    print(ReadConfig().get_userData('token', '../TestFile/config.ini'))
    # print(config.items('USER'), config.options('USER'))

