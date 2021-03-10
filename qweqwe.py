from flask import Flask, json
from flask_cors import CORS
from flask_restplus import Resource, Api, reqparse
from datetime import datetime, timedelta
from functools import wraps
from influxdb import InfluxDBClient
import requests

app = Flask(__name__)
CORS(app)
# title = 'my homepage'
# api = Api(app=app)


@app.route('/')
def index():
    host='localhost'
    port=8086
    user = 'root'
    password = '1234'
    dbname = 'qweqwe'
    query = 'select template from testtable'

    url = "http://localhost:5000/schedules"
    response = requests.get(url)
    response.status_code
    data = response.json()
    bind_params = {'host' : 'server01'}
    for i in range(len(data)):
            data[i]['measurement'] = 'testtable'
            data[i]['fields'] = {'c': 'c'}
            data[i]['tag'] = {'host':'server01',
            'region': 'us-west'}
            data[i]['time'] = 'None'
    print(data[0])
    # for v in data:
    #         v['measurement'] = 'table'
    dt = datetime.now() - timedelta(seconds=6)
    data[0]['time'] = dt
    print ("UTC now=<%s>" % (dt))
    client=InfluxDBClient(host, port, user, password, dbname )
    client.write_points([data[0]])
    result = client.query(query)
    return 'sensor activated!'

# @api.doc('/a')
# class abc(Resource):
#     def get(self):
#         url = "http://localhost:5000/schedules"
#         response = requests.get(url)
#         response.status_code
#         data = response.json()

#         res = data
#         return res, {}
# api.add_resource(abc, '/')

# @api.param('sensor_id', '')
# def get(self):
#     print("hello222")
#     url = "http://localhost:5000/schedules"
#     response = requests.get(url)
#     response.status_code
#     data = response.json()

#     # '''
#     # 사용자가 보낸 parameter를 통해
#     # 데이터를 보내줍니다.
#     # :return:
#     # '''
#     # parameter 를 받습니다.
#     # param_list = ['sensor_id']
#     # parser = reqparse.RequestParser()
#     # for param in param_list:
#     #     parser.add_argument(param)
#     # query = parser.parse_args()
#     # print("hello3333")

#     # 제대로 parameter를 받았는지 debug를 위해
#     # print('_id_{}'.format(query['key']))

#     # return 데이터를 받아놓습니다.
#     # res = self.data.get('{}'.format(query['key']))
#     res = self.data

#     # 데이터, 반응, 헤더 로 구성
#     return res, {}


# api.add_resource(abc, '/v0.0/test')

if __name__ == '__main__':
    app.run(debug=True, port=5004)

# @api.param('body', '', 'body')
    # def post(self):
    #     '''
    #     사용자가 보낸 session 정보를 통해
    #     수정 역할을 합니다.
    #     :return: 수정 여부를 반환합니다.
    #     '''
    #     data = request.get_json(silent=True, force=True)
    #     # 데이터 확인
    #     print(data)


    #     return data

    # def put(self):
    #     '''
    #     사용자가 보낸 데이터를 저장한다.
    #     :return:
    #     '''
    #     return {'msg': 'put ok'}

    # def delete(self):
    #     '''
    #     데이터를 삭제한다.
    #     :return:
    #     '''
    #     return {'msg': 'delete ok'}
