from flask import Flask, jsonify, request
import os


app = Flask(__name__)

accounts = [
    {'name': 'Mohsen', 'balance': 450.0},
    {'name': 'hosein', 'balance': 600.0},
]

'''
usage: curl http://127.0.0.1:8080/accounts
'''
@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify(accounts)

'''
 usage: curl http://127.0.0.1:8080/accounts/<id>
'''
@app.route('/accounts/<id>', methods=['GET'])
def get_account(id):
    id = int(id) - 1
    return jsonify(accounts[id])

'''
usage: curl -X POST -H "Content-Type: application/json" -d '{"name": "<name>", "balance": <balance>}' http://127.0.0.1:8080/account 
'''
@app.route('/account', methods=['POST'])
def add_account():
    name = request.json['name']
    balance = request.json['balance']
    data = {'name':name, 'balance': balance}
    accounts.append(data)
    return jsonify(data)


@app.route('/wireshark/open', methods=['GET'])
def do_something():
    os.popen('sudo wireshark')
    data =  {}
    return 'done\n'

@app.route('/wireshark/close', methods=['GET'])
def do_anotherthing():
    os.system('proc=`pgrep wireshark`; sudo kill $proc')
    return 'done\n'

if __name__ == "__main__":
    app.run(host='192.168.1.9',port=8080)