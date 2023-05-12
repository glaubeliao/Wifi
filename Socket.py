#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '192.168.100.146'
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
indata = s.recv(1024)

print('recv: ' + indata.decode())
