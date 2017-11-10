import sys
from scapy import *
packet = IP(dst="192.168.1.114")/ICMP()/"Hello, World!"
send(packet)
packet.show()
