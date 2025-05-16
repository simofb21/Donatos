from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/login" method="post">
            <input type="text" name="nm" placeholder="Enter your name">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
    else:
        user = request.args.get('nm')

    if user:
        return redirect(url_for('success', name=user))
    else:
        return "Error: 'nm' parameter missing", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
