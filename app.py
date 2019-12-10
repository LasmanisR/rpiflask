from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def index():
    return render_template('indexc.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

