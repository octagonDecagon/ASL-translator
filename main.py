
from flask import Flask, render_template, Response
from camera import VideoCamera


# SOURCE: https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6

global letter

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
def gen(camera): 
    while True:
         #get camera frame
        letter=camera.get_letter()
        frame = camera.get_frame() #initializes object and uses get_frame attribute
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        render_template('Model.html', letter)


    #renders HTML Template

@app.route('/video_feed')
def video_feed():
    #shows video feed to user
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Model.html', methods=["GET", "POST"])
def model():
    return render_template('Model.html')
    #renders HTML Template

    #renders HTML Template


if __name__ == '__main__':
    app.run(debug=True)
