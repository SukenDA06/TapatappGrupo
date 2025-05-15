import dadesServer3 as dades
from dadesServer3 import Account, Infant, Tap, Position, Condition, Therapy
from flask import Flask, jsonify, request

app = Flask(__name__)

class UserDAO:
    def __init__(self):
        self.accounts = dades.accounts

    def get_all_accounts(self):
        return [account.__dict__ for account in self.accounts]

    def get_account_by_username(self, user_name):
        for account in self.accounts:
            if account.user_name == user_name:
                return account.__dict__

class ChildDAO:
    def __init__(self):
        self.infants = dades.infants

    def get_all_infants(self):
        return [infant.__dict__ for infant in self.infants]

    def get_infants_by_user_id(self, acc_id):
        infants_ids = []
        for rel in dades.relation_acc_infant:
            if rel["acc_id"] == acc_id:
                infants_ids.append(rel["inf_id"])
        infants_dicts = []
        for infant in self.infants:
            if infant.inf_id in infants_ids:
                infants_dicts.append(infant.__dict__)
        return infants_dicts
    
user_dao = UserDAO()
child_dao = ChildDAO()

@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    accounts = user_dao.get_all_accounts()
    return jsonify(accounts)

@app.route('/account/<username>', methods=['GET'])
def get_account_by_username(username):
    account = user_dao.get_account_by_username(username)
    if account:
        return jsonify(account)
    else:
        return jsonify({'error': 'Account not found'}), 404

@app.route('/children', methods=['GET'])
def get_all_children():
    children = child_dao.get_all_infants()
    return jsonify(children)

@app.route('/children/<int:acc_id>', methods=['GET'])
def get_children_by_user_id(acc_id):
    children = child_dao.get_infants_by_user_id(acc_id)
    return jsonify(children)

if __name__ == '__main__':
    app.run(debug=True)