import cv2

IMG_DIR = 'Golestan-Captchas/'
INPUT_IMAGE = IMG_DIR + '80861.gif'

INPUT_IMAGE = 'captchaG3.gif'

def sharp_img(img):
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur_image = cv2.blur(gray_img, (4, 4))
	gblur_img = cv2.GaussianBlur(blur_image, (0, 0), 6)
	sharp_img = cv2.addWeighted(gray_img, 1.80, gblur_img, -0.60, 0)
	sharp_not_img = cv2.bitwise_not(sharp_img);
	retval, img_zeroone = cv2.threshold(sharp_not_img, 20, 255, cv2.THRESH_BINARY)
	return img_zeroone

im = cv2.imread(INPUT_IMAGE)
sim = sharp_img(im)

def clear_img(img):
	gray = cv2.rectangle(img, (45, 45), (139, 49), (0,0,0), -1)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
	opening_img = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

	for height in range((opening_img.shape[0])):
		for width in range((opening_img.shape[1])):
			opening_img[height][width]
			if opening_img[height][width] == 255:
				opening_img[height][width] = 0
			else:
				opening_img[height][width] = 255
	return opening_img

cl_img = clear_img(sim)
cv2.imshow("linesDetected", cl_img)
cv2.waitKey(0)
cv2.destroyAllWindows()