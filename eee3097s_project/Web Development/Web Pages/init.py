from flask import Flask, render_template, redirect, url_for, request, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import mysql.connector

app = Flask(__name__)

temperature = None
luminosity = None
time = None
alert = None
t_x = None
l_x = None
t = None
l = None
y = []

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1Stevethomi!",
  database="FIRE_DETECTION"
)

mycursor = mydb.cursor(buffered=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create_User', methods=['POST','GET'])
def create_User():
    if request.method == 'POST':
        userID = request.form.get('userID')
        fname = request.form.get('fname')
        sname = request.form.get('sname')
        name = fname+" "+sname
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = request.form.get('user')
        if user == 'forestRanger':
            forest_department = request.form.get('forest_department')
            administration = "Forest."+forest_department
        else:
            fire_department = request.form.get('fire_department')
            administration = "FireStation."+fire_department

        sql = "INSERT INTO USER (USERID, NAME, PHONE_NUMBER, PASSWORD, DEPARTMENT) VALUES (%s, %s, %s, %s, %s)"
        val = (userID, name, phone, password, administration)

        mycursor.execute(sql, val)

        mydb.commit()

    return render_template('create_User.html')

@app.route('/login_User', methods=['POST','GET'])
def login_User():
    success = None
    if request.method == 'GET':
        userID = request.args.get('userID')
        password = request.args.get('password')

        sql = "SELECT NAME FROM USER WHERE USERID = %s AND PASSWORD = %s"
        val = (userID, password)

        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()

        success=myresult

    return render_template('login_User.html',success=success)

@app.route('/register_Sensor', methods=['POST','GET'])
def register_Sensor():
    if request.method == 'POST':
        sensorID = request.form.get('sensorID')
        lat_degrees = request.form.get('lat_degrees')
        lat_minutes = request.form.get('lat_minutes')
        lat_seconds = request.form.get('lat_seconds')
        long_degrees = request.form.get('long_degrees')
        long_minutes = request.form.get('long_minutes')
        long_seconds = request.form.get('long_seconds')

        sql = "INSERT INTO SENSOR (SENSORID, LATITUDE_degree, LATITUDE_minute, LATITUDE_second, LONGITUDE_degree, LONGITUDE_minute, LONGITUDE_second) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (sensorID, lat_degrees, lat_minutes, lat_seconds, long_degrees, long_minutes, long_seconds)

        mycursor.execute(sql, val)

        mydb.commit()

    return render_template('register_Sensor.html')

@app.route('/modify_Sensor', methods=['POST','GET'])
def modify_Sensor():
    if request.method == 'POST':
        modify = request.form.get('modify')
        sensorID = request.form.get('sensorID')
        lat_degrees = request.form.get('lat_degrees')
        lat_minutes = request.form.get('lat_minutes')
        lat_seconds = request.form.get('lat_seconds')
        long_degrees = request.form.get('long_degrees')
        long_minutes = request.form.get('long_minutes')
        long_seconds = request.form.get('long_seconds')

        if modify == 'modLatitude':
            sql1 = "DELETE FROM SENSOR WHERE SENSORID = %s"
            val1= (sensorID, )

            mycursor.execute(sql1, val1)

            mydb.commit()

            sql2 = "INSERT INTO SENSOR (SENSORID, LATITUDE_degree, LATITUDE_minute, LATITUDE_second, LONGITUDE_degree, LONGITUDE_minute, LONGITUDE_second) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val2 = (sensorID, lat_degrees, lat_minutes, lat_seconds, long_degrees, long_minutes, long_seconds)

            mycursor.execute(sql2, val2)

            mydb.commit()
        else:
            sql1 = "DELETE FROM SENSOR WHERE SENSORID = %s"
            val1= (sensorID, )

            mycursor.execute(sql1, val1)

            mydb.commit()

            sql2 = "INSERT INTO SENSOR (SENSORID, LATITUDE_degree, LATITUDE_minute, LATITUDE_second, LONGITUDE_degree, LONGITUDE_minute, LONGITUDE_second) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val2 = (sensorID, lat_degrees, lat_minutes, lat_seconds, long_degrees, long_minutes, long_seconds)

            mycursor.execute(sql2, val2)

            mydb.commit()

    return render_template('modify_Sensor.html')

@app.route('/monitor', methods=['POST','GET'])
def monitor():
    # count number of already read values
    mycursor.execute("SELECT * FROM READINGS")
    number_results=mycursor.rowcount
    # read new values from log file, process data, and transfer to database
    readFile(number_results)
    graph()
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    Response(output.getvalue(), mimetype='image/jpg')
    fig.savefig('static/sensor1.jpg')
    return render_template('monitor.html', temperature=temperature, luminosity=luminosity, time=time, alert=alert)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

# read from log file, process data, and transfer to database
def readFile(readFrom = 0):
    # Open file for input
    infile = open(r"/Volumes/share/data.txt", "r")
    input = None
    readFrom = readFrom
    count = 0
    finalLuminosity = None
    global temperature
    global luminosity
    global time
    global alert

    infile.readline() # clear first empty line

    while True:
        input = infile.readline()
        if input != '':
            if count >= (readFrom+1):
                temperature = eval(input[0:5])
                luminosity = eval(input[7:13])
                time = input[15:34]
                if finalLuminosity and luminosity < finalLuminosity:
                    if temperature > 20:
                        alert = True
                else:
                    alert = False

                sql = "INSERT INTO READINGS (SENSORID, TEMPERATURE, LUMINOSITY, ALERT, DATE_TIME) VALUES (%s, %s, %s, %s, %s)"
                val = (5678, temperature, luminosity, alert, time)

                mycursor.execute(sql, val)

                mydb.commit()
            count += 1
        else:
            break
        finalLuminosity = luminosity
    infile.close() # Close the input file

def graph():
    global t_x
    global l_x
    global t
    global l
    global y

    mycursor.execute("SELECT TEMPERATURE FROM READINGS")
    t_x = mycursor.fetchall()

    while len(t_x)>10:
        t_x.pop(0)
    t_x.reverse()

    t = []
    for x in t_x:
        a = str(x)
        a = a[2:6]
        t.append(eval(a))

    mycursor.execute("SELECT LUMINOSITY FROM READINGS")
    l_x = mycursor.fetchall()

    while len(l_x)>10:
        l_x.pop(0)
    l_x.reverse()

    l = []
    for x in l_x:
        a = str(x)
        a = a[2:6]
        l.append(eval(a))

    y = []
    i = 0
    for x in t_x:
        y.append(i)
        i += 30
        
def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(y, t, y, l)
    axis.set_xlabel("time [s]")
    axis.set_ylabel("temperature/luminosity")
    axis.set_title("Environmental Mapping")
    axis.grid(True)

    return fig

if __name__ == '__main__':
    app.run(debug=True)
