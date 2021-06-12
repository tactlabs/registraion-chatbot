from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///actions/chats_db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50))
    clg_name = db.Column(db.String(50))
    dept_name = db.Column(db.String(10))
    stud_year = db.Column(db.String(10))
    os_type = db.Column(db.String(50))
    email_id = db.Column(db.String(30))
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat-history',methods=['GET','POST'])
def show_chats():
    user = User.query.all()
    return render_template('chats.html',user=user)

@app.route('/del_entry',methods=['GET','POST'])
def del_entry():
    return render_template('del_entry.html')

@app.route('/delete_entry',methods=['GET','POST'])
def delete_books():
    user_id=request.form['id']
    entryToDelete = db.session.query(User).filter_by(id=user_id).one()
    db.session.delete(entryToDelete)
    db.session.commit()
    user = User.query.all()
    return render_template('chats.html',user=user)


if __name__ == '__main__':
    app.run()
