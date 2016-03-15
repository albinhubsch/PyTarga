#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Author: Albin Hubsch - albin.hubsch@gmail.com
# Website: http://albinhubsch.se
# 
# 

# Extend System Path
import sys
sys.path.append('./modules/')
sys.path.append('./pkgs/websocket_client-0.35.0/')

# Imports
import hidapi
import websocket
import json
import time
import sys
import base64
import requests
import inspect, thread, time
# import Leap
from xml.dom import minidom

from Gamepad import *
from TargaSocket import *

'''
	Main function, initiates and runs complete program
'''
def main():

	# Load settings
	with open('_settings.json') as data_file:
		_settings = json.load(data_file)

	# Create Gamepad
	# Right now only supports one!
	# gp1 = Gamepad(_settings['controllers']['gamepads'][0])

	# Open TARGA socket
	# ts = TargaSocket(_settings['TARGA'])

	# # ts.takeControl()
	# # ts.send('activate', '1')
	# # time.sleep(0.2)
	# # ts.send('activate', '0')
	# # time.sleep(0.2)
	# # ts.send('activate', '0')

	# ts.takeControl()
	# ts.send('horiz', '127')
	# time.sleep(0.15)
	# ts.send('vert', '127')
	# # ts.send('valve', '0')

	# ts.close()

	# controller = Leap.Controller()
	
'''
	Main start
'''
if __name__ == "__main__":
	main()

