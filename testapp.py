from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)



def generate_frames(camera):
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # do face recognition here
            # draw a rectangle around the detected face(s) on the frame
            # convert the frame to bytes for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('update.html')

@app.route('/video_feed')
def video_feed():
    camera = cv2.VideoCapture(0)
    return Response(generate_frames(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start')
def start():
    return render_template('start.html')
if __name__ == '__main__' :
    app.run(debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('test.html')

# @app.route('/get_data')
# def get_data():
#     # This is the function that will be called from the HTML page
#     id = 300
#     name = 'test'
#     data = [id, name]
#     return data

# if __name__ == '__main__':
#     app.run(debug=True)
