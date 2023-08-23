from flask import Flask, request, jsonify

app = Flask(_name_)

# Endpoint to check if the service is available
@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

# Endpoint to add two numbers
@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first + second
    return jsonify({"result": result}), 200

# Endpoint to subtract two numbers
@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first - second
    return jsonify({"result": result}), 200

if _name_ == '_main_':
    app.run()
