from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

app.secret_key = 'secret'

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'item was not found'}, 404

    def post(self, name):
        data = request.get_json(silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class Items(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')


app.run(port=5000, debug=True)