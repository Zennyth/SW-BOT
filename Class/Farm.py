from Class.Exception import Exception
from Class.Template import Template
from Class.Action import Action
from Class.ImageAnalyser import ImageAnalyser

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

class Farm():
	def __init__(self, sequences = []):
		self._sequences = sequences

	def selectSequence(self):
		results = []

		for sequence in self._sequences:
			template = sequence.mainTemplate()
			if not(isinstance(template, Exception)):
				result = ImageAnalyser.find(template)
				if result:
					self._activeSequence = sequence
					self._activeSequence.execute()
					results.append(result)
			else:
				print(template)

			print('Farm search for the main sequence !', end="\r")

		for tempate_error in templates_errors:
			result = ImageAnalyser.find(tempate_error)
			if len(loc[0]) > 0:
				tempate_error.execute()
				break