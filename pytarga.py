#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Author: Albin Hubsch - albin.hubsch@gmail.com
# Website: http://albinhubsch.se
# 
# 

# Extend System Path
import sys
sys.path.append('./pkgs/websocket_client-0.35.0/')
sys.path.append('./modules/')

# Imports
import websocket
from Gamepad import *
import json
import base64
import requests
from xml.dom import minidom

# Main function, initiates and runs complete program
def main():

	# Load settings
	with open('_settings.json') as data_file:
		_settings = json.load(data_file)

	# Create Gamepad
	# Right now only supports one!
	# gp1 = Gamepad(_settings['controllers']['gamepads'][0])

	# Open Socket against TARGA

	ws = websocket.WebSocket()
	ws.connect("ws://"+str(_settings['TARGA']['host'])+":"+str(_settings['TARGA']['port']))
	# print ws.recv()
	print base64.b64decode(ws.recv())

	b64 = base64.b64encode('<?xml version="1.0" encoding="utf-8"?><targa><destination uuid="8042d29d-6d43-43d4-a51a-3fd0c932f6f4" type="slave"/><content type="set"><map name="valve" value="1"/></content></targa>')

	ws.send(b64)

	# Fetch UUID
	r = requests.get('http://'+str(_settings['TARGA']['host'])+'/php/getxml.php?file=targa.configuration.xml')

	systemprofile = minidom.parseString(r.content)
	uuid = systemprofile.getElementsByTagName('Slaves')[0].getElementsByTagName('Slave')[0].getElementsByTagName('Identifier')[0].attributes['uuid'].value
	# print uuid

	ws.close()

	

if __name__ == "__main__":
	main()

