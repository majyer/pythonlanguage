__author__ = 'tom.li'
# -*- coding:utf-8 -*-
from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType


class GetWebCase(Model):
    element_info = StringType() # (look for type：name/id/xpah)
    operate_type = StringType() #description,example:xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id
    find_type = StringType() # operate type
    name = StringType()
    index = IntType()
    text = StringType()


# test base info
class GetWebInfoCase(Model):
    test_id = StringType()
    test_intr = StringType()
    test_name = StringType()
    test_result =StringType()
    test_reason = StringType()
    test_module = StringType()
