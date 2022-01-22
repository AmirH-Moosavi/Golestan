from Captcha_Reader import getWords
from shutil import copy
import os

IMAGES = 'Golestan-Captchas/'

OUTPUT = 'OUTPUT/'

if not os.path.exists(OUTPUT):
	os.mkdir(OUTPUT)

for index, captcha in enumerate(os.listdir(IMAGES)):
	print(index + 1)
	dirName = OUTPUT + captcha.replace('.gif', '')
	if not os.path.exists(dirName):
		os.mkdir(dirName)
	copy(IMAGES + captcha, dirName)
	getWords(IMAGES + captcha, dirName)
