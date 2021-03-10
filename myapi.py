from flask import Flask, json
from flask_cors import CORS
from flask_restplus import Resource, Api, reqparse
from datetime import datetime, timedelta
from influxdb import InfluxDBClient
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    host='localhost'
    port=8086
    user = 'root'
    password = '1234'
    dbname = 'sensorDB'
    query = 'select template from table'

    url = "http://localhost:5000/schedules"
    response = requests.get(url)
    response.status_code
    data = response.json()
    print(data[0])

    for i in range(len(data)):
            data[i]['measurement'] = 'sensor_table'
            data[i]['fields'] = {'cds': '304', 'temp': '23.6°C'}
    # for v in data:
    #         v['measurement'] = 'table'
    client=InfluxDBClient(host, port, user, password, dbname )
    client.write_points([data[0]])
    result = client.query(query)
    return "sensor activated!"

if __name__ == '__main__':
    app.run(debug=True, port=5003)
