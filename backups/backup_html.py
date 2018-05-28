#!/usr/bin/python
#coding=utf-8

import os
import sys
import time

def backup(name_html,dir_name):
    backup_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) #time
    os.chdir("/var/www/html/")
    os.system("zip -r {0}-{1}.zip {0}".format(name_html,backup_time)) #compress
    os.system("scp -r -i /usr/local/backups/id_rsa {0}-{1}.zip root@47.104.86.129:/usr/local/nginx/html/backups/{2}/".format(name_html,backup_time,dir_name))# upload
    os.system("rm -rf {0}-{1}.zip".format(name_html,backup_time)) #Delete compressed package


def backup_lbw(name_html,dir_name):
    backup_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) #time
    os.chdir("/var/www/html/container_one/")
    os.system("zip -r {0}-{1}.zip {0}".format(name_html,backup_time)) #compress
    os.system("scp -r -i /usr/local/backups/id_rsa {0}-{1}.zip root@47.104.86.129:/usr/local/nginx/html/backups/{2}/".format(name_html,backup_time,dir_name))# upload
    os.system("rm -rf {0}-{1}.zip".format(name_html,backup_time)) #Delete compressed package


while True:
	time.sleep(172800) #Pause a day,one day
	while True:
        if time.strftime("%H",time.localtime(time.time())) == "01": #for 02:00 start
            backup("xiaochengxu","xiaochengxu")
            backup_lbw("lbwcs","langbowang")
            break
        else:
            time.sleep(3600) #one hour
 