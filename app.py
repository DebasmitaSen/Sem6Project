from flask import Flask, render_template, request, send_from_directory, url_for, Response
import db_conn
import db_execute_query
from imgcapture import imcapture
# from recogniy import recogniseImg
import connection
import cv2

# Create a Flask Instance
app = Flask(__name__)

@app.route('/Data/<path:filename>')
def data(filename):
    return send_from_directory('Data', filename)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

camera = cv2.VideoCapture(0)

@app.route("/update", methods = ['GET', 'POST'])
def update():

    if (request.method == 'POST'):
        id = request.form['id']
        name = request.form['name']
        imcapture(id, name, camera)
        connection.insert_to_db()
        connection.crbk()
    return render_template('update.html')


@app.route("/details", methods = ['GET', 'POST'])
def details():
    id = '' 
    name = ''
    total_attendence = ''
    image = url_for('static', filename = 'person.webp')
    if(request.method == 'POST') :       
        id = request.form['id']
        connection = db_conn.create_db_connection('localhost', 'root', '', 'person')
        query = "select name, total_att from total_attendence where id = %s"
        results = db_execute_query.read_query(connection, query, id)
        if not results:
            image = url_for('static', filename = 'person.webp')
            return render_template('details.html', no_data = True, image = image)
        
        for row in results:
            name, total_attendence = row
        connection.close()
        path_1st_image = '/img1.jpg'
        path_1st_image = id + path_1st_image
        image = url_for('data', filename = path_1st_image)
        return render_template('details.html', id = id, name = name, attendence = total_attendence, image = image)
    
    return render_template('details.html', image = image)

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

@app.route('/video_feed')
def video_feed():
    # camera = cv2.VideoCapture(0)
    return Response(generate_frames(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/start")
def start():
    total_attendence = ''
    name = ''
    id = ''
    # id, name = recogniseImg()
    return render_template('start.html', attendence = total_attendence, name = name, id = id, recognized = True)

if __name__ == '__main__' :
    app.run(debug=True)