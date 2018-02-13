__author__ = 'tom.li'
# -*- coding:utf-8 -*-
from epamDAL import mobileBase
def get_avg_raw(l_men, deviceName):
    return mobileBase.get_avg_raw(l_men, deviceName)

def get_men_total(devices=""):
    return mobileBase.get_men_total(devices)

def get_app_pix(devices):
    return mobileBase.get_app_pix(devices)

def get_phone_info(devices=""):
    return mobileBase.get_phone_info(devices)

def get_cpu_kel(devices=""):
    return mobileBase.get_cpu_kel(devices)
