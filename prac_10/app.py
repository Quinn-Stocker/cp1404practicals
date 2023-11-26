from flask import Flask

app = Flask(__name__)


def celsius_calc(celsius=0.0):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
def greet():
    return 'Hello'


@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<temp>')
def f(temp=0.0):
    return f"{celsius_calc(temp)}"


if __name__ == '__main__':
    app.run()
