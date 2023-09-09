## About project

This project aims to read and Solve captchas from the Golestan website. 
Steps:

#### 1) Collect Captchas:
- Collect captchas using an API.

#### 2) Make captchas ready for the ML process:
- Convert captcha backgrounds to black and white.
- Split the created picture into alphabet and digits by cropping the picture. 

#### 3) Implement Classification-Algorithms to make cropped pictures to text:
- Train the handmade Dataset from Golestan captchas
- Implement KNN to the trained dataset.
- Save the model to the .sav file to decrease the program's running time.
- Generate the captcha's text with 96% accuracy.

## How to run?

Install the dependencies.

```sh
pip3 install -r requirements.txt
```

### Train Dataset:
Run [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/modelTrainer.py) for train model using [Datasets](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/DataSet).


### Solve captcha:
After the model is created and saved in the directory you should run [captchaSolver.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/captchaSolver.py) to solve the specific captcha.


## Files and directories

- [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/modelTrainer.py): trains the model

- [captchaSolver.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/captchaSolver.py): captcha solver

- [cropLettersFromImage.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/cropLettersFromImage.py): image preproccessing and cropping

- [TrainAndSolver.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/TrainAndSolver.ipynb): captcha solving proccess in notebook

- [Datasets](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/DataSet): training dataset captchas

- [Golestan-Captchas](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/Golestan-Captchas): test captchas
