__author__ = 'tom.li'
# -*- coding:utf-8 -*-
from epamDAL import server

# control appium server
class AppiumServer():
    def __init__(self, l_devices):
        self.server = server.AppiumServer(l_devices)
    def start_server(self):
        self.server.start_server()
    def stop_server(self):
        self.server.stop_server()
    def is_runnnig(self):
        return self.server.is_runnnig()