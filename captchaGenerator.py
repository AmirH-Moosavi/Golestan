from PIL import Image, ImageDraw, ImageFont, ImageOps
import random, os

OUTPUT = 'Dataset/'

if not os.path.exists(OUTPUT):
	os.mkdir(OUTPUT)

SEED = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

W = 40
H = 40

for item in SEED:
	print(item)
	msg = item

	directoryName = OUTPUT + item + '/'
	if not os.path.exists(directoryName):
		os.mkdir(directoryName)

	counter = 0
	while counter < 100:
		img = Image.new(mode='RGB', size=(W,H), color = 0)

		font = ImageFont.truetype('/Library/Fonts/Arial.ttf', random.randrange(40,50))

		text_layer = Image.new('L', (W, H))
		draw = ImageDraw.Draw(text_layer)
		w, h = draw.textsize(msg, font = font)
		draw.text((0, 0), msg,  font = font, fill = 255)

		rotated_text_layer = text_layer.rotate(random.randrange(-30,30), expand=1)

		img.paste(ImageOps.colorize(rotated_text_layer, (255,255,255), (255,255,255)), (0,0+random.randrange(-5, 0)),  rotated_text_layer)
		img.save(directoryName + str(random.randrange(1000,9999)) + '.png')
		counter += 1