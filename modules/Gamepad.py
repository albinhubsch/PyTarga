#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Author: Albin Hubsch - albin.hubsch@gmail.com
# Website: http://albinhubsch.se
# 
# 

import hidapi
hidapi.hid_init()

'''
'''
class Gamepad(object):

	'''
		initiate
	'''
	def __init__(self, gamepad_obj):
		self.name = gamepad_obj['name']
		self.vendor_id = int(gamepad_obj['vendor_id'])
		self.product_id = int(gamepad_obj['product_id'])
		# self.serial_number = gamepad_obj['serial_number']

		# # Open USB HID
		self.HID = self.openHID()

	'''
		openHID
	'''
	def openHID(self):
		return hidapi.hid_open(self.vendor_id, self.product_id)

	'''
		read
	'''
	def read(self):
		return hidapi.hid_read(self.HID, 12)
		
