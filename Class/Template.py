from Class.Exception import Exception
from Class.Action import Action

import cv2
import numpy as np
from mss import mss
from PIL import Image
import mouse as m
import time
import random as r
import numpy as np

BOUNDING_BOX = {'top': 50, 'left': 1800, 'width': 2000, 'height': 1200}
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
			if self._iteration <= self.maxIteration:
				self._iteration += 1
				return Exception(0, "no coordinates")
			else:
				self._iteration = 0
				return False

	def execute(self):
		sct_img = SCT.grab(BOUNDING_BOX)
		img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))
		img_gray = cv2.cvtColor(img_init,cv2.COLOR_RGB2GRAY)
		w, h = self._template.shape[::-1]
		result = cv2.matchTemplate(img_gray, self._template, cv2.TM_CCOEFF_NORMED)
		loc = np.where( result >= self._threshold )
		if len(loc[0]) > 0:
			coordinates = list(zip(*loc[::-1]))[0]
			point = (int(coordinates[0] + self._template.shape[1]*r.random() + BOUNDING_BOX['left']), int(coordinates[1] + self._template.shape[0]*r.random() + BOUNDING_BOX['top']))
			for action in self._actions:
				action.execute(point)
			self._iteration = 0
			return True
		else:
			if self._required:
				return Exception(0, "no coordinates")
			else:
				if self._iteration <= self.maxIteration:
					self._iteration += 1
					return Exception(0, "no coordinates")
				else:
					self._iteration = 0
					return False


	def __str__(self):
		return "matching '" + self._path + "' with " + str(self._threshold) + " threshold"