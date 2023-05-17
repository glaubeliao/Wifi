#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '192.168.100.122'
PORT = 24

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

outdata = 'hello tcp'
print('send: ' + outdata)
s.send(outdata.encode())

indata = s.recv(1024)
print('recv: ' + indata.decode())

s.close()
