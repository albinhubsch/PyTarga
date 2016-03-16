#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, inspect, thread, time
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

'''
'''
class LeapListener(Leap.Listener):

	def setSocket(self, socket):
		self.socket = socket

	# On every frame
	def on_frame(self, controller):

		time.sleep(0.12)

		frame = controller.frame()

		for hand in frame.hands:
			
			if hand.is_right:
				# print hand.grab_strength
				print hand.direction
				if hand.grab_strength < 0.1:
					direction = hand.direction

					reHoriz = (((direction[0] - (-1)) * (255 - 0)) / (1 - (-1))) + 0
					reVert = (((direction[1] - (-1)) * (255 - 0)) / (1 - (-1))) + 0
					reVert = 255-reVert

					self.socket.takeControl()
					self.socket.send('horiz', reHoriz)
					# time.sleep(0.1)
					self.socket.takeControl()
					self.socket.send('vert', reVert)
				else:
					self.socket.takeControl()
					self.socket.send('horiz', '127')
					# time.sleep(0.1)
					self.socket.takeControl()
					self.socket.send('vert', '127')