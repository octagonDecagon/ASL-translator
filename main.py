
from flask import Flask, render_template, Response, session
from camera import VideoCamera
from flask_socketio import SocketIO, emit
from flask import jsonify

# SOURCE: https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6

app = Flask(__name__)

global letter
global camera
camera=VideoCamera()
letter = '*default*'

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Model.html', methods=["GET", "POST"])
def model():  
    return render_template('Model.html')
    #renders HTML Template
def gen(): 

    while (True):
        #get camera frame    
        frame = camera.get_frame() #initializes object and uses get_frame attribute
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/video_feed')
def video_feed():
    #shows video feed to user
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/curr_letter', methods = ['GET'])
def curr_letter():
    #returns a json object of the letter
    letter=camera.get_letter()
    message = {'letter': letter}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)
