#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Author: Albin Hubsch - albin.hubsch@gmail.com
# Website: http://albinhubsch.se
# 
# 

import sys
sys.path.append('../pkgs/websocket_client-0.35.0/')

import websocket

class TargaSocket(object):

	def __init__(self, targa_settings):
		self.host = str(targa_settings['host'])
		self.port = int(targa_settings['port'])
		self.ws = websocket.WebSocket()
		ws.connect("ws://"+self.host+":"+str(self.port))

	def connect(self):
		pass

	def send(self):
		pass

	def read(self):
		pass