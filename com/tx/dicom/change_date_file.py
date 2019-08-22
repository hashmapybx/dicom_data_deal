#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 上午11:34
import os
import datetime

root_path = "/home/tx-eva-data/Desktop/test_data_clean/0007869068"
for h_folder in os.listdir(root_path):
    os.system('touch -m -d %s %s' % ('2018-12-12 '+ datetime.datetime.now().strftime('%H:%M:%s'), os.path.join(root_path, h_folder)))
    for sfile in os.listdir(os.path.join(root_path, h_folder)):
        for tfile in os.listdir(os.path.join(os.path.join(root_path, h_folder), sfile)):
            dcm_file = os.path.join(os.path.join(os.path.join(root_path, h_folder), sfile), tfile)
            os.system('touch -m -d %s %s' % ('2018-12-12 '+ datetime.datetime.now().strftime('%H:%M:%s'), dcm_file))

