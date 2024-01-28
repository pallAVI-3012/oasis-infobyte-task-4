from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

users = {}  # A dictionary to store user information


@app.route('/')
def home():
    return 'Welcome to the Simple Login Authentication System!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = {'password': password}
            return redirect(url_for('login'))
        else:
            return 'Username already exists. Please choose another username.'

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('secured_page'))
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('login.html')


@app.route('/secured-page')
def secured_page():
    if 'username' in session:
        return f'Welcome, {session["username"]}! This is a secured page.'
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
