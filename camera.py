# SOURCE: https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6
# with some edits to use ASL model

import numpy as np
from PIL import Image
import os
import tensorflow as tf
from tensorflow import keras
import cv2


global model 
model = tf.keras.models.load_model('ASL_model.h5')

class VideoCamera(object):
    def __init__(self):
        #starts video capture
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()

        def predict_image(pathname):
            img = load_image(pathname)
            #img = np.expand_dims(img, axis=0)
            pred = model.predict(img[np.newaxis])
            predicted_letter = categories[np.argmax(pred)]
            print(predicted_letter)
        def load_image(pathname):
            #load image data into an array
            img = cv2.imread(pathname)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_array = Image.fromarray(img, 'RGB')

            #data augmentation - resizing the image
            resized_img = img_array.resize((200, 200))
    
            return np.array(resized_img) #return numpy array of image


        #predict_image('drive/MyDrive/ASL Proj: WAI/photo.jpg')

        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

