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
        ret, image = self.video.read()
        
        def predict_image():
            img = load_image()
            #img = np.expand_dims(img, axis=0)
            pred = model.predict(img[np.newaxis])
            predicted_letter = categories[np.argmax(pred)]
            print('predicted letter is ',predicted_letter)
        def load_image():
            #load image data into an array
            img = self.video.read()
            #img = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img, 'RGB')

            #data augmentation - resizing the image
            resized_img = img.resize((200, 200))
    
            return np.array(resized_img) #return numpy array of image
        

        predict_image()

        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

