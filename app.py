from flask import Flask

app = Flask(__name__)


@app.route('/total')
def cal():
    pass


if __name__ == '__main__':
    app.run()
