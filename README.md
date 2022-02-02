This project started with Reading and Solving captchas from the Golestan site. 
Steps:

1) Collecting Captchas:
-Collecting captchas using an API.

2) Getting captchas ready for the ML process:
- Convert captcha backgrounds to black and white.
- Split created picture to alphabet and digits by cropping the picture. 

3) Implement Classification-Algorithms to make cropped pictures to text:
- Train the handmade Dataset from Golestan captchas
- Implement KNN to the trained dataset.
- Save the model to the .sav file for decreasing the running time of the program.
- Get the captcha's text as the output by 96% accuracy.
