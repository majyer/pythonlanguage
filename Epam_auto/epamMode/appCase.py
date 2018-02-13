__author__ = 'tom.li'
#-*-coding:utf-8-*-

from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType


class GetAppCase(Model):
    element_info = StringType() # (look for type：name/id/xpah)
    operate_type = StringType() #description,example:xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id
    msg = StringType() # enter content
    find_type = StringType() # operate typr example:press,drag....according common
    time = IntType() # swip operate
    name = StringType()
    index = IntType()
    text = StringType()# enter text
    log = StringType() # logger path ,mobile-name+mobile type本地log

# base information
class GetAppCaseInfo(Model):
    test_id = StringType() # id
    test_intr = StringType() # introduce
    test_name = StringType() # name
    test_result =StringType() # result
    test_reason = StringType() # reason for fail
    test_module = StringType() # test template
    test_men_max = StringType() # max memory
    test_men_avg = StringType() # avage memory
    test_cpu_max = StringType() #max cpu
    test_cpu_avg = StringType() #cpu avage
    test_fps_max = StringType() # max fps
    test_fps_avg = StringType() # fps avage
    # test_devices = StringType()
    test_phone_name = StringType() #device_name_type
    test_image = StringType() # picture
    test_log = StringType() #crash log
