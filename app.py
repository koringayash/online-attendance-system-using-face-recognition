from flask import Flask,render_template,request,session,redirect,send_file
from datetime import datetime
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import pymysql
import cv2
import datetime 
import pytz
import json
import ast
import os


pymysql.install_as_MySQLdb()


with open('config.json','r') as c:
    params = json.load(c)["params"]

app=Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config['UPLOAD_CONTACT_IMG'] = params['upload_contact']

if params['local_server']:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Attendance(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Id_no = db.Column(db.String(200), nullable=False)
    present = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=True)
    img_file = db.Column(db.String(120), nullable=True)

@app.route('/')
def home():
    return render_template("index.html",params=params)

@app.route('/training')
def training():
    # file = open(r'train_model.py', 'r').read()
    # print(file)
    # exec(file)
    exec(open("train_model.py").read())
    return render_template("dashboard.html",params=params)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/uploader",methods = ['GET', 'POST'])
def uploader():
    msg = "You are not login"
    if ( 'user' in session and session['user'] == params['admin_user']):
        msg = "Your request is invalid"
        if request.method == 'POST':
            id_no = request.form.get('id_no')
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("test")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    print('Tari maa ne')
                    continue
                cv2.imshow("test", frame)
                k = cv2.waitKey(1)

                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    dirPath = (os.path.join(app.config['UPLOAD_FOLDER'],id_no))
                    print(dirPath)
                    if not os.path.isdir(dirPath):
                        os.mkdir(dirPath)
                    img_name = "_{}.png".format(img_counter)
                    img_loc = os.path.join(dirPath,img_name)
                    print(img_loc)
                    cv2.imwrite(img_loc, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()
            cv2.destroyAllWindows()
            msg = "Image Uploaded successfully!"
    
    #passing appropriat msg
    return render_template("dashboard.html",params=params,msg=msg)

@app.route("/reset")
def reset():
    msg = "attendance sheet is reset"
    student_present = set()
    with open('F:\collage\sem-6\Project\\Website\\present_student.txt','w') as f:
        f.write(str(student_present))
    return render_template("dashboard.html",params=params,msg=msg)

@app.route("/about")
def about():
    return render_template("about.html",params=params)


# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html",params=params)

@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
    print("hello")
    if request.method=="POST":
        Id_no = request.form.get('Id_no')
        attends = Attendance.query.filter_by(Id_no=Id_no).all()
        return render_template("attendance.html",params=params,attends=attends)
    return render_template("attendance.html",params=params)


@app.route("/takingattendance",methods = ['GET', 'POST'])
def takingattendance():    
    msg = "You are not login"
    if ( 'user' in session and session['user'] == params['admin_user']):
        c_t = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        t = str(c_t.hour) + ':' + str(c_t.minute) + ':' + str(c_t.second)
        d = c_t.strftime('%Y-%m-%d')
        total_students = os.listdir("F:\collage\sem-6\Project\WebSite\static\\assets\studentsImg")
        print(total_students)
        for student in total_students:
            present = "0"
            with open('F:\collage\sem-6\Project\\Website\\present_student.txt','r') as f:
                present_student = ast.literal_eval(f.read())
            if student in present_student:
                present="1"
            attendance = Attendance(Id_no=student,present=present,date=d,time=t)            
            db.session.add(attendance)
            db.session.commit()
        msg = "Attendance is taken successfully!" 
    #passing appropriat msg
    return render_template("dashboard.html",params=params,msg=msg)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    #temparari for checking purpose only
    # return render_template("dashboard.html",params=params)
    if ( 'user' in session and session['user'] == params['admin_user']):
        return render_template("dashboard.html",params=params)
    msg = ""
    if request.method=="POST":
        username = request.form.get('username')        
        userpass = request.form.get('pass')
        if(username == params['admin_user'] and userpass == params['admin_password']):
            session['user'] = username
            return render_template("dashboard.html",params=params)
        msg = "invalid username and password"

    print(msg)
    return render_template("login.html", params=params,msg=msg)

@app.route('/showingpost',methods=['GET','POST'])
def showingpost():
    if ( 'user' in session and session['user'] == params['admin_user']):
        requ = Contacts.query.filter_by().all()
        return render_template("post.html",params=params,posts=requ)
    return render_template("login.html", params=params)

@app.route('/download',methods=['GET','POST'])
def download():
    # with open('total_students.txt','r') as f:
    #         total_students = ast.literal_eval(f.read())
    total_students = os.listdir("F:\collage\sem-6\Project\WebSite\static\\assets\studentsImg")
    df = pd.DataFrame(total_students, columns=['Id_no'])
    presnet = []
    for row in df['Id_no']:
        
        with open('F:\collage\sem-6\Project\\Website\\present_student.txt','r') as f:
            present_student = ast.literal_eval(f.read())
        if row in present_student:
            presnet.append("1")
        else:
            presnet.append("0")
    df['Present'] = presnet
    c_t = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    d = c_t.strftime('%Y-%m-%d')
    fileName = d + ".csv"
    df.to_csv("Rough\\"+fileName)
    path = "F:\collage\sem-6\Project\WebSite\Rough"
    path = path + "\\" + fileName
    return send_file(path, as_attachment=True)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')
        f = request.files['file1']
        print(os.path.join(app.config['UPLOAD_CONTACT_IMG'], f.filename))
        f.save(os.path.join(app.config['UPLOAD_CONTACT_IMG'], f.filename))
        entry = Contacts(name=name,email=email,phone_num=phone,date = datetime.datetime.now(pytz.timezone('Asia/Kolkata')),mes=msg,img_file = f.filename)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from '+name,
        #                   sender = email,
        #                   recipients = [params['gmail-user']],
        #                   body = msg + "\n" + phone
        #                   )

    return render_template("contact.html",params=params)

@app.route('/takePhoto')
def takePhoto():
    pass


if __name__ == "__main__":
     app.run(debug=True ,port=8080)