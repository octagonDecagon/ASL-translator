# SOURCE: https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6
# with some edits to use ASL model

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.preprocessing import image as image_utils

from keras.models import model_from_json
from keras.models import load_model
from tensorflow import keras

from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.applications.vgg16 import preprocess_input

import cv2
import matplotlib.pyplot as plt
from PIL import Image

global labels
labels = {0: 'A',
 1: 'B',
 2: 'C',
 3: 'D',
 4: 'E',
 5: 'F',
 6: 'G',
 7: 'H',
 8: 'I',
 9: 'J',
 10: 'K',
 11: 'L',
 12: 'M',
 13: 'N',
 14: 'O',
 15: 'P',
 16: 'Q',
 17: 'R',
 18: 'S',
 19: 'T',
 20: 'U',
 21: 'V',
 22: 'W',
 23: 'X',
 24: 'Y',
 25: 'Z',
 26: 'del',
 27: 'nothing',
 28: 'space'}
class VideoCamera(object):
    def __init__(self):
        #starts video capture
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
        # encode OpenCV raw frame to jpg and displaying it
        return jpeg.tobytes()
    def get_letter(self):
        ret, frame = self.video.read()

        #resize and convert to RGB
        frame_input = cv2.resize(frame, (200, 200))
        frame_input = cv2.cvtColor(frame_input, cv2.COLOR_BGR2RGB)

        #preprocess the image
        my_image = img_to_array(frame_input)
        my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
        my_image = preprocess_input(my_image)

        #make the prediction
        prediction = model.predict(my_image)
        itemindex = np.where(prediction==1)
        prediction = [labels[k] for k in itemindex[1]]

        #print out the predictions in real time
        #print(prediction)
        return prediction