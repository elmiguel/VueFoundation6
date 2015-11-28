from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run(debug=True)
