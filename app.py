from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Tina Li! This is my first code change.'

if __name__ == '__main__':
    app.run()

@app.route('/hello')
def hello():
    return render_template('Hello World from Tina Li!')

