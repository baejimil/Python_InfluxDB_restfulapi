from flask import Flask, json
from flask_cors import CORS
from flask_restplus import Resource, Api, reqparse
from datetime import datetime, timedelta
from functools import wraps
from influxdb import InfluxDBClient
import requests

app = Flask(__name__)
CORS(app)
title = 'my homepage'
api = Api(app=app)

# @app.route('/test', methods=['GET'])
@api.doc('')
# class HealthCheck(Resource):
class abc(Resource):
    url = "http://localhost:5000/schedules"
    response = requests.get(url)
    response.status_code
    data = response.json()
    host='localhost'
    port=8086
    user = 'root'
    password = '1234'
    dbname = 'qwe'
    
    def index():
        url = "http://localhost:5000/schedules"
        response = requests.get(url)
        response.status_code
        data = response.json()
        host='localhost'
        port=8086
        user = 'root'
        password = '1234'
        dbname = 'qwe'

        query = 'select template from testtable'

        for v in data:
                v['measurement'] = 'testtable'
                v['fields'] = {'a' : 'a'}
        client=InfluxDBClient(host, port, user, password, dbname )
        client.write_points([self.data[0]])
        result = client.query(query)
        # print(data)
        print("hello111")

    # @api.param('sensor_id', '')
    def get(self):
        print("hello222")
        url = "http://localhost:5004/"
        response = requests.get(url)
        print(response)

        # '''
        # 사용자가 보낸 parameter를 통해
        # 데이터를 보내줍니다.
        # :return:
        # '''
        # parameter 를 받습니다.
        # param_list = ['sensor_id']
        # parser = reqparse.RequestParser()
        # for param in param_list:
        #     parser.add_argument(param)
        # query = parser.parse_args()
        # print("hello3333")

        # 제대로 parameter를 받았는지 debug를 위해
        # print('_id_{}'.format(query['key']))

        # return 데이터를 받아놓습니다.
        # res = self.data.get('{}'.format(query['key']))
        res = [self.data]
        
        # 데이터, 반응, 헤더 로 구성
        return res, {}
        

api.add_resource(abc, '/v0.0/test')

if __name__ == '__main__':
    app.run(debug=True, port=5005)

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