__author__ = 'tom.li'
# -*- coding: utf-8 -*-

import yaml
import os
import sys

from epamBLL import mobileBase


# -*- coding:utf-8 -*-
def getYam(homeyaml):
    try:
        with open(homeyaml, 'r') as file:
            x = yaml.load(file)
            print x
            return x
    except:
        print(u"cannot find the home Yaml file")


