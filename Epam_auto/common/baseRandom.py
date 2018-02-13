__author__ = "tom.li"
# -*- coding:utf-8 -*-
import datetime
import random
#use date to create random
def get_ran_dom():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    randomNum = random.randint(0, 100)
    if randomNum <= 10:
        randomNum = str(0)+str(randomNum)
    uniqueNum = str(nowTime)+str(randomNum)
    return  uniqueNum