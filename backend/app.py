from flask_cors import CORS
import pymongo
from flask import Flask, request, jsonify

client = pymongo.MongoClient('localhost', 27017)
db = client['recipes-app']
collection = db['recipe']

app = Flask(__name__)
CORS(app)

# Define uma rota para o método GET
@app.route('/recipes', methods=['GET'])
def get_data():
    data = []
    for item in collection.find():
        item['_id'] = str(item['_id'])
        data.append(item)
    return jsonify(data)

# Define uma rota para o método POST
@app.route('/recipes', methods=['POST'])
def data():
    data = request.get_json()
    res = collection.insert_one(data)
    data['_id'] = str(res.inserted_id)
    print(data)
    return jsonify({
        'status': 'success',
        'data': data
    })


if __name__ == '__main__':
    app.run(debug=True)
