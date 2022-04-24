#!/usr/bin/env python
import os
import pickle

import numpy as np
import pandas as pd
from skimage.io import imread
from skimage.transform import resize
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

print('loading DateSet...')
target = []
flat_data = []
DataDirectory = './DataSet/'

Categories = os.listdir(DataDirectory)

for index, i in enumerate(Categories):
    print(i, '-> ', str(round(100*(index + 1)/len(Categories))) + '%')
    target_class = index
    path = os.path.join(DataDirectory,i)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path,img))
        img_resized = resize(img_array,(40,40,3))
        flat_data.append(img_resized.flatten())
        target.append(target_class)

flat_data = np.array(flat_data)
target = np.array(target)

df = pd.DataFrame(flat_data)
df['Target'] = target

x = df.iloc[:,:-1].values
y = target

print("Input data dimensions:",x.shape)
print("Output data dimensions:",y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle = True, test_size = 0.2, random_state = 109, stratify = y)

print("Dimensions of input training data:",x_train.shape)
print("Dimensions of input testing data:",x_test.shape)
print("Dimensions of output training data:",y_train.shape)
print("Dimensions of output testing data:",y_test.shape)

print('Training model...')
knn = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
knn.fit(x_train, y_train)

print('saving model...')
filename = 'finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))

y_pred = knn.predict(x_test)
print(y_test)
print(y_pred)
ac = accuracy_score(y_test,y_pred)
print(f'Accuracy: {ac}')
