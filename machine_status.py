#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

check_disk = check_disk_usage('/')
check_cpu = check_cpu_usage()

if not check_disk or not check_cpu:
    print('ERROR!')
    if not check_disk:
        print('- Free space lower than 20%')
    elif not check_cpu:
        print('- CPU usage above 75%')
else:
    print('Everything is OK!')