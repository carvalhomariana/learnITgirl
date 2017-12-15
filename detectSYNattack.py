#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:18:47 2017

@author: mcarvalho
"""

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
        
    print syn
    print (len(pkts_list))


