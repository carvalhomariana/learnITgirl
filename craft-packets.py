#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16  21:40:47 2017

@author: mcarvalho

This is a simple code for some functions that you can play around using Scapy.

Source Explanation: https://github.com/secdev/scapy
Documentation of Scapy: http://scapy.readthedocs.io/en/latest/installation.html#windows

On my computer, macOS High Sierra, I was unable to run it on Python Notebook, for instance,
so to start, I ran these line on the terminal as it follows:
    $ sudo python
    $ *insert password*
    $ import scapy
    $ from scapy.all import *

"""


import scapy
from scapy.all import *

# Creating packet
p = IP()

# Showing packet with .show function
p.show()

# Stacking the packets together
p = IP()/TCP()
p.show()

# Moving up the TCP packet
# show() command makes easy to see the changes you are doing on the packets
p.payload.show()

# Changing the TCP port to 444
p.payload.dport=444
p.show()

# Changing the flag to 2
p.payload.flags=2
p.show()
## You will notice the flags will not change, and will remain "S", as it was before. It happens because S
## is the second flag in the bitmask (2^1)

# Now, let's try to change the flags to 18
p.payload.flags=18
p.show()
# You will notice the flags will change to SA

send(p)
