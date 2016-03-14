#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Author: Albin Hubsch - albin.hubsch@gmail.com
# Website: http://albinhubsch.se
# Date: 03-2016
# 

import websocket
import requests
import base64

class TargaSocket(object):

	'''
		Initiate TARGA socket object
	'''
	def __init__(self, targa_settings):
		self.host = str(targa_settings['host'])
		self.port = int(targa_settings['port'])
		self.ws = websocket.WebSocket()
		self.uuid = self.getIdentity()

		# Try to connect and read first message from server
		self.connect()
		print self.read()

	'''
		Try to connect to server connection
	'''
	def connect(self):
		try:
			self.ws.connect("ws://"+self.host+":"+str(self.port))
		except Exception, e:
			raise e

	'''
		Send data through socket connection
	'''
	def send(self, map_name, map_value):
		
		prepXML = '<?xml version="1.0" encoding="utf-8"?><targa><destination uuid="'+str(self.uuid)+'" type="slave"/><content type="set"><map name="'+str(map_name)+'" value="'+str(map_value)+'"/></content></targa>'

		try:
			self.ws.send(self.encode(prepXML))
		except Exception, e:
			raise e

	'''

		?!?!?!   FRÅGAN ÄR OM DENNA KOMMER BEHÖVAS   ?!?!?!

		Sends a ?take control? command to TARGA server

	'''
	def takeControl(self):
		self.ws.send('<?xml version="1.0" encoding="utf-8"?><targa><content type="command"><command action="control" param="take"/></content></targa>')

	'''
		Read incoming data on socket connection
		Returns an xml string decoded from a base64 string
	'''
	def read(self):
		return self.decode(self.ws.recv())

	'''
		Close socket
	'''
	def close(self):
		try:
			self.ws.close()
		except Exception, e:
			raise e

	'''
		Encode data string to base64 string
	'''
	def encode(self, data):
		return base64.b64encode(data)

	'''
		Decode data string to base64 string
	'''
	def decode(self, data):
		return base64.b64decode(data)

	'''
		Fetch uuid from TARGA raspberry webserver
	'''
	def getIdentity(self):
		# Fetch UUID
		try:
			r = requests.get('http://'+self.host+'/php/getxml.php?file=targa.configuration.xml')
			systemprofile = minidom.parseString(r.content)
			uuid = systemprofile.getElementsByTagName('Slaves')[0].getElementsByTagName('Slave')[0].getElementsByTagName('Identifier')[0].attributes['uuid'].value

			return uuid
		except Exception, e:
			raise e