import os, shutil
from random import randrange

DIRNAME = 'DataSet/'

captchas_path = [1,2,3,4]

if not os.path.exists(DIRNAME):
	os.mkdir(DIRNAME)

counter = 0
for directory in captchas_path:
	try:
		captchas = os.listdir('./' + str(directory) + '/')
		for captcha in captchas:
			if not 'remianed' in captcha and not 'gif' in captcha:
				alphnum = captcha[0]
				if not os.path.exists(DIRNAME + alphnum):
					os.mkdir(DIRNAME + alphnum)
				shutil.copy(str(directory) + '/' + captcha, DIRNAME + alphnum + '/' + str(randrange(1000,99999)) + '.png')	
				print(counter)
				counter += 1			
	except Exception as e:
		print(e)
		continue
