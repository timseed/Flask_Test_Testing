from tim.instance.app import app
print("Loading routes")
@app.route('/')
def top():
    return 'Running'

@app.route('/hello')
def hello():
    return 'Hello, World!'