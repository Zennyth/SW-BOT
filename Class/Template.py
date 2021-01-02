from Class.Exception import Exception
from Class.Action import Action
from Class.ImageAnalyser import ImageAnalyser

import cv2
import numpy as np
from mss import mss
from PIL import Image
import mouse as m
import time
import random as r
import numpy as np
import imutils

BOUNDING_BOX = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
SCT = mss()

PATH = './Ressources/'

class Template():
	def __init__(self, path, threshold = 0.8, actions = [Action(0, description = "click")], required = True, maxIteration = 0, activeRate = 1):
		self._path = path
		self._template = cv2.imread(PATH + self._path + '.jpg', 0)
		self._threshold = threshold
		self._actions = actions
		self._required = required
		self._maxIteration = maxIteration
		self._iteration = 0
		self._activeRate = activeRate

	def throw_error(self):
		if self._required:
			return Exception(0, "no coordinates")
		else:
			if self._iteration <= self._maxIteration:
				self._iteration += 1
				return Exception(0, "no coordinates")
			else:
				self._iteration = 0
				return False

	def execute(self):
		found = ImageAnalyser.find(self)
		if found:
			coordinates = found
			point = (int(coordinates[0] + self._template.shape[1]*r.random() + BOUNDING_BOX['left']), int(coordinates[1] + self._template.shape[0]*r.random() + BOUNDING_BOX['top']))
			for action in self._actions:
				action.execute(point)
			self._iteration = 0
			return True
		else:
			if self._required:
				return Exception(0, "no coordinates")
			else:
				if self._iteration <= self._maxIteration:
					self._iteration += 1
					return Exception(0, "no coordinates")
				else:
					self._iteration = 0
					return False


	def __str__(self):
		return "matching '" + self._path + "' with " + str(self._threshold) + " threshold"