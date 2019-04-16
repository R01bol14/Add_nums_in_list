from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/total', methods=["POST"])
def cal():
    """Check of data is list containing integer or float; Then sum up numbers in list"""

    data_list = request.get_json()
    list_item = data_list['list_item']

    if not isinstance(list_item, list):
        return "Not list item"

    if not all(isinstance(x, (int, float)) for x in list_item):
        return 'All list items are not int or float'

    return jsonify({'total': sum(list_item)})


if __name__ == '__main__':
    app.run()
