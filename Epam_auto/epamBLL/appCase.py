__author__ = 'tom.li'
# -*- coding: utf-8 -*-
from epamDAL import appCase
class GetAppCase():
    # def __init__(self, test_module="", AppCaseInfo="", AppCase="",fps=[], cpu=[], men=[]):
    def __init__(self, **kwargs):
        '''
        :param kwargs:
        test_module:'module name'
        GetAppCaseInfo: 'test name' model lawyer
        GetAppCase: 'app case' model layer
        fps: []
        cpu: []
        men: []
        driver:
        package： package name
        devices: device name
        '''
        self.kwargs= kwargs
        self.be = appCase.AppCase(**self.kwargs)
    def execCase(self, f, **kwargs):
        '''

        :param f: test file
        :param kwargs:
        test_name: test name
        is_last: last test 1, 0
        :return:
        '''
        self.be.execCase(f, **kwargs)

