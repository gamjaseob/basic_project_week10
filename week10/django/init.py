from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '안녕, 세상!'

@app.route('/hello')
def hello_hello():
    return 'HELLO HELLO!'

if __name__ == "__main__":
    app.run(debug=True)