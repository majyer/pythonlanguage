__author__ = 'tom.li'
#-*-coding:utf-8-*-

import os
import sys
import yaml
import time
import unittest
import datetime
sys.path.append("..")
from common import operateYaml
from testRunner.runnerBase import TestInterfaceCase
from epamBLL import adbCommon
from common import myserver
from common.variable import GetVariable as common
from epamBLL import server
from epamBLL import mobileBase
from testCase.monkey import testMonkey
from multiprocessing import Process
from multiprocessing import Pool
import subprocess
from BaseHTTPServer import HTTPServer
from itertools import product
from common import dataToString

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

#print PATH("../devices.yaml")

data = {"init":[], "info":[]}
def get_devices():
    return operateYaml.getYam(PATH("../devices.yaml"))
ga = get_devices()

def Creatsuite():
    testunit = unittest.TestSuite()

    #find the test cases
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)

    #add test cases to test container
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print testunit
    return testunit

def runnerCaseApp(l_devices):
    start_test_time = dataToString.getStrTime(time.localtime(), "%Y-%m-%d %H:%M %p")
    starttime = datetime.datetime.now()
    #print l_devices
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(testMonkey, l_devices=l_devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()

    #get_common_report(start_test_time, endtime, starttime)
    #report()
   
def runnerPool():
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        t = {}
        t["deviceName"] = ga["appium"][i]["devices"]
        t["platformVersion"] = mobileBase.get_phone_info(devices=ga["appium"][i]["devices"])["release"]
        t["platformName"] = ga["appium"][i]["platformName"]
        t["port"] = ga["appium"][i]["port"]
        l_pool.append(t)
        devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # async
    pool.map(runnerCaseApp,devices_Pool,1)
    pool.close()
    pool.join()

def open_web_server():
    web_server = HTTPServer((common.HOST, common.PORT), myserver.myHandler)
    web_server.serve_forever()

# if os.path.exists(tdresult):
#     filename = tdresult + "\\" + now + "_result.html"
#     fp = file(filename, 'wb')
#     #defined test report
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Appium测试报告', description=u'用例详情：')

#     #run test case
#     runner.run(test_case)
#     fp.close()  #close report file
# else:
#     os.mkdir(tdresult)
#     filename = tdresult + "\\" + now + "_result.html"
#     fp = file(filename, 'wb')
#     #define test report
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Appium测试报告', description=u'用例详情：')

#     #run test cases
#     runner.run(test_case)
#     fp.close()  #close report file

if __name__ == '__main__':
	ga = get_devices()
	if adbCommon.attached_devices():
		# p= Process(target=open_web_server,args=())
		# p.start()

		# appium_server = server.AppiumServer(ga)
		# appium_server.start_server()
		# while not appium_server.is_runnnig():
		# 	time.sleep(2)
		runnerPool()
		# appium_server.stop_server()
		#subprocess.Popen("taskkill /F /T /PID "+str(p.pid),shell=True)
		print(u"hello mobile webui automation")
	else:
	    print(u"devices does not exist")