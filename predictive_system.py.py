# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 18:15:06 2025

@author: druvi
"""

import numpy as np
import pickle

#loading the model
loaded_model=pickle.load(open('C:/Users/druvi/OneDrive/Desktop/ML/heart_disease_model.sav','rb'))#reading binary format=rb

#Types to check the data
input_data=(51,1,0,140,298,0,1,122,1,4.2,1,3,3)
#input_data=x_test.iloc[7]
#import random
#input_data=x_test.iloc[random.randint(0,len(x_test)-1)]
#print(input_data)
# change the input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape numpy array aswe are predicting for only on one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person does have a Heart Disease')