from flask import Flask, render_template, request, send_from_directory, url_for, Response, stream_with_context
import db_conn
import db_execute_query
from imgcapture import imcapture
from recogniy import recogniseImg, face_train
import image_manupulation
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

# camera = cv2.VideoCapture("http://192.168.30.73:4747/video")
camera = cv2.VideoCapture(0)

@app.route("/update", methods = ['GET', 'POST'])
def update():
    updated = False
    if (request.method == 'POST'):
        id = request.form['id']
        name = request.form['name']
        imcapture(id, name, camera)
        image_manupulation.insert_to_db()
        image_manupulation.crbk()
        updated = True
    return render_template('update.html', updated = updated)


@app.route("/details", methods = ['GET', 'POST'])
def details():
    id = '' 
    name = ''
    total_attendence = ''
    image = url_for('static', filename = 'person.png')
    if(request.method == 'POST') :       
        id = request.form['id']
        connection = db_conn.create_db_connection('localhost', 'root', '', 'students_details')
        query = "select name, total_att from total_attendence where id = %s"
        results = db_execute_query.read_query(connection, query, id)
        if not results:
            image = url_for('static', filename = 'person.png')
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
    return Response(generate_frames(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/start")
def start(): 
    def generate():
        yield render_template('start.html')
        yield '<script>document.getElementById("loading-bar-script").onload = startLoadingBar;</script>'
        # Execute the long-running task here
        # ...
        face_train()
    return Response(stream_with_context(generate()))
    

@app.route('/get_data')
def get_data():
    id = ''
    name =''
    total_attendence = ''
    id = recogniseImg(camera)  
    if id != 0 or id != None:
        connection = db_conn.create_db_connection('localhost', 'root', '', 'students_details')
        query = "select name, total_att from total_attendence where id = %s"
        results = db_execute_query.read_query(connection, query, id)
        connection.close()
        for row in results:
            name, total_attendence = row
    data = [id, name, total_attendence]
    return data

if __name__ == '__main__' :
    app.run(debug=True)