from flask import Flask, render_template , request
import mysql.connector
from database import mydb


app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form["name"]
    age = request.form["age"]
    date = request.form["date"]
    time = request.form["time"]
    room_temperature = request.form["room_temperature"]
    room_humidity = request.form["room_humidity"]
    pulse_rate = request.form["pulse_rate"]
    body_temperature = request.form["body_temperature"]

    cursor = mydb.cursor()
    sql = "INSERT INTO patients (p_date,p_time,p_name,age,pulse_rate,body_temperature,room_temperature,room_humidity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date, time,name, age, pulse_rate, body_temperature, room_temperature, room_humidity)
    cursor.execute(sql, val)
    mydb.commit()

    return "Form submitted successfully"






if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
