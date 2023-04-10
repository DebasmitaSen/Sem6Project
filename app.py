from flask import Flask, render_template, request, send_from_directory, url_for
import db_conn
import db_execute_query


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

@app.route("/update", methods = ['GET', 'POST'])
def update():
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


@app.route("/start")
def start():
    return render_template('start.html')

if __name__ == '__main__' :
    app.run(debug=True)