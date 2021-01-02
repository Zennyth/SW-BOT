from setup import registry
from Class.Exception import Exception
import cv2
import numpy as np
from mss import mss
from PIL import Image, ImageGrab
import random as r
import time
import imutils

PATH = './Ressources/'
threshold = 0.7

time.sleep(1)

screen = registry["config"]._data["screen"]
SCT = mss()

sct_img = SCT.grab(screen)
img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))
img_gray = cv2.cvtColor(img_init,cv2.COLOR_RGB2GRAY)

template = cv2.imread(PATH + 'chat.JPG', 0)
(tH, tW) = template.shape[:2]
found = None

while not(found):
    sct_img = SCT.grab(screen)
    img_init = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX"))
    img_gray = cv2.cvtColor(img_init,cv2.COLOR_RGB2GRAY)
    for scale in np.linspace(0.05, 1.0, 30)[::-1]:
        print(scale)
        resized = imutils.resize(img_gray, width = int(img_gray.shape[1] * scale))
        r = img_gray.shape[1] / float(resized.shape[1])

        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        edged = resized
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where( result >= threshold )
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if (found is None or maxVal > found[0]) and len(loc[0]) > 0:
            print("found")
            found = (maxVal, maxLoc, r)

(_, maxLoc, r) = found
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
# draw a bounding box around the detected result and display the image
cv2.rectangle(img_init, (startX, startY), (endX, endY), (0, 0, 255), 2)
cv2.imshow("Image", img_init)
cv2.waitKey(0)