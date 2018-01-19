#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:18:47 2017

@author: mcarvalho
"""

import sys
import scapy
from scapy.all import *

def detectSYN(filename):
    pkts_list = rdpcap(filename)
    syn = 0
    
    for p in pkts_list:
        if "TCP" not in p:
            continue
        if p["TCP"].flags == 2L:
            syn += 1
        
    print '# of Packets in this pcapfile: ', len(pkts_list)
    print 'TCP packets: ', syn

def Main(filename):
    syn = detectSYN(filename)

if __name__== "__main__":

    if len(sys.argv) < 2:
        print 'Please provide file name'
    else:
        filename = sys.argv[1]
        Main(filename)
