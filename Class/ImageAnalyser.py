import cv2
import numpy as np
from mss import mss

bounding_box = {'top': 50, 'left': 1800, 'width': 1800, 'height': 1200}

sct = mss()

class ImageAnalyser():
	def __init__(self):
		self._id = 0

	def get(self):
		return []

	def analyse(self):
		# sct_img = sct.grab(bounding_box)
		# img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))

		# cv2.imshow('img', img)
		# cv2.waitKey(0)
		return "image_results"