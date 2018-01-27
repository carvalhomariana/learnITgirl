#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:18:47 2017

@author: mcarvalho

In order to connect a client and a server, the TCP protocol uses a method called
"3-hand shake", where the client sends a SYN to the target server, and receive
a SYN-ACK in return. Then, the client send a ACK, and the connection is
established between client and server.

You need to look into the the TCP protocols to determine if a SYN attack is occurring.

A SYN Flood attack is when a intruder sends a succession of SYN requests
to a specific system, trying to get its servers in a network congestion,
rendering ineffective its normal network traffic.

You should create your pcap file, in order to analyze its packets.

You will find an example of a pcap file that has an SYN Flood attack: synflood.pcap.
You will find two more examples of a pcap file that don't contain any attack:
jsu.pcap and dailymail.pcap. You can use both of them to compare.

"""

# Import libraries
import sys
import scapy
from scapy.all import *

# Analyze the TCP Protocols.
# It will be suspicius and possibly a SYN Flood attack
# when you see many sent TCP requests from the client, and none response from the
# destination, it is probably a SYN Flood attack.

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

# Run your code typing:
    # python detectSYNattack.py filename.py
    
def Main(filename):
    syn = detectSYN(filename)

if __name__== "__main__":

    if len(sys.argv) < 2:
        print 'Please provide file name'
    else:
        filename = sys.argv[1]
        Main(filename)
