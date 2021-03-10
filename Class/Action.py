from Class.Exception import Exception

import mouse as m
import time
import pyperclip
import keyboard
import random as r

class Action():
	def __init__(self, _id, wait = 0, description = "", task = ""):
		self._id = _id
		self._wait = wait
		self._description = description 
		self._task = task

	def execute(self, point, status = None):
		if self._wait > 0:
			time.sleep(self._wait)

		if self._id == -1:
			Exception(2, "Quizz !", status)
		elif self._id == 0:
			m.move(point[0], point[1])
			time.sleep(r.random())
			m.click(button='left')
		elif self._id == 1:
			pyperclip.copy(self._task)
			time.sleep(r.random())
			keyboard.press_and_release('ctrl+v')
			keyboard.press_and_release('enter')
		else:
			return Exception(1, "wrong id on : execute | " + str(self))


	def throw_error(self, errors):
		return False

	def __str__(self):
		return "execute " + str(self._id)