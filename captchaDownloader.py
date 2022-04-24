import os
import random

import requests

DIRNAME = "Golestan-Captchas"
if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)

uniques = []
numberOfImages = 30
counter = 1
while counter <= numberOfImages:
    url = "https://golestan.ikiu.ac.ir/Forms/AuthenticateUser/captcha.aspx"
    r = requests.get(url, allow_redirects=True)

    if r.status_code == 200:
        contentLength = r.headers["content-length"]
        if contentLength not in uniques:
            uniques.append(contentLength)
            fileName = str(int(random.uniform(10000, 99999))) + ".gif"
            with open(DIRNAME + "/" + fileName, "wb") as f:
                f.write(r.content)

            print(counter)
            counter += 1
