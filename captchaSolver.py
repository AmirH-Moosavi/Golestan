#!/usr/bin/env python
import os
import pickle

import numpy as np
from skimage.transform import resize

from cropLettersFromImage import getWords

DataDirectory = "./DataSet/"
Categories = os.listdir(DataDirectory)

filename = "finalized_model.sav"
try:
    loaded_model = pickle.load(open(filename, "rb"))
except:
    print("You should train model and save the model first!")
    exit(0)


def getCaptchaText(Captcha):
    clusters = getWords(Captcha)
    text = ""
    for image in clusters:
        flat_data = []
        img_resized = resize(image, (40, 40, 3))
        flat_data.append(img_resized.flatten())
        flat_data = np.array(flat_data)
        y_output = loaded_model.predict(flat_data)
        text += Categories[y_output[0]].replace("upper", "").replace("lower", "")
    return text


Captcha = "./Golestan-Captchas/69310.gif"
text = getCaptchaText(Captcha)
print("Predicted Text Is:", text)
