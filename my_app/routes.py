from flask import jsonify, request
from my_app.utils import read_table, find_values_of_the_last_months
from my_app import app

@app.route('/', methods=['POST'])
def homepage():
    table = read_table()
    data = request.json
    final_value = find_values_of_the_last_months(table, data['months'])

    return jsonify({'final_value': final_value})