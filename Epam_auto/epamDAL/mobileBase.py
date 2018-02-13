__author__ = 'tom.li'
# -*- coding:utf-8 -*-
import sys
#sys.path.insert(0,"../common")
import os
import re
import math
from math import ceil
import subprocess
from common.variable import GetVariable as common
#from variable import GetVariable as common
# get moild infomation
def get_phone_info(devices):
    cmd = "adb -s "+ devices +" shell cat /system/build.prop "
    # phone_info = os.popen(cmd, mode="r").readlines()
    phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()

    l_list = {}
    release = "ro.build.version.release=" # version
    model = "ro.product.model=" #type
    brand = "ro.product.brand=" # product
    device = "ro.product.device=" # device name
    for line in phone_info:
         for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                l_list["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                l_list["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                l_list["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                l_list["device"] = temp[len(device) :]
                break
    print(l_list)
    return l_list

# get the memory
def get_men_total(devices):
    cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
            break
    return int(men_total)
# get cpu account
def get_cpu_kel(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + " kernel"

# get mobile pixel
def get_app_pix(devices):
    result = os.popen("adb -s " + devices+ " shell wm size", "r")
    return result.readline().split("Physical size:")[1]
# get_phone_info("DU2TAN15AJ049163")
# get_phone_info("MSM8926")
def get_avg_raw(l_men, devices):
    '''
    :param l_men: memory list
    :param devices: device name
    :return:
    '''
    l_men = [math.ceil(((l_men[i])/get_men_total(devices))*1024) for i in range(len(l_men))]  # How much memory is taken each time
    if len(l_men) > 0 :
            return str(math.ceil(sum(l_men)/len(l_men))) + "%"
    return "0%"

# if __name__=="__main__":
#     get_phone_info("emulator-5554")
#     print get_men_total("emulator-5554")
#     print get_cpu_kel("emulator-5554")
#     print get_app_pix("emulator-5554")
    #get_avg_raw("2","emulator-5554")
