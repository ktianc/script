#!/usr/bin/python
#coding=utf-8

import os
import sys
import time



def backup(sql,name_dir):
    backup_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    os.chdir("/usr/local/backups/")
    os.system("mysqldump {0} > {0}-{1}.sql".format(sql,backup_time))
    os.system("scp -r -i /usr/local/backups/id_rsa {0}-{1}.sql root@47.104.86.129:/usr/local/nginx/html/backups/{2}/".format(sql,backup_time,name_dir))
    os.system("rm -rf {0}-{1}.sql".format(sql,backup_time))


while True:
    time.sleep(172800)
    while True:
        if time.strftime("%H",time.localtime(time.time())) == "00":
            backup("hanyuan","hanyuan")
            backup("lbdz","hnlbdz")
            backup("miniprogram_food","xiaochengxu")
            backup("lbwsql","langbowang")
            break
        else:
            time.sleep(3600)
