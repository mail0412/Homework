from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello Suphasara!'

@app.route('/Id')
def Id():
    return '654281101'

@app.route('/name')
def name():
    return 'Suphasara Plangdee'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if _name_ == '_main_':
    app.run(debug=True)