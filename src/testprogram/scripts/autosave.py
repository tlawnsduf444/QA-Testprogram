#!/usr/bin/env python
import os
import tarfile
import shutil

filenames = os.listdir("/home/yujin/.ros/log")
lognames = list()
deliverynames = os.listdir("/home/yujin/qa_file/delivery_file")
posenames = os.listdir("/home/yujin/qa_file/pose_file")
for i in range(len(filenames)):
    if filenames[i][:4] == '2018':
        if filenames[i][-1].isdigit() == True: 
            lognames.append(filenames[i])
lognames = sorted(lognames)
deliverynames = sorted(deliverynames)
posenames = sorted(posenames)
try:
    os.mkdir("/home/yujin/" + lognames[-1])
except: 
    pass

with tarfile.open("/home/yujin/" + lognames[-1] + '/' +lognames[-1] + '.tar.gz', mode='w:gz') as tar:
    tar.add("/home/yujin/.ros/log/" + lognames[-1], arcname=lognames[-1])
shutil.copy("/home/yujin/.ros/log/console_output.log", "/home/yujin/" + lognames[-1] + "/" + lognames[-1] + "_console_output" + ".log")
shutil.copy("/home/yujin/qa_file/delivery_file/" + deliverynames[-1], "/home/yujin/" + lognames[-1] + "/" + deliverynames[-1])
shutil.copy("/home/yujin/qa_file/pose_file/" + posenames[-1], "/home/yujin/" + lognames[-1] + "/" + posenames[-1])