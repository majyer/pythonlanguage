__author__ = "tom.li"
# -*- coding:utf-8 -*-
import subprocess
import re, os
import math
# Common performance monitoring

def top_cpu(devices, pkg_name):
    cmd = "adb -s "+devices+" shell dumpsys cpuinfo | grep -w " + pkg_name+":"
    get_cmd = os.popen(cmd).readlines()
    for info in get_cmd:
        print info
        return float(info.split()[2].split("%")[0])



# get memory usage
def get_men(devices, pkg_name):
    cmd = "adb -s "+devices+" shell  dumpsys  meminfo %s"  %(pkg_name)
    total = "TOTAL"
    get_cmd = os.popen(cmd).readlines()
    for info in get_cmd:
        info_sp = info.strip().split()
        for item in range(len(info_sp)):
            if info_sp[item] == total:
               return int(info_sp[item+1])
    return 0

# get fps
def get_fps(devices, pkg_name):
    print("fps-")
    _adb = "adb -s "+devices+" shell dumpsys gfxinfo %s | grep -A 128 'Execute'  | grep -v '[a-Z]' "%pkg_name
    result = os.popen(_adb).read().strip()
    result = result.split('\r\n')
    # r_result = [] # 总值
    # t_result = [] # draw,Process,Execute分别的值
    # f_sum = 0
    for i in result:
        l_result = i.split('\t')[-3:]
        f_sum = 0
        for j in l_result:
            r = re.search(r"\d+\.\d+", str(j))
            if r:
                f_sum += float(r.group())
            # t_result.append('%.2f'%f_sum)
        return float('%.2f'%f_sum)
    # print(r_result)
    # print(t_result)
# get_phone_info("MSM8926")

# After taking the flow, you can use the flow after the step to reduce the flow before the step and get the flow of the flow. You can also use the time difference to calculate!
# def getFlow(pid="31586"):
#     flow_info = os.popen("adb shell cat /proc/"+pid+"/net/dev").readlines()
#     t = []
#     for info in flow_info:
#         temp_list = info.split()
#         t.append(temp_list)
#     flow[0].append(ceil(int(t[6][1])/1024)) # 下载
#     flow[1].append(ceil(int(t[6][9])/1024)) # 发送
#     return flow
def read_report(f=""):
    from common.operateFile import OperateFile
    op = OperateFile(f, "r")
    return op.read_txt_row()
if __name__ == '__main__':
    print(top_cpu(devices="DU2TAN15AJ049163",pkg_name="cn.ibona.t1_beta"))
    pass