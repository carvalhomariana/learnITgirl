#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:49:00 2017

@author: mcarvalho

Read "README.dm" file for more explanation about this code "image_carver.py" source code.

This Python Code "image_carver.py" was created to extract images from unsecure websites,
such as DailyMail.co.uk, Telegraph.co.uk, globo.com, alibaba.com, among others.

To start playing with this code is mandatory that you have a pcap file in
order to make it run.

Run this code with:
    python image_carver.py filename.pcap
    
On my files you will find an example of two pcap files, so you can try using them.
To record a pcap file, I used WireShark.

You can always record your own traffic using WireShark.
Remember that this Python file only is useful for unsecure websites (http instead of https)

"image_carver.py" has a function called "face_detect" that was not used for this project.
I kept the function so I can develop it in the future, or you can play around with it.

"""

import re
import sys
import cv2
import scapy
from scapy.all import *

#def face_detect(path, file_name):
#    img = cv2.imread(path)
#    cascade = cv2.CascadeClassifier('/Users/mcarvalho/haarcascade_frontalface_alt.xml')
#    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (300,300))
#    if len(rects) == 0:
#        return False
#    rects[:, 2:] += rects[:, :2]
#    for x1, y1, x2, y2 in rects:
#        cv2.retangle(img, (x1, y1), (x2, y2), (127, 255,0), 2)
#        cv2.imwrite('%s-%s' % (PCAP, file_name), img)
#    return True

def get_http_headers(http_payload):
    try:
        headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]
        headers = dict(re.findall(r'(?P<name>.*?):(?P<value>.*?)\r\n', headers_raw))
    except:
        return None
    if 'Content-Type' not in headers:
        return None
    return headers

def extract_image(headers, http_payload):
    image,image_type = None, None
    try:
        if 'image' in headers['Content-Type']:
            image_type = headers['Content-Type'].split('/')[1]
            image = http_payload[http_payload.index('\r\n\r\n')+4:]
            try:
                if 'Content-Encoding' in headers.keys():
                    if headers['Content-Encoding'] == 'gzip':
                        image = zlib.decompress(image, 16+zlb.MAX_WBITS)
                    elif headers['Content-Encoding'] == 'deflate':
                        image = zlib.decompress(image)
            except:
                pass
    except:
        return None, None
    return image, image_type

def http_assembler(PCAP):
    carved_images, faces_detected = 0, 0
    p = rdpcap(PCAP)
    sessions = p.sessions()
    print('number of sessions: ', len(sessions))
    temp = ''
    
    for session in sessions:
        http_payload = ''
        for packet in sessions[session]:
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    http_payload += str(packet[TCP].payload)
            except:
                pass
            headers = get_http_headers(http_payload)
            if headers is None:
                continue
            
            # extract the raw image and return the image type and the binary body of
            # the image itself
            image, image_type = extract_image(headers, http_payload)             
            
            if image is not None and image_type is not None:
#                print (len(image), len(temp))
                if (len(image) > len(temp)):
                    temp = str(image)
#                    print(len(temp))
                    continue
                
                file_name = '%s-pic_carver_%d.%s' %(PCAP, carved_images, image_type)
                print(file_name)
                fd = open((file_name), 'wb')
                print(len(temp))
                fd.write(temp)
                temp = image
                fd.close()
                carved_images += 1
                
#                try:
#                    result = face_detect('%s' %(file_name), file_name)
#                    if result is True:
#                        faces_detected += 1
#                except:
#                    pass
    return carved_images, faces_detected

def Main(filename):
    carved_images, faces_detected = http_assembler(filename)
    print 'Carved images: ', carved_images
    
    #    print('faces detected: ', faces_detected)

if __name__== "__main__":
    if len(sys.argv) < 2:
        print 'Please provide file name'
    else:
        filename = sys.argv[1]
        Main(filename)
    
    
