from flask import Flask, request
from flask_cors import CORS , cross_origin
from test import google as g
from flask import request

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/search', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        print("request cames from : " +str(request.environ['REMOTE_ADDR']))
        res = dict()
        req = request.get_json()
        topic = req["topic"]
        tmp = g(topic)
        # tmp.append({'ip' : request.environ['REMOTE_ADDR']})
        res["response"] = [tmp , {'ip' : request.environ['REMOTE_ADDR']}]
        print("res last state ")
        print(res)
        return res
    else:
        return "ERR Flask"

if __name__ == '__main__':
    app.run(debug=True)