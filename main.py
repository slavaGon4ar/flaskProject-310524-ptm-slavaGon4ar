from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greet_user', name=name))
    return '''
        <h2>Welcome to the home page!</h2><h1>Hello, Flask!</h1>
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/user/<name>')
def greet_user(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
