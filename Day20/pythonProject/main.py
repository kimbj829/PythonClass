import stat

from flask import Flask
from flask import jsonify, request, make_response, json

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World";

@app.route('/sign', methods=['post'])
def sign():
    user = request.json;
    print(user);
    response = {
        'name' : user['name'],
        'email' : user['email'],
        'password' : user['password']
    };
    result = json.dumps(response, ensure_ascii=False);
    res = make_response(result);
    return res, 200;

if __name__ == '__main__':
    app.run(port=4000);