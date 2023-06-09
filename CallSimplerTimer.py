#!/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time    : 3/27/2023 1:50 PM
# @Author  : Zheng Tan
# @Site    : 
# @File    : CallSimplerTimer.py
# @Software: PyCharm 
# @Comment : 
# 

# import statements
import time
import datetime
from timer import Timer as timer


# main
@timer('Anything you would like to say')
def any_function(a: int = 1,
                 b: int = 2,
                 c: str = 'abaaba'):
    print('I am a function')
    print(c, '=', a + b)
    time.sleep(5)


# run 
if __name__ == '__main__':
    # call and run the function
    any_function()

'''
Expected Output:
Anything you would like to say
Start time: 2023-03-27 14:06:17.884332
I am a function
abaaba = 3
End time: 2023-03-27 14:06:22.891991
Time used: 0:00:05.007659
'''
