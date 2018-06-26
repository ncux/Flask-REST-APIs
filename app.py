from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [
    {'name': 'Store 1', 'items': [{'name': 'item 1', 'price': 12.33}]},
    {'name': 'Store 2', 'items': [{'name': 'item 2', 'price': 13.33}]},
    {'name': 'Store 3', 'items': [{'name': 'item 3', 'price': 14.33}]},
    {'name': 'Store 4', 'items': [{'name': 'item 4', 'price': 15.33}]},
    {'name': 'Store 5', 'items': [{'name': 'item 5', 'price': 16.33}]}
]



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    request_info = request.get_json()
    new_store = {
        'name': request_info['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_info = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_info['name'], 'price': request_info['price']}
            store['items'].append(new_item)
            return jsonify(new_item)

    return "Store wasn't found!"



@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return "Store wasn't found!"


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return "Store wasn't found!"



@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})





app.run(port=5000)