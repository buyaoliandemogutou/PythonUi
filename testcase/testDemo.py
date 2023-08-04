import requests
import unittest
import common.HTMLTestRunner1 as HTMLTestRunner
import os
import time
from common.log import MyLog

nowTime = time.strftime("%Y-%m-%d", time.localtime())
path = os.path.join('../result', nowTime+'.html')
logger = MyLog().get_log().get_logger()
class unitDemo(unittest.TestCase):
    def tearDown(self):
        print('每个测试用例执行之后')
        logger.info('每个测试用例执行之后')
    def setUp(self):
        print('每个测试用例执行之前')
        logger.info('每个测试用例执行之前')

    @classmethod
    def setUpClass(self):
        print('必须使用 @ classmethod装饰器, 所有test运行完后运行一次')
        logger.info('必须使用 @ classmethod装饰器, 所有test运行完后运行一次')

    @classmethod
    def tearDownClass(self):
        print('必须使用@classmethod 装饰器,所有test运行前运行一次')
        logger.info('必须使用@classmethod 装饰器,所有test运行前运行一次')

    def test_a_run(self):
        #self.assertEqual(1,1)
        # param = {'type': 'yuantong', 'postid': '806063787827863801'}
        # result= RunMain().run_main('post','http://www.kuaidi100.com/query', param )
        # res=RunMain().getValue(result,'message')
        # value= self.assertEqual('ok', str(res))
        # print(res,'结果：',value)
        print('test_a_run')
        logger.info('test_a_run')

    def test_b_run(self):
        print('test_b_run')
        logger.info('test_b_run')
        # param = {'tel': '18109045175'}
        # result = RunMain().run_main('get', 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm', param)
        # #result=self.getRequests('https://tcc.taobao.com/cc/json/mobile_tel_segment.htm', param)
        # print(result.text)
        # if result.status_code == 200:
        #     self.assertIn("province:'四川'", result.text)
        # else:
        #     print( '请求失败，响应码：',result.status_code)

#cls=readExcel().get_xls('userCase.xlsx', 'login')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unitDemo('test_a_run'))
    suite.addTest(unitDemo('test_b_run'))
    # runner = unittest.TestRunner()
    print('测试地址：'+path)
    try:
        fp = open('../result/1.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='web测试报告', tester='ZhaoJun')
        runner.run(suite)
    except Exception as e:
        print(format(e))
    fp.close()
    # unittest.main()
