from scapy import *

print(sr(IP(dst="192.168.0.1")/TCP(dport=80)))
