# app.py

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


app.secret_key = 'my_secret_key'

# Thiết lập tên người sử dụng và mật khẩu
users = {
	'mailong': '1234',
	'user2': 'password2'
}

# Tới trong login
@app.route('/')
def view_form():
	return render_template('register.html')


@app.route('/handle_get', methods=['GET'])
def handle_get():
	if request.method == 'GET':
		username = request.args['username']
		password = request.args['password']
		print(username, password)
		if username in users and users[username] == password:
			return '<h1>Welcome!!!</h1>'
		else:
			return '<h1>invalid credentials!</h1>'
	else:
		return render_template('register.html')


@app.route('/handle_post', methods=['POST','GET'])
def handle_post():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print(username, password)
		if username in users and users[username] == password:
			return render_template('index.html')
		else:
			return render_template('register.html',error=error)
	else:
		return render_template('register.html')

if __name__ == '__main__':
	app.run()


