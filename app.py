from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Tina Li!'


if __name__ == '__main__':
    app.run()


@app.route('tea')
def tea():
    return render_template("tea.html")