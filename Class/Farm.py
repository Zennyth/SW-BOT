from Class.Exception import Exception
from Class.Template import Template
from Class.Action import Action
from Class.ImageAnalyser import ImageAnalyser
from Class.Status import Status

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
	def __init__(self, sequences = [], description = "", index_sequence = 0):
		self._sequences = sequences
		self._type = description
		self._i = index_sequence
		self._timer = time.time()

	def selectSequence(self, status, socket):
		results = []
		i = 0
		updateCount = False
		for sequence in self._sequences:
			template = sequence.mainTemplate()
			if not(isinstance(template, Exception)):
				result = ImageAnalyser.find(template)
				if result:
					self._activeSequence = sequence
					if i == self._i:
						print("update status !", self._i, i)
						status.add_history(self._type.export((time.time() - self._timer)/60))
						socket.send_status(status.send())
						updateCount = True
					self._activeSequence.execute()
					results.append(result)
					self._timer = time.time()
			# else:
				# print(template)

			# print('Farm search for the main sequence !', end="\r")
			i+=1

		for tempate_error in templates_errors:
			result = ImageAnalyser.find(tempate_error)
			if result:
				tempate_error.execute(status)
				break

		return updateCount