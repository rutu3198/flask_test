from flask import Flask,jsonify
from flask_pymongo import PyMongo




app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/assignment'

mongo = PyMongo(app)

@app.route('/')
def index ():
    return '<h1>hello</h1>'

@app.route('/mydata', methods=['GET'])
def getdata():
    user = mongo.db.mydata.find()
    output =[]
    for s in user:
        output.append({'name' : s['name'], 'img' : s['img'],'summary':s['summary']})

    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)
