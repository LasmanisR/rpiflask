from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if _name_ == '__main__'
    app.run(debug=True, host='0.0.0.0')