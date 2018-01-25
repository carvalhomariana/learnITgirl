#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:07:37 2017

@author: mcarvalho
"""

# This file is part of the project to learn Python, Scapy, and Wireshark
# for Learn IT, Girl.

import scapy
from scapy.all import *
from scapy.all import rdpcap # If you don't want to import all,
                             # simply import rdpcap
from scapy.all import wrpcap


# Wireshark is a tool to analyze network traffic, record traffic, in order to
# identify possible network attacks. Wireshark captures packets and display them
# in a easy way to visualize, and filter them.

# First, let's open Wireshark and record some traffic. Click on the blue icon on
# the right top of the page. Open any website of your preference. Play around.
# I use the CNN website (http://www.cnn.com) to record my own traffic in this website.
# Click on the red square on the top left, and stop the network traffic recording.
# Save the file with a .pcap extension.
# My file name is cnn-test.pcap

# Let's read the pcap file  
pkts_list = rdpcap('/Users/mcarvalho/cnn-test.pcap')

# Let's see how long the file is (how many packets the pcap file has)
print ("The cnn-test.pcap has", len(pkts_list), " packets")

# Let's read one packet from the pcap file
pkts_list[245] # You can pick which packet you like

# Let's display the entire packet with layers
pkts_list[245].show()

# Let's display the IPv6 layer of source and destionation
print ("This is the IPv6 source: ", pkts_list[245]['IPv6'].src)
print ("This is the IPv6 destination: ", pkts_list[245]['IPv6'].dst)
print ("This is the sport", pkts_list[245]['TCP'].sport)

# With scapy, we can also modify the IP:
### pkts_list[245]['IPv6'].src = "10.0.0.2"

# We can also write the modified packets into another pcapfile
## wrpcap("modified.pcap", pkts_list)

#Let's read the pcapfile for an ev




