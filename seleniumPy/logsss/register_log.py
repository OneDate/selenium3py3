#!/user/bin/env python
#-*- coding:utf-8 -*-

import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger =logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #输出到控制台
        # str_handle = logging.StreamHandler()
        # logger.addHandler(str_handle)
        # logger.debug('info')


        #按照当前时间创建log文件
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name = log_dir+'/'+log_file
        print(log_name)


        #输出到文件
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s---> %(funcName)s %(levelno)s: %(levelname)s -----%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        #关闭


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler ( self.file_handle )
        self.file_handle.close ()


if __name__ == '__main__':
    r = UserLog()

    l = r.get_log()

    l.debug('asdada')

    r.close_handle()