#!/usr/bin/env python

"""
python3 arp_ip.py -m "mac addr" -n "net segment"
用于根据已知的MAC地址获取设备IP
"""

import os
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='depends on mac to get ip')
parser.add_argument('-m', '--mac_addr', help='Mac addr')
parser.add_argument('-n', '--net_segment', help='Net segment')

args = parser.parse_args()
mac_addr = args.mac_addr
net_segment = args.net_segment

def mac_to_ip():
    s = subprocess.Popen("arp -n", shell=True, stdout=subprocess.PIPE)
    status, err = s.communicate()
    status = str(status, encoding='utf-8')
    for arp_status in status.splitlines()[1:-1]:
        if mac_addr in arp_status:
            print(arp_status)
            exit(0)

if __name__ == '__main__':

    for num in range(1, 255):
        ip = net_segment + str(num)
        subprocess.Popen("ping {} -c 1 >> /dev/null".format(ip), shell=True)
        mac_to_ip()
