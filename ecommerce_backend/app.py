from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_friend():
    return 'Hello, Friend!'

if __name__ == '__main__':
    app.run(debug=True)