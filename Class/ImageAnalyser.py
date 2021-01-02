import cv2
import numpy as np
from mss import mss
import imutils
from PIL import Image

screen = {'top': 0, 'left': 0, 'width': 1800, 'height': 1200}

SCT = mss()

class ImageAnalyser():
	@staticmethod
	def set_screen(new_screen):
		global screen
		screen = new_screen

	@staticmethod
	def find(template):
		sct_img = SCT.grab(screen)
		img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))
		img_gray = cv2.cvtColor(img_init,cv2.COLOR_RGB2GRAY)

		(tH, tW) = template._template.shape[:2]
		found = None

		for scale in np.linspace(0.05, 1.0, 30)[::-1]:
			resized = imutils.resize(img_gray, width = int(img_gray.shape[1] * scale))
			r = img_gray.shape[1] / float(resized.shape[1])

			if resized.shape[0] < tH or resized.shape[1] < tW:
				break

			edged = resized
			result = cv2.matchTemplate(edged, template._template, cv2.TM_CCOEFF_NORMED)
			loc = np.where( result >= template._threshold )
			(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

			if (found is None or maxVal > found[0]) and len(loc[0]) > 0:
				found = (maxVal, maxLoc, r)
		
		if found:
			(_, maxLoc, r) = found
			return (int(maxLoc[0] * r), int(maxLoc[1] * r))
		else:
			return None