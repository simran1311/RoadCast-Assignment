from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy as sqal
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://sql6398291:SIDq2vj96G@sql6.freemysqlhosting.net/sql6398291'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS']= {'pgSql': 'postgres://ctsrvfes:uVhHgk54pyWO-t7KONKdJozbg5iGkOzV@john.db.elephantsql.com:5432/ctsrvfes'}
sql=sqal(app)

#MySQL Class
class StudentInfo(sql.Model):
    id= sql.Column(sql.Integer, primary_key=True)
    name= sql.Column(sql.String(100))
    rollNo = sql.Column(sql.Integer)
    age = sql.Column(sql.String(100))
    phoneNo =  sql.Column(sql.String(100))
    
    def __init__(self, name, rollNo, age, phoneNo):
        self.name = name
        self.rollNo = rollNo
        self.age = age
        self.phoneNo = phoneNo
#Mysql Class End

#PostgreSQL Class
class StudentInfoPg(sql.Model):
    id= sql.Column(sql.Integer, primary_key=True)
    name= sql.Column(sql.String(100))
    rollNo = sql.Column(sql.Integer)
    age = sql.Column(sql.String(100))
    phoneNo =  sql.Column(sql.String(100))
    
    def __init__(self, name, rollNo, age, phoneNo):
        self.name = name
        self.rollNo = rollNo
        self.age = age
        self.phoneNo = phoneNo
#PostgreSQL Class End



@app.route("/")
def home_page():
    return '<a href="/MySQL">Start</a>'

@app.route('/MySQL',methods=['GET','POST'])
def sql_page():
    if request.method == 'POST':
        sInfo = StudentInfo(request.form['name'], request.form['roll'], request.form['age'], request.form['phone'])
        print(request.form['name'], request.form['roll'], request.form['age'], request.form['phone'])
        sql.session.add(sInfo)
        sql.session.commit()
    
    if request.method == 'GET':
        return render_template("mySQL.html", data=StudentInfo.query.all())

    return render_template("mySQL.html",data=StudentInfo.query.all())


@app.route('/PostgreSQL',methods=['GET','POST'])
def pgsql_page():
    if request.method == 'POST':
        sInfop = StudentInfoPg(request.form['name'], request.form['roll'], request.form['age'], request.form['phone'])
        print(request.form['name'], request.form['roll'], request.form['age'], request.form['phone'])
        sql.session.add(sInfop)
        sql.session.commit()
    
    if request.method == 'GET':
        return render_template("postgreSQL.html", data=StudentInfo.query.all())

    return render_template("postgreSQL.html",data=StudentInfo.query.all())



if __name__ == '__main__':
    sql.create_all()
    app.run()

