from fabric.api import *
import sys


ip_l = []
for i in range(2,101):
    i = str(i)
    a = "192.168.0."+i
    ip_l.append(a)

env.hosts=[ip_l]
env.user=root
env.password=*****
env.port=22


def ssh():
    put("G://authorized_keys","~/.ssh/")

