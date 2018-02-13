__author__ = 'tom.li'
# -*- coding: utf-8 -*-
import json

from common import operateYaml, appPerformance as ap, operateElement as bo
from common.variable import GetVariable as common
from common import testLog
from common import testLogScreen
from common import reportPhone as rp
from epamBLL import mobileBase as ba
import os
from common import  operateFile
from common import basePickle
from common import baseRandom
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
IS_CRASH = 1 # crash
NO_ELEMENT = 2 # cannnot find element
NORMAL = 0 # normal

class AppCase():

    def __init__(self, **kwargs):
        '''

        :param kwargs:
        test_module:'module anme'
        GetAppCaseInfo: 'test introduce'
        GetAppCase: 'app case'
        fps: []
        cpu: []
        men: []
        driver:
        package： package name
        devices: device name
        '''
        self.test_module = kwargs["test_module"]
        self.GetAppCaseInfo = kwargs["GetAppCaseInfo"]
        self.GetAppCase = kwargs["GetAppCase"]
        self.fps = kwargs["fps"]
        self.cpu = kwargs["cpu"]
        self.men = kwargs["men"]
        self.driver = kwargs["driver"]
        print("driver_1")
        print(self.driver)
        self.package = kwargs["package"]
        self.devices = kwargs["devices"]
    def get_phone_name(self):
        get_phone = ba.get_phone_info(devices=self.devices)
        phone_name = get_phone["brand"] + "_" +get_phone["model"] + "_"+"android" +"_"+ get_phone["release"]
        return phone_name, get_phone["device"] # device name

    def getModeList(self, f):
        bs = []
        gh = operateYaml.getYam(f)
        for i in range(len(gh)):
            if i == 0:
                  #test id
                self.GetAppCaseInfo.test_id = gh[i].get("test_id", "false")
                 # test introduce
                self.GetAppCaseInfo.test_intr = gh[i].get("test_intr", "false")
            # bt = self.GetAppCase
            self.GetAppCase.element_info = gh[i].get("element_info", "false")

            self.GetAppCase.log = r"d:/" + self.get_phone_name()[0]

          # operate type
            self.GetAppCase.operate_type = gh[i].get("operate_type", "false")
            # enter data
            self.GetAppCase.name = gh[i].get("name", "false")

            self.GetAppCase.index = gh[i].get("index", "false")

            self.GetAppCase.text = gh[i].get("text", "false") # by_link_text

           # verify
            self.GetAppCase.find_type = gh[i].get("find_type", "false")

            self.GetAppCase.time = gh[i].get("time", 0)

            bs.append(json.loads(json.dumps(self.GetAppCase().to_primitive())))
        return bs

    def execCase(self, f, **kwargs):
        '''

        :param f: test file
        :param kwargs:
        test_name: test name
        is_last: latest test 1, 0
        :return:
        '''
        # logTest = testLog.myLog().getLog()
        bc = self.getModeList(f)
        go = bo.OperateElement(driver=self.driver)
        ch_check = bc[-1]
        _d_report_common = {"test_success": 0, "test_failed": 0, "test_sum": 0} #case run account
        is_crash = NORMAL # 0 no crash，1 crash，2 no crash，just cannot find element
        for k in bc:
            if k["operate_type"] != "false":
                k["devices"] = self.devices
                # _d_report_common["test_sum"] += 1
                _operate = go.operate_element(k)
                if _operate:
                    is_crash = NORMAL
                if len(self.pull_crash_log()) > 0:
                    is_crash = IS_CRASH
                elif _operate == False:
                    is_crash = NO_ELEMENT
        #         get_men = ap.get_men(devices=self.devices, pkg_name=self.package)
        #         get_cpu = ap.top_cpu(devices=self.devices, pkg_name=self.package)
        #         get_fps = ap.get_fps(devices=self.devices, pkg_name=self.package)
        #         # case info collection
        #         self.cpu.append(get_cpu)
        #         self.men.append(get_men)
        #         self.fps.append(get_fps)
        # _d_report_common["test_sum"] += 1
        # self.report(go, ch_check, _d_report_common, kwargs, is_crash=is_crash)


    def report(self,go, ch_check, _d_report_common, kwargs, is_crash):

        self.GetAppCaseInfo.test_men_max = rp.phone_max_use_raw(self.men)  # max memory
        avg_men = ba.get_avg_raw(self.men, self.devices)  # avage memory
        self.GetAppCaseInfo.test_men_avg = avg_men
        self.GetAppCaseInfo.test_cpu_max = rp.phone_avg_max_use_cpu(self.cpu)  # max cpu
        self.GetAppCaseInfo.test_cpu_avg = rp.phone_avg_use_cpu(self.cpu)  # avage cpu
        self.GetAppCaseInfo.test_fps_max = rp.fps_max(self.fps)
        self.GetAppCaseInfo.test_fps_avg = rp.fps_avg(self.fps)

        d_report = {}
        raw = ba.get_men_total(devices=self.devices)
        d_report["phone_name"] = self.get_phone_name()[0]
        d_report["phone_pix"] = ba.get_app_pix(self.devices)
        d_report["phone_cpu"] = ba.get_cpu_kel(self.devices)
        d_report["phone_raw"] = rp.phone_raw(raw / 1024)
        if is_crash == NORMAL: # normal
            if go.findElement(ch_check):
                _d_report_common["test_success"] += 1
                self.GetAppCaseInfo.test_result = "成功"
                self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # run case count
            else:
                _d_report_common["test_failed"] += 1
                test_reason = "found not element"
                self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # run case total amount
                ng_img = testLogScreen.screenshotNG(caseName=kwargs["test_name"], driver=self.driver, resultPath=common.SCREEN_IMG_PATH)
                self.GetAppCaseInfo.test_image = ng_img
                self.GetAppCaseInfo.test_result = "fail"
                self.GetAppCaseInfo.test_reason = test_reason
        elif is_crash == IS_CRASH: #if crash
            _d_report_common["test_failed"] += 1
            self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # case total amount
            ng_img = testLogScreen.screenshotNG(caseName=kwargs["test_name"], driver=self.driver,
                                                resultPath=common.SCREEN_IMG_PATH)
            self.GetAppCaseInfo.test_image = ng_img
            self.GetAppCaseInfo.test_result = "fail"
            self.GetAppCaseInfo.test_reason = "crash"
            self.GetAppCaseInfo.test_log = self.pull_crash_log() #recoder local log
        elif is_crash == NO_ELEMENT: #found not element
            _d_report_common["test_failed"] += 1
            self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # run case total amount
            self.GetAppCaseInfo.test_result = "fail"
            self.GetAppCaseInfo.test_reason = "found fail"

        self.GetAppCaseInfo.test_name = kwargs["test_name"]
        self.GetAppCaseInfo.test_module = self.test_module
        self.GetAppCaseInfo.test_phone_name = self.get_phone_name()[0]

        info_case = json.loads(json.dumps(self.GetAppCaseInfo().to_primitive()))
        self.write_detail(info_case, f=common.REPORT_INFO_PATH, key="info")  # all case
        if kwargs["isLast"] == "1":
            # recoder every case status
            if is_crash == NORMAL: #if no crash
                d_report["phone_avg_use_cpu"] = self.GetAppCaseInfo.test_cpu_avg
                d_report["phone_avg_max_use_cpu"] = self.GetAppCaseInfo.test_cpu_max
                d_report["phone_avg_use_raw"] = self.GetAppCaseInfo.test_men_avg
                d_report["phone_max_use_raw"] = self.GetAppCaseInfo.test_men_max
                d_report["fps_avg"] = self.GetAppCaseInfo.test_fps_avg
                d_report["fps_max"] = self.GetAppCaseInfo.test_fps_max
            else:
                d_report["phone_avg_use_cpu"] = "0"
                d_report["phone_avg_max_use_cpu"] = "0"
                d_report["phone_avg_use_raw"] = "0"
                d_report["phone_max_use_raw"] = "0"
                d_report["fps_avg"] = "0"
                d_report["fps_max"] = "0"
            # step count for case
            self.write_detail(d_report, f=common.REPORT_INIT, key="init")
    def read_detail_report(self, f=""):
       op = operateFile.OperateFile(f, "r")
       return op.read_txt_row()
       
    def write_detail(self, json, f="", key="info"):
        '''

        :param json: save json
        :param f: info,and init position
        :param key:  info and init avlue,REPORT_INFO_PATH->info,REPORT_INIT->init
        key is init,when f value is REPORT_INFO_PATH,here
        :return:
        '''
        _read_json_temp = self.read_detail_report(f)
        _result = {}
        if len(_read_json_temp) > 0:
            _read_json = eval(_read_json_temp)
            _read_json[key].append(json)
            _result = _read_json
        else:
            _result[key] = []
            _result[key].append(json)
        op = operateFile.OperateFile(f, "w")
        op.write_txt(str(_result))
        print(_result)
    # write run case time count
    def write_report_collect(self, json, f=""):
        _read_json_temp = self.read_detail_report(f)
        op = operateFile.OperateFile(f, "w")
        _result = {}
        if len(_read_json_temp) > 0:
            _read_json = eval(_read_json_temp)
            for i in _read_json:
                if i == "test_success" or i == "test_failed" or i == "test_sum":  # run time count
                    _result[i] = int(_read_json[i]) + int(json[i])
                else:
                    _result[i] = _read_json[i]
        if len(_result) > 0:
            op.write_txt(str(_result))
        else:
            op.write_txt(str(json))

    def pull_crash_log(self):
        log = ""
        print("pull_crash_log")
        _read_crash = basePickle.read_pickle(common.CRASH_LOG_PATH)
        if len(_read_crash) > 0:
            for i in range(len(_read_crash)):
                    if _read_crash[i]["devices"] == self.get_phone_name()[1]: 
                        log = _read_crash[i]["log"]
                        rand_log = baseRandom.get_ran_dom()+".log" # random log file
                        push_log = common.APACHE_PATH+rand_log #save to apache path
                        os.system("adb -s "+ self.devices+" pull "+log+" " +push_log)
                        return common.PROTOCOL + common.HOST +"/"+common.APACHE_PATH+rand_log
        return log
