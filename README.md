## About project

This project started with Reading and Solving captchas from the Golestan site. 
Steps:

#### 1) Collecting Captchas:
- Collecting captchas using an API.

#### 2) Getting captchas ready for the ML process:
- Convert captcha backgrounds to black and white.
- Split created picture to alphabet and digits by cropping the picture. 

#### 3) Implement Classification-Algorithms to make cropped pictures to text:
- Train the handmade Dataset from Golestan captchas
- Implement KNN to the trained dataset.
- Save the model to the .sav file for decreasing the running time of the program.
- Get the captcha's text as the output by 96% accuracy.

## How to run?

Install the dependencies.

```sh
pip3 install -r requirements.txt
```

### Train Dataset:
Run [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/modelTrainer.py) for train model using [Datasets](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/DataSet).


### Solve captcha:
After the model created and saved in directory you should run [captchaSolver.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/captchaSolver.py) for solving speciefic captcha.


## Files and directories

- [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/modelTrainer.py): trains the model

- [captchaSolver.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/captchaSolver.py): captcha solver

- [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/cropLettersFromImage.py): image preproccessing and cropping

- [modelTrainer.py](https://github.com/AmirHoseinMousavi/Captcha-Reader/blob/main/TrainAndSolver.ipynb): captcha solving proccess in notebook

- [Datasets](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/DataSet): training dataset captchas

- [Golestan-Captchas](https://github.com/AmirHoseinMousavi/Captcha-Reader/tree/main/Golestan-Captchas): test captchas
