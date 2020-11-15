# Load all needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import random
import pandas as pd
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.applications import *
from tensorflow.keras.callbacks import *
from tensorflow.keras.initializers import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image



n_classes = 15
model = Sequential()
model.add(Conv2D(20, (10, 10), activation='relu', input_shape=[224, 224, 3]))
model.add(Dense(100, activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(n_classes, activation='softmax'))
# compile model
opt = SGD(lr=0.001)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

model.load_weights('/home/sebastian/project_fe/utilities/model_weights.hdf5')

labels = {0: '655',
 1: '277',
 2: '654',
 3: '172',
 4: '280',
 5: '272',
 6: '295',
 7: '634',
 8: '170',
 9: '169',
 10: '281',
 11: '656',
 12: '653',
 13: '584',
 14: '585'}

def predict(coor):
    fig = plt.figure(figsize=(10,10))
    plt.scatter(x=coor.LATITUD,y=coor.LONGITUD, c='k')    
    plt.axis('off')
    fig.savefig('assets/route.jpg')

    test_image = image.load_img("assets/route.jpg", target_size=(224, 224))
    print("image generated")
    # Predict artist
    test_image = image.img_to_array(test_image)
    test_image /= 255.
    test_image = np.expand_dims(test_image, axis=0)

    prediction = model.predict(test_image)
    prediction_probability = np.amax(prediction)
    prediction_idx = np.argmax(prediction)

    return (labels[prediction_idx], prediction_probability)


