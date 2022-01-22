from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

IMG_DIR = 'Golestan-Captchas/'
INPUT_IMAGE = IMG_DIR + '99821.gif'

# INPUT_IMAGE = 'captchaG.gif'

def sharp_img(img):
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur_image = cv2.blur(gray_img, (4, 4))
	gblur_img = cv2.GaussianBlur(blur_image, (0, 0), 6)
	sharp_img = cv2.addWeighted(gray_img, 1.80, gblur_img, -0.60, 0)
	sharp_not_img = cv2.bitwise_not(sharp_img);
	retval, img_zeroone = cv2.threshold(sharp_not_img, 20, 255, cv2.THRESH_BINARY)
	return img_zeroone


def clear_img(img):
	im  = cv2.imread('mask.png')
	mask = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	retval, t_mask = cv2.threshold(mask, 70, 255, cv2.THRESH_BINARY)
	masker = cv2.bitwise_not(t_mask)
	img = cv2.bitwise_and(img, masker)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
	opening_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	opening_img = cv2.bitwise_not(opening_img)

	return opening_img

im = cv2.imread(INPUT_IMAGE)
sim = sharp_img(im)

cl_img = clear_img(sim)

# cv2.imshow("ClearedImage", cl_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('captcha.png', cl_img)