from flask import Flask, render_template,request,redirect,url_for ,jsonify
import flask 
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask.json import jsonify
from bson.objectid import ObjectId

from datetime import date
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/TodoList'
mongo = PyMongo(app)
db = mongo.db



@app.route("/")
def home():
    todo = db.todo.find()
    return render_template("home.html",todo=todo)

    
@app.route('/add', methods=['POST'])
def add_todb():
    d = date.today()
    d=str(d)
    new_todo = request.form.get('new-todo')
    db.todo.insert_one({'task': new_todo, 'status' : 'false', 'date':d})
    return redirect(url_for('home'))

@app.route('/complete/<oid>')
def complete(oid):
    todos = db.todo.find()
    db.todo.update_one({'_id': ObjectId(oid)}, {"$set": {'status': 'true'}})
    return render_template("home.html",todo=todos)

@app.route('/delete_selected')
def delete_selected():
    db.todo.delete_many({'status' : 'true'})
    return redirect(url_for('home'))

@app.route('/delete_all')
def delete_all():
    db.todo.delete_many({})
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True, port=5005)