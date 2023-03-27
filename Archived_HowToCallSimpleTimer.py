#!/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time    : 3/27/2023 11:06 AM
# @Author  : Zheng Tan
# @Site    : 
# @File    : Archived_HowToCallSimpleTimer.py
# @Software: PyCharm 
# @Comment : 
# 

# import statements
import time
from Archived_timer import Timer
deco_timer = Timer().deco_timer


# main
@deco_timer
def any_function(a: int = 1,
                 b: int = 2,
                 c: str = 'abaaba'):
    print('I am a function')
    time.sleep(5)


# run
if __name__ == '__main__':
    # call and run the function
    any_function()
