from flask import Flask, jsonify, request 
import requests
  
app = Flask(__name__) 
  
@app.route('/translate', methods=['GET']) 
def helloworld(): 
    if request.method == 'GET': 
        txt = request.args["text"]
        data = {"result": str(requests.get(txt).text)} 
        print(data)
        res = jsonify(data)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
  
  
if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=443, ssl_context=('server.crt', 'server.key')) 