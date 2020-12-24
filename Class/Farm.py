from Class.Exception import Exception
from Class.Template import Template
from Class.Action import Action

#/ Actions error \#

actions = {
	"error": Action(-1, description = "Quizz !")
}

#/ Templates error \#

templates_errors = [
	Template("quizz", actions = [actions['error']])
]

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

class Farm():
	def __init__(self, sequences = []):
		self._sequences = sequences

	def selectSequence(self):
		results = []

		sct_img = SCT.grab(BOUNDING_BOX)
		img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))
		img_gray = cv2.cvtColor(img_init,cv2.COLOR_RGB2GRAY)

		for sequence in self._sequences:
			template = sequence.mainTemplate()
			if not(isinstance(template, Exception)):
				w, h = template._template.shape[::-1]
				result = cv2.matchTemplate(img_gray, template._template, cv2.TM_CCOEFF_NORMED)
				loc = np.where( result >= template._threshold )
				if len(loc[0]) > 0:
					self._activeSequence = sequence
					self._activeSequence.execute()
					results.append(list(zip(*loc[::-1]))[0])
			else:
				print(template)

			print('Farm search for the main sequence !', end="\r")

		for tempate_error in templates_errors:
			w, h = tempate_error._template.shape[::-1]
			result = cv2.matchTemplate(img_gray, tempate_error._template, cv2.TM_CCOEFF_NORMED)
			loc = np.where( result >= tempate_error._threshold )
			if len(loc[0]) > 0:
				tempate_error.execute()
				break