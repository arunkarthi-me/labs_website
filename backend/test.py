from flask import Flask, render_template, request,render_template_string,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__)


# Connect to MongoDB
client = MongoClient('mongodb+srv://kannanb2745:xxYGaI4NCAwvHxxb@kannan.8bbghpx.mongodb.net/?retryWrites=true&w=majority&appName=kannan')
db = client['linux_db']  # Change 'testdb' to your database name
collection = db['sensor']  # Change 'userdata' to your collection name

global userid
global password

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        
        # Store the data in MongoDB
        collection.insert_one({'userid': userid, 'password': password})
        
        return render_template("logined.html",userid=userid, password=password)
        
    return render_template('index_test.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
