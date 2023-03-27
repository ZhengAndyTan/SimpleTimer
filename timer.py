#!/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time    : 3/27/2023 10:42 AM
# @Author  : Zheng Tan
# @Site    : 
# @File    : timer.py
# @Software: PyCharm 
# @Comment : 
# 

# import statements
import datetime
from functools import wraps


# main
class Timer:
    def __init__(self, prcd_name=''):
        self.prcd_name = prcd_name
        self.start_time = None
        self.end_time = None
    
    def __call__(self, func, *args, **kwargs):
        print(self.prcd_name)

        @wraps(func)
        def wrapper(*args, **kwargs):
            self.start()
            func(*args, **kwargs)
            self.end()

        return wrapper

    def start(self, prcd_name=''):
        self.start_time = datetime.datetime.now()
        print('Start time: {}'.format(self.start_time))

    def end(self, prcd_name=''):
        self.end_time = datetime.datetime.now()
        print('End time: {}'.format(self.end_time))
        print('Time used: {}'.format(self.end_time - self.start_time))

    def deco_timer(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.start()
            func(*args, **kwargs)
            self.end()
        return wrapper


# run 
if __name__ == '__main__':
    # call and run the function
    pass
