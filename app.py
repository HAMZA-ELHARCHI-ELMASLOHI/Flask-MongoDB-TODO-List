from flask import Flask, render_template,request,redirect,url_for
import flask 
from pymongo import MongoClient
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/TodoList'
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def home():
    db.todo .insert_one({'title': "todo title", 'body': "todo body"})
    return render_template("home.html")


if __name__=='__main__':
    app.run(debug=True, port=5005)