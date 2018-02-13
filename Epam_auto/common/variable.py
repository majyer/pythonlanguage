__author__ = "tom.li"
# -*- coding:utf-8 -*-

# the way for finding elements
class GetVariable(object):
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    APPIUM = "appium"
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"

    CLICK = "click"
    DRIVER = ""
    TAP = "tap"
    SWIPELEFT = "swipeLeft"

    SELENIUM_APPIUM = "appium"

    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"
    WAIT_TIME = 5

    #selenium
    SEND_CODE = "send_code" # enter verify code

    #The path to record all the cases locally
    REPORT_INFO_PATH = "/root/report/info.txt"
    REPORT_INIT = "/root/report/init.txt"
    REPORT_COLLECT_PATH = "/root/report/collect.txt"
    CRASH_LOG_PATH = "/root/report/crash.txt" # save crash file name
    #my server
    HOST = '127.0.0.1'
    PORT = 8088

    PROTOCOL = "http://" #proxy
    APACHE_PATH = "/root/Apache2/htdocs/appium/log/" #apapche server logger

    SCREEN_IMG_PATH = "/root/Apache2/htdocs/appium/img/" # screenshot address



