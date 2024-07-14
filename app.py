# app.py

from flask import Flask, render_template, request, redirect, session, jsonify
import pymongo
from bson.objectid import ObjectId
#=====================================================================

# Tạo biến để lưu đường dẫn kết nối 
connection_str = "mongodb+srv://mailongkf:22LCNuBgzPZksiMX@cluster0-mailong.4lpjsis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0-MaiLong"
try:
    # Tạo kết nối đến MongoDB
    print("Connect done")
    client = pymongo.MongoClient(connection_str)
except Exception:
    # Nếu kết nối bị lỗi
    print("Error" + Exception)

# Truy cập vào cơ sở dữ liệu

mydb = client["mydatabase"]
mycol = mydb["todolist"]
print("mycol: ", mycol)
for x in mycol.find():
    print(x)
#=====================================================================
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
	documents = list(mycol.find())
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print(username, password)
		if username in users and users[username] == password:
			return render_template('test_data.html', documents = documents)
		else:
			return render_template('register.html',error=error)
	else:
		return render_template('register.html')



#==================================================================
@app.route('/add_task', methods=['POST'])
def add_task():
	task_name = request.json['text']
	print(str(task_name))
	new_task = {'name': task_name, 'disabled': False}
	result = mycol.insert_one(new_task)
	new_task['_id'] = str(result.inserted_id)
	return jsonify(new_task)


@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_id = request.json['_id']
    result = mycol.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'_id': task_id})

@app.route('/get_data', methods=['GET'])
def get_data():
    data = list(mycol.find({}, {'_id': 0}))
    return jsonify(data)

#==================================================================
if __name__ == '__main__':
	app.run()


