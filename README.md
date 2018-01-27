# Project Learn IT, Girl - 3rd Edition
This project was developed by me, with my mentor orientation, for the program Learn IT, Girl - 3rd Edition.

The objective of this project is to bring attention from girls and boys who are interested in learning more
about network, cybersecurity, and also learn a new programming language - in this case, Python.

The tools used to develop this project were:
1. Python - Programming Language
2. Scapy - Python Library
3. WireShark - open source tool to record and analyze network traffic
4. GitHub

#### To learn how to install Scapy, you can verify:
1. About Scapy: https://github.com/secdev/scapy
2. Documentation: http://scapy.readthedocs.io/en/latest/installation.html#windows

This project was developed for a education purpose, and it is a modification of other source codes,
in order to facilitate the learning for its users. The codes presented on my project Learn IT, Girl
were modifed to adapt the project's needs. The source codes are:
1. https://github.com/AllGloryToTheHypnotoad/Black-Hat-Python/blob/master/BHP-Code/Chapter4/pic_carver.py
2. http://bt3gl.github.io/black-hat-python-infinite-possibilities-with-the-scapy-module.html

#### Some network attacks concepts were learned over the course:
Basic network attacks / How to defend against them

__Port Scan Attack__: when an attacker sends packets to your machine, varying the destination port.
The attacker can use this to find out what services you are running and to get a pretty good idea
of the operating system you have. Most Internet sites get a dozen or more port scans per day –
it is more common than you imagine!

__Denial-of-service attack (DoS attack)__: is a cyber-attack where the perpetrator seeks to make a machine
or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of
a host connected to the Internet. Denial of service is typically accomplished by flooding the targeted machine
or resource with superfluous requests in an attempt to overload systems and prevent some or all legitimate
requests from being fulfilled.
_Countermeasures_: It is very difficult to defend against these types of attacks because the response data is
coming from legitimate servers. These attack requests are also sent through UDP, which does not require a
connection to the server.

__SYN Flood Attack__: A SYN flood is a form of denial-of-service attack in which an attacker sends a succession
of SYN requests to a target's system in an attempt to consume enough server resources to make the system
unresponsive to legitimate traffic. The connection should do the ‘three-way handshake’ (SYN -> SYN-ACK->ACK).
Countermeasures: filtering / increasing backlog / firewalls and proxies / SYN Cache / SYN Cookies.

__I would like to say thank you to my mentor, Karla Saur, for helping and guiding me,
and all the Learn IT, Girl team for the support, and for bringing this program for me and
for many other girls.__


