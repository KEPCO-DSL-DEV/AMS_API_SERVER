# -- coding: utf-8 --


#import json
#from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api 
from flask_restful import reqparse
import pymysql
import pandas as pd


# def execute(query):
#     pc.execute(query)
#     return pc.fetchall()



connection = pymysql.connect(host='10.41.179.169',
                             user='kepco',
                             password='power12#',
                             port=3306,
                             db='silver_care',
                             charset='utf8',
                             #ssl={'ssl-mode': 'DISABLED'}
                            
                             )

cursor = connection.cursor()

# connection.commit()


# if(connection):
#     cursor.close()
#     connection.close()

# getphoneNum = cursor.fetchone()
# phoneNum = getphoneNum[0]

# kCodeinListwithU = cursor.fetchall()
# kCodeList=[code[0] for code in kCodeinListwithU]





#쿼리 입력
genTable = """
CREATE TABLE teacher (
    id          serial PRIMARY KEY,
    name        varchar(40),
    jumin       char(13),
    adm         date,
    retire      timestamptz
);
"""

# query = """
# select id from users limit 1
# """

# #일반적인 쿼리 조회 방법
#cursor.execute(genTable)
#connection.commit()

#pandas를 통한 조회 방법
# pd.read_sql("select id from users limit 1", product)

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def get(self):
    #def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']
            # if _userName == "의택":
            #     return "true"
            # else:
            #     return "false"
            return {'Email': args['email'], 'UserName': args['user_name'], 'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/userinfo')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/test', methods=['GET'])
def test():
    args1 = request.args['args1']
    args2 = request.args['args2']
    args3 = request.args['args3']
    return testFunc(args1, args2,args3)

def index():
    return 'Hello Flask'
#@app.route('/testapi')(testFunc(3))

@app.route('/info', methods=['GET', 'POST'])
def info():
    id = request.args.get('id')
    return id

# String 타입의 username 파라메터
# http://localhost:5000/user/사용자명
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# int 타입의 post_id 파라메터
# http://localhost:5000/post/19
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# float 타입의 pi 파라메터
# http://localhost:5000/circle/3.14
@app.route('/circle/<float:pi>')
def show_pi(pi):
    # show the post with the given id, the id is an integer
    return 'PI %f' % pi

# path 타입의 path 파라메터
# http://localhost:5000/path/path/test/kkk/
@app.route('/path/<path:path>')
def show_path(path):
    # show the post with the given id, the id is an integer
    return 'path %s' % path

#@app.route('/polls/questions/', methods=['GET', 'POST'])
