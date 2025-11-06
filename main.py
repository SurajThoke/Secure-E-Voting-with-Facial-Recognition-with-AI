from flask import Flask, render_template, url_for, request, session, flash, redirect
from flask_mail import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pymysql
import pandas as pd
import numpy as np
import os
import cv2
from PIL import Image
import shutil
import datetime
import time
import requests
from sklearn.preprocessing import LabelEncoder
import pickle
le = LabelEncoder()




facialdata = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(facialdata)

mydb=pymysql.connect(host='localhost', user='root', password='admin', port=3306, database='smart_voting')

sender_address = 'suarjthoke06@gmail.com' #sender's email id
sender_password= 'ynppomwqwkbxuhcs' #sender's email password

app = Flask(__name__)

app.config['SECRET_KEY']='ce058dbd9b56efdeaa8ad730fe5abde2'



@app.before_request
def setup():
    if 'IsAdmin' not in session:
        session['IsAdmin'] = False
    if 'User' not in session:
        session['User'] = None


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/typeofvoteelection',methods=['POST','GET'])
def typeofvoteelection():
    return render_template('typeofvoteelection.html')


@app.route('/typeofelection', methods=['POST','GET'])
def typeofelection():
    return render_template('typeofelection.html')

@app.route('/update')
def update():
    return render_template('update.html')






@app.route('/admin', methods=['GET', 'POST'])
def admin():
    is_admin = session.get('IsAdmin', False)

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@voting.com' and password == 'admin':
            session['IsAdmin'] = True
            session['User'] = 'admin'
            flash('Admin login successful', 'success')
            is_admin = True
        else:
            flash('Invalid credentials', 'danger')

    return render_template('admin.html', admin=is_admin)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('home'))


#-----------------------------------------------ADD NOMINIEE----------------------------------------------


@app.route('/zptc', methods=['POST','GET'])
def zptc():
    if request.method=='POST':
        member=request.form['member_name']
        party=request.form['party_name']
        logo=request.form['test']
        nominee=pd.read_sql_query('SELECT * FROM zptcnomiee', mydb)
        all_members=nominee.member_name.values
        all_parties=nominee.party_name.values
        all_symbols=nominee.symbol_name.values
        if member in all_members:
            flash(r'The member already exists', 'info')
        elif party in all_parties:
            flash(r"The party already exists", 'info')
        elif logo in all_symbols:
            flash(r"The logo is already taken", 'info')
        else:
            sql="INSERT INTO zptcnomiee (member_name, party_name, symbol_name) VALUES (%s, %s, %s)"
            print(sql)
            cur=mydb.cursor()
            cur.execute(sql, (member, party, logo))
            mydb.commit()
            cur.close()
            flash(r"Successfully registered a new nominee", 'primary')
    return render_template('zptc.html',admin=session['IsAdmin'])


@app.route('/assembly', methods=['POST','GET'])
def assembly():
    if request.method=='POST':
        state = request.form['state']
        member=request.form['member_name']
        party=request.form['party_name']
        logo=request.form['test']
        nominee=pd.read_sql_query("SELECT * FROM assemblynomiee where village='%s'"%state, mydb)
        all_members=nominee.member_name.values
        all_parties=nominee.party_name.values
        all_symbols=nominee.symbol_name.values
        if member in all_members:
            flash(r'The member already exists', 'info')
        elif party in all_parties:
            flash(r"The party already exists", 'info')
        elif logo in all_symbols:
            flash(r"The logo is already taken", 'info')
        else:
            sql="INSERT INTO assemblynomiee (village, member_name, party_name, symbol_name) VALUES (%s, %s, %s, %s)"
            cur=mydb.cursor()
            cur.execute(sql, (state, member, party, logo))
            print(cur)
            mydb.commit()
            cur.close()
            flash(r"Successfully registered a new nominee", 'primary')
    return render_template('assembly.html',admin=session['IsAdmin'])


@app.route('/mptc', methods=['POST','GET'])
def mptc():
    if request.method=='POST':
        member=request.form['member_name']
        party=request.form['party_name']
        logo=request.form['test']
        nominee=pd.read_sql_query('SELECT * FROM mptcnomiee', mydb)
        all_members=nominee.member_name.values
        all_parties=nominee.party_name.values
        all_symbols=nominee.symbol_name.values
        if member in all_members:
            flash(r'The member already exists', 'info')
        elif party in all_parties:
            flash(r"The party already exists", 'info')
        elif logo in all_symbols:
            flash(r"The logo is already taken", 'info')
        else:
            sql="INSERT INTO mptcnomiee (member_name, party_name, symbol_name) VALUES (%s, %s, %s)"
            cur=mydb.cursor()
            cur.execute(sql, (member, party, logo))
            mydb.commit()
            cur.close()
            flash(r"Successfully registered a new nominee", 'primary')
    return render_template('mptc.html')




@app.route('/add_nominee', methods=['POST','GET'])
def add_nominee():
    if request.method=='POST':

        member=request.form['member_name']
        party=request.form['party_name']
        logo=request.form['test']
        nominee=pd.read_sql_query('SELECT * FROM nominee', mydb)
        all_members=nominee.member_name.values
        all_parties=nominee.party_name.values
        all_symbols=nominee.symbol_name.values
        if member in all_members:
            flash(r'The member already exists', 'info')
        elif party in all_parties:
            flash(r"The party already exists", 'info')
        elif logo in all_symbols:
            flash(r"The logo is already taken", 'info')
        else:
            sql="INSERT INTO nominee (member_name, party_name, symbol_name) VALUES (%s, %s, %s)"
            cur=mydb.cursor()
            cur.execute(sql, (member, party, logo))
            mydb.commit()
            cur.close()
            flash(r"Successfully registered a new nominee", 'primary')
    return render_template('nominee.html', admin=session['IsAdmin'])

#--------------------------------------ADD NOMINIEE--------------------------------------------------------


#---------------------------------------VOTER REGISTRATION----------------------------------------------------

@app.route('/registration', methods=['POST','GET'])
def registration():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        state = request.form['state']
        d_name = request.form['d_name']

        middle_name = request.form['middle_name']
        aadhar_id = request.form['aadhar_id']
        voter_id = request.form['voter_id']
        pno = request.form['pno']
        age = int(request.form['age'])
        email = request.form['email']
        voters=pd.read_sql_query('SELECT * FROM voters', mydb)
        all_aadhar_ids=voters.aadhar_id.values
        all_voter_ids=voters.voter_id.values
        if age >= 18:
            if (aadhar_id in all_aadhar_ids) or (voter_id in all_voter_ids):
                flash(r'Already Registered as a Voter')
            else:
                sql = 'INSERT INTO voters (first_name, middle_name, last_name, aadhar_id, voter_id, email,pno,state,d_name, verified) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)'
                cur=mydb.cursor()
                cur.execute(sql, (first_name, middle_name, last_name, aadhar_id, voter_id, email, pno, state, d_name, 'no'))
                mydb.commit()
                cur.close()
                session['aadhar']=aadhar_id
                session['status']='no'
                session['email']=email
                return redirect(url_for('verify'))
        else:
            flash("if age less than 18 than not eligible for voting","info")
    return render_template('voter_reg.html')


@app.route('/zptcregister', methods=['POST','GET'])
def zptcregister():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        state = request.form['state']
        d_name = request.form['d_name']

        middle_name = request.form['middle_name']
        aadhar_id = request.form['aadhar_id']
        voter_id = request.form['voter_id']
        pno = request.form['pno']
        age = int(request.form['age'])
        email = request.form['email']
        voters=pd.read_sql_query('SELECT * FROM zptcvoters', mydb)
        all_aadhar_ids=voters.aadhar_id.values
        all_voter_ids=voters.voter_id.values
        if age >= 18:
            if (aadhar_id in all_aadhar_ids) or (voter_id in all_voter_ids):
                flash(r'Already Registered as a Voter')
            else:
                sql = 'INSERT INTO zptcvoters (first_name, middle_name, last_name, aadhar_id, voter_id, email,pno,state,d_name, verified) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)'
                cur=mydb.cursor()
                cur.execute(sql, (first_name, middle_name, last_name, aadhar_id, voter_id, email, pno, state, d_name, 'no'))
                mydb.commit()
                cur.close()
                session['aadhar']=aadhar_id
                session['status']='no'
                session['email']=email
                return redirect(url_for('zptcverify'))
        else:
            flash("if age less than 18 than not eligible for voting","info")
    return render_template('zptcvoter_reg.html')


@app.route('/mptcregister', methods=['POST','GET'])
def mptcregister():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        state = request.form['state']
        d_name = request.form['d_name']

        middle_name = request.form['middle_name']
        aadhar_id = request.form['aadhar_id']
        voter_id = request.form['voter_id']
        pno = request.form['pno']
        age = int(request.form['age'])
        email = request.form['email']
        voters=pd.read_sql_query('SELECT * FROM mptcvoters', mydb)
        all_aadhar_ids=voters.aadhar_id.values
        all_voter_ids=voters.voter_id.values
        if age >= 18:
            if (aadhar_id in all_aadhar_ids) or (voter_id in all_voter_ids):
                flash(r'Already Registered as a Voter')
            else:
                sql = 'INSERT INTO mptcvoters (first_name, middle_name, last_name, aadhar_id, voter_id, email,pno,state,d_name, verified) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)'
                cur=mydb.cursor()
                cur.execute(sql, (first_name, middle_name, last_name, aadhar_id, voter_id, email, pno, state, d_name, 'no'))
                mydb.commit()
                cur.close()
                session['aadhar']=aadhar_id
                session['status']='no'
                session['email']=email
                return redirect(url_for('mptcverify'))
        else:
            flash("if age less than 18 than not eligible for voting","info")
    return render_template('mptcvoter_reg.html')


@app.route('/assmregister', methods=['POST','GET'])
def assmregister():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        state = request.form['state']
        d_name = request.form['d_name']

        middle_name = request.form['middle_name']
        aadhar_id = request.form['aadhar_id']
        voter_id = request.form['voter_id']
        pno = request.form['pno']
        age = int(request.form['age'])
        email = request.form['email']
        voters=pd.read_sql_query('SELECT * FROM assmvoters', mydb)
        all_aadhar_ids=voters.aadhar_id.values
        all_voter_ids=voters.voter_id.values
        if age >= 18:
            if (aadhar_id in all_aadhar_ids) or (voter_id in all_voter_ids):
                flash(r'Already Registered as a Voter')
            else:
                sql = 'INSERT INTO assmvoters (first_name, middle_name, last_name, aadhar_id, voter_id, email,pno,state,d_name, verified) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)'
                cur=mydb.cursor()
                cur.execute(sql, (first_name, middle_name, last_name, aadhar_id, voter_id, email, pno, state, d_name, 'no'))
                mydb.commit()
                cur.close()
                session['aadhar']=aadhar_id
                session['status']='no'
                session['email']=email
                return redirect(url_for('assmverify'))
        else:
            flash("if age less than 18 than not eligible for voting","info")
    return render_template('assmvoter_reg.html')

#---------------------------------------VOTER REGISTRATION----------------------------------------------------



#---------------------------------------------VERIFY----------------------------------------------------------
@app.route('/zptcverify', methods=['POST','GET'])
def zptcverify():
    if session['status']=='no':
        if request.method=='POST':
            otp_check=request.form['otp_check']
            if otp_check==session['otp']:
                session['status']='yes'
                sql="UPDATE zptcvoters SET verified='%s' WHERE aadhar_id='%s'"%(session['status'], session['aadhar'])
                cur=mydb.cursor()
                cur.execute(sql)
                mydb.commit()
                cur.close()
                flash(r"Email verified successfully",'primary')
                return redirect(url_for('capture_images')) #change it to capture photos
            else:
                flash(r"Wrong OTP. Please try again.","info")
                return redirect(url_for('zptcverify'))
        else:
            #Sending OTP
            message = MIMEMultipart()
            receiver_address = session['email']
            message['From'] = sender_address
            message['To'] = receiver_address
            Otp = str(np.random.randint(100000, 999999))
            session['otp']=Otp
            message.attach(MIMEText(session['otp'], 'plain'))
            abc = smtplib.SMTP('smtp.gmail.com', 587)
            abc.starttls()
            abc.login(sender_address, sender_password
)
            text = message.as_string()
            abc.sendmail(sender_address, receiver_address, text)
            abc.quit()
    else:
        flash(r"Your email is already verified", 'warning')
    return render_template('zptcverify.html')

@app.route('/mptcverify', methods=['POST','GET'])
def mptcverify():
    if session['status']=='no':
        if request.method=='POST':
            otp_check=request.form['otp_check']
            if otp_check==session['otp']:
                session['status']='yes'
                sql="UPDATE mptcvoters SET verified='%s' WHERE aadhar_id='%s'"%(session['status'], session['aadhar'])
                cur=mydb.cursor()
                cur.execute(sql)
                mydb.commit()
                cur.close()
                flash(r"Email verified successfully",'primary')
                return redirect(url_for('capture_images')) #change it to capture photos
            else:
                flash(r"Wrong OTP. Please try again.","info")
                return redirect(url_for('mptcverify'))
        else:
            #Sending OTP
            message = MIMEMultipart()
            receiver_address = session['email']
            message['From'] = sender_address
            message['To'] = receiver_address
            Otp = str(np.random.randint(100000, 999999))
            session['otp']=Otp
            message.attach(MIMEText(session['otp'], 'plain'))
            abc = smtplib.SMTP('smtp.gmail.com', 587)
            abc.starttls()
            abc.login(sender_address, sender_password
)
            text = message.as_string()
            abc.sendmail(sender_address, receiver_address, text)
            abc.quit()
    else:
        flash(r"Your email is already verified", 'warning')
    return render_template('mptcverify.html')

@app.route('/assmverify', methods=['POST','GET'])
def assmverify():
    if session['status']=='no':
        if request.method=='POST':
            otp_check=request.form['otp_check']
            if otp_check==session['otp']:
                session['status']='yes'
                sql="UPDATE assmvoters SET verified='%s' WHERE aadhar_id='%s'"%(session['status'], session['aadhar'])
                cur=mydb.cursor()
                cur.execute(sql)
                mydb.commit()
                cur.close()
                flash(r"Email verified successfully",'primary')
                return redirect(url_for('capture_images')) #change it to capture photos
            else:
                flash(r"Wrong OTP. Please try again.","info")
                return redirect(url_for('assmverify'))
        else:
            #Sending OTP
            message = MIMEMultipart()
            receiver_address = session['email']
            message['From'] = sender_address
            message['To'] = receiver_address
            Otp = str(np.random.randint(100000, 999999))
            session['otp']=Otp
            message.attach(MIMEText(session['otp'], 'plain'))
            abc = smtplib.SMTP('smtp.gmail.com', 587)
            abc.starttls()
            abc.login(sender_address, sender_password
)
            text = message.as_string()
            abc.sendmail(sender_address, receiver_address, text)
            abc.quit()
    else:
        flash(r"Your email is already verified", 'warning')
    return render_template('assmverify.html')


@app.route('/verify', methods=['POST','GET'])
def verify():
    if session['status']=='no':
        if request.method=='POST':
            otp_check=request.form['otp_check']
            if otp_check==session['otp']:
                session['status']='yes'
                sql="UPDATE voters SET verified='%s' WHERE aadhar_id='%s'"%(session['status'], session['aadhar'])
                cur=mydb.cursor()
                cur.execute(sql)
                mydb.commit()
                cur.close()
                flash(r"Email verified successfully",'primary')
                return redirect(url_for('capture_images')) #change it to capture photos
            else:
                flash(r"Wrong OTP. Please try again.","info")
                return redirect(url_for('verify'))
        else:
            #Sending OTP
            message = MIMEMultipart()
            receiver_address = session['email']
            message['From'] = sender_address
            message['To'] = receiver_address
            Otp = str(np.random.randint(100000, 999999))
            session['otp']=Otp
            additional_message = "This is otp for Voter Registratioon: "
            message.attach(MIMEText(additional_message, 'plain'))
            message.attach(MIMEText(session['otp'], 'plain'))
            abc = smtplib.SMTP('smtp.gmail.com', 587)
            abc.starttls()
            abc.login(sender_address, sender_password
)
            text = message.as_string()
            abc.sendmail(sender_address, receiver_address, text)
            abc.quit()
    else:
        flash(r"Your email is already verified", 'warning')
    return render_template('verify.html')

#--------------------------------------------------VERIFY---------------------------------------------------

@app.route('/capture_images', methods=['POST','GET'])
def capture_images():
    if request.method=='POST':
        cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        sampleNum = 0
        path_to_store=os.path.join(os.getcwd(),"all_images\\"+session['aadhar'])
        try:
            shutil.rmtree(path_to_store)
        except:
            pass
        os.makedirs(path_to_store, exist_ok=True)
        while (True):
            ret, img = cam.read()
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            except:
                continue
            faces = cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite(path_to_store +r'\\'+ str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
            else:
                cv2.imshow('frame', img)
                cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum >= 200:
                break
        cam.release()
        cv2.destroyAllWindows()
        flash("Registration is successfull","success")
        return redirect(url_for('home'))
    return render_template('capture.html')



#----------------------------------------------MODEL TRAINING-----------------------------------------------------

def getImagesAndLabels(path):
    folderPaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    global le
    for folder in folderPaths:
        imagePaths = [os.path.join(folder, f) for f in os.listdir(folder)]
        aadhar_id = folder.split("\\")[1]
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(aadhar_id)
            # Ids.append(int(aadhar_id))
    Ids_new=le.fit_transform(Ids).tolist()
    output = open('encoder.pkl', 'wb')
    pickle.dump(le, output)
    output.close()
    return faces, Ids_new

@app.route('/train', methods=['POST','GET'])
def train():
    if request.method=='POST':
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, Id = getImagesAndLabels(r"all_images")
        print(Id)
        print(len(Id))
        recognizer.train(faces, np.array(Id))
        recognizer.save("Trained.yml")
        flash(r"Model Trained Successfully", 'Primary')
        return redirect(url_for('home'))
    return render_template('train.html')

#----------------------------------------------MODEL TRAINING-----------------------------------------------------



#---------------------------------UPDATE VOTER DETAILS---------------------------------------------------

@app.route('/updateback', methods=['POST','GET'])
def updateback():
    if request.method=='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        aadhar_id = request.form['aadhar_id']
        voter_id = request.form['voter_id']
        email = request.form['email']
        pno = request.form['pno']
        age = int(request.form['age'])
        voters=pd.read_sql_query('SELECT * FROM voters', mydb)
        all_aadhar_ids=voters.aadhar_id.values
        if age >= 18:
            if (aadhar_id in all_aadhar_ids):
                sql="UPDATE VOTERS SET first_name='%s', middle_name='%s', last_name='%s', voter_id='%s', email='%s',pno='%s', verified='%s' where aadhar_id='%s'"%(first_name, middle_name, last_name, voter_id, email, 'no', aadhar_id)
                cur=mydb.cursor()
                cur.execute(sql, (first_name, middle_name, last_name, aadhar_id, voter_id, email,pno, 'no'))
                mydb.commit()
                cur.close()
                session['aadhar']=aadhar_id
                session['status']='no'
                session['email']=email
                flash(r'Database Updated Successfully','Primary')
                return redirect(url_for('verify'))
            else:
                flash(f"Aadhar: {aadhar_id} doesn't exists in the database for updation", 'warning')
        else:
            flash("age should be 18 or greater than 18 is eligible", "info")
    return render_template('update.html')



#---------------------------------UPDATE VOTER DETAILS---------------------------------------------------



#----------------------------------------------VOTE------------------------------------------------------------



@app.route('/zptcvotinghom', methods=['POST','GET'])
def zptcvotinghom():
    if request.method=='POST':
        pkl_file = open('encoder.pkl', 'rb')
        my_le = pickle.load(pkl_file)
        pkl_file.close()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(r"Trained.yml")
        cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_SIMPLEX
        flagss = 0
        det_aadhar = None
        while True:
            ret, im = cam.read()
            flags += 1
            if flags == 400:
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('zptcselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('zptcvotinghom.html')
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 80):
                    det_aadhar = my_le.inverse_transform([Id])[0]
                    cv2.putText(im, f"Aadhar: {det_aadhar}", (x, y + h), font, 1, (255, 255, 255), 2)
                else:
                    cv2.putText(im, "Unknown", (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('im', im)
            try:
                cv2.setWindowProperty('im', cv2.WND_PROP_TOPMOST, 1)
            except:
                pass
            if (cv2.waitKey(1) == (ord('q'))):
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('zptcselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('zptcvotinghom.html')
    return render_template('zptcvotinghom.html')


@app.route('/mptcvotinghom', methods=['POST','GET'])
def mptcvotinghom():
    if request.method=='POST':
        pkl_file = open('encoder.pkl', 'rb')
        my_le = pickle.load(pkl_file)
        pkl_file.close()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(r"Trained.yml")
        cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_SIMPLEX
        flags = 0
        det_aadhar = None
        while True:
            ret, im = cam.read()
            flags += 1
            if flags == 500:
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('mptcselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('mptcvotinghom.html')
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 80):
                    det_aadhar = my_le.inverse_transform([Id])[0]
                    cv2.putText(im, f"Aadhar: {det_aadhar}", (x, y + h), font, 1, (255, 255, 255), 2)
                else:
                    cv2.putText(im, "Unknown", (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('im', im)
            try:
                cv2.setWindowProperty('im', cv2.WND_PROP_TOPMOST, 1)
            except:
                pass
            if (cv2.waitKey(1) == (ord('q'))):
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('mptcselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('mptcvotinghom.html')
    return render_template('mptcvotinghom.html')


@app.route('/assmvotinghom', methods=['POST','GET'])
def assmvotinghom():
    if request.method=='POST':
        pkl_file = open('encoder.pkl', 'rb')
        my_le = pickle.load(pkl_file)
        pkl_file.close()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(r"Trained.yml")
        cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_SIMPLEX
        flags = 0
        det_aadhar = None
        while True:
            ret, im = cam.read()
            flags += 1
            if flags == 400:
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('assmselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('assmvotinghom.html')
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 80):
                    det_aadhar = my_le.inverse_transform([Id])[0]
                    cv2.putText(im, f"Aadhar: {det_aadhar}", (x, y + h), font, 1, (255, 255, 255), 2)
                else:
                    cv2.putText(im, "Unknown", (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('im', im)
            try:
                cv2.setWindowProperty('im', cv2.WND_PROP_TOPMOST, 1)
            except:
                pass
            if (cv2.waitKey(1) == (ord('q'))):
                cv2.destroyAllWindows()
                if det_aadhar:
                    session['select_aadhar'] = det_aadhar
                    return redirect(url_for('assmselect_candidate'))
                else:
                    flash(r"Unable to detect person. Contact help desk for manual voting", "info")
                    return render_template('assmvotinghom.html')
    return render_template('assmvotinghom.html')

@app.route('/zptcselect_candidate', methods=['POST','GET'])
def zptcselect_candidate():
    #extract all nominees
    aadhar = session['select_aadhar']

    df_nom=pd.read_sql_query('select * from zptcnomiee', mydb)
    all_nom=df_nom['symbol_name'].values
    sq = "select * from zptcvote"
    g = pd.read_sql_query(sq, mydb)
    all_adhar = g['aadhar'].values
    if aadhar in all_adhar:
        flash("You already voted", "warning")
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            vote = request.form.get('test')
            if not vote:
                flash("Please select a nominee before voting.", "warning")
                return redirect(url_for('zptcselect_candidate'))  # or the correct route for your page
    
            session['vote'] = vote
            sql = "INSERT INTO zptcvote (vote, aadhar) VALUES ('%s', '%s')" % (vote, aadhar)
            cur = mydb.cursor()
            cur.execute(sql)
            mydb.commit()
            cur.close()
            s = "select * from voters where aadhar_id='" + aadhar + "'"
            c = pd.read_sql_query(s, mydb)
            pno = str(c.values[0][7])
            name = str(c.values[0][1])
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            
            flash(r"Voted Successfully", 'Primary')
            return redirect(url_for('home'))
    return render_template('zptcselect_candidate.html', noms=sorted(all_nom))


@app.route('/mptcselect_candidate', methods=['POST','GET'])
def mptcselect_candidate():
    #extract all nominees
    aadhar = session['select_aadhar']

    df_nom=pd.read_sql_query('select * from mptcnomiee', mydb)
    all_nom=df_nom['symbol_name'].values
    sq = "select * from vote"
    g = pd.read_sql_query(sq, mydb)
    all_adhar = g['aadhar'].values
    if aadhar in all_adhar:
        flash("You already voted", "warning")
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            vote = request.form.get('test')
            if not vote:
                flash("Please select a nominee before voting.", "warning")
                return redirect(url_for('zptcselect_candidate'))  # or the correct route for your page
            session['vote'] = vote
            sql = "INSERT INTO mptcvote (vote, aadhar) VALUES ('%s', '%s')" % (vote, aadhar)
            cur = mydb.cursor()
            cur.execute(sql)
            mydb.commit()
            cur.close()
            s = "select * from voters where aadhar_id='" + aadhar + "'"
            c = pd.read_sql_query(s, mydb)
            pno = str(c.values[0][7])
            name = str(c.values[0][1])
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            
            flash(r"Voted Successfully", 'Primary')
            return redirect(url_for('home'))
    return render_template('mptcselect_candidate.html', noms=sorted(all_nom))



@app.route('/assmselect_candidate', methods=['POST','GET'])

def assmselect_candidate():
    #extract all nominees
    aadhar = session['select_aadhar']
    s=pd.read_sql_query("SELECT * FROM voters where aadhar_id='%s'" %aadhar, mydb)
    state = str(s['d_name'].values[0])
    df_nom=pd.read_sql_query("SELECT * FROM assemblynomiee where village='%s'" %state, mydb)
    all_nom=df_nom['symbol_name'].values
    sq = "select * from assmvote"
    g = pd.read_sql_query(sq, mydb)
    all_adhar = g['aadhar'].values
    if aadhar in all_adhar:
        flash("You already voted", "warning")
        return redirect(url_for('assmvotinghom'))
    else:
        if request.method == 'POST':
            vote = request.form.get('test')
            if not vote:
                flash("Please select a nominee before voting.", "warning")
                return redirect(url_for('zptcselect_candidate'))  # or the correct route for your page
            session['vote'] = vote
            sql = "INSERT INTO assmvote (vote, aadhar, village) VALUES ('%s', '%s','%s')" % (vote, aadhar,state)
            cur = mydb.cursor()
            cur.execute(sql)
            mydb.commit()
            cur.close()
            flash(r"Voted Successfully", 'Primary')
            return redirect(url_for('home'))

    return render_template('assmselect_candidate.html', noms=sorted(all_nom),village=state)
#---------------------------------------------select candidate------------------------------------------------

@app.route('/typeofeleresult')
def typeofeleresult():
    return render_template('typeofeleresult.html')



@app.route('/voting_res')
@app.route('/voting_res')
def voting_res():
    votes = pd.read_sql_query('select * from vote', mydb)
    counts = pd.DataFrame(votes['vote'].value_counts())
    counts.reset_index(inplace=True)
    all_imgs=['1.png','2.png','3.jpg','4.png','5.png','6.png']
    all_freqs=[counts[counts['vote']==i].iloc[0,1] if i in counts['vote'].values else 0 for i in all_imgs]
    df_nom=pd.read_sql_query('select * from nominee', mydb)
    all_nom=df_nom['symbol_name'].values
    return render_template('voting_res.html', freq=all_freqs, noms=all_nom)


@app.route('/zptc_result')
def zptc_result():
    votes = pd.read_sql_query('select * from zptcvote', mydb)
    counts = pd.DataFrame(votes['vote'].value_counts())
    counts.reset_index(inplace=True)
    # all_imgs=['1.png','2.png','3.jpg','4.png','5.png','6.png']
    all_imgs=['zptc1.jpg','zptc2.jpg','zptc3.jpg','zptc4.jpg','zptc5.jpg','zptc6.jpg']
    all_freqs=[counts[counts['vote']==i].iloc[0,1] if i in counts['vote'].values else 0 for i in all_imgs]

    df_nom=pd.read_sql_query('select * from zptcnomiee', mydb)
    all_nom=df_nom['symbol_name'].values
    return render_template('zptc_result.html', freq=all_freqs, noms=all_nom)


@app.route('/mptc_result')
def mptc_result():
    votes = pd.read_sql_query('select * from assmvote', mydb)
    counts = pd.DataFrame(votes['vote'].value_counts())
    counts.reset_index(inplace=True)
    # all_imgs=['1.png','2.png','3.jpg','4.png','5.png','6.png']
    all_imgs=['mlcp1.jpg','mlcp2.jpg','mlcp3.jpg','mlcp4.jpg','mlcp5.jpg','mlcp6,jpg']
    all_freqs=[counts[counts['vote']==i].iloc[0,1] if i in counts['vote'].values else 0 for i in all_imgs]
# ...existing code...
    df_nom=pd.read_sql_query('select * from mptcnomiee', mydb)
    all_nom=df_nom['symbol_name'].values
    return render_template('mptc_result.html', freq=all_freqs, noms=all_nom)

@app.route('/select_village', methods=['POST','GET'])
def select_village():
    if request.method=='POST':
        state = request.form['state']
        session['select']=state
        return redirect(url_for('assm_result'))

    return render_template('select_village.html',admin=session['IsAdmin'])


@app.route('/assm_result')
def assm_result():
    village=session['select']
    votes = pd.read_sql_query("select * from assmvote where village='%s'" %village, mydb)
    counts = pd.DataFrame(votes['vote'].value_counts())
    counts.reset_index(inplace=True)
    # all_imgs=['1.png','2.png','3.jpg','4.png','5.png','6.png']
    all_imgs=['assm1.jpg','assm1.jpg','assm3.jpg','assm4.jpg','assm5.jpg','assm6.jpg']
    all_freqs=[counts[counts['vote']==i].iloc[0,1] if i in counts['vote'].values else 0 for i in all_imgs]
# ...existing code...
    df_nom=pd.read_sql_query('select * from assemblynomiee', mydb)
    all_nom=df_nom['symbol_name'].values
    return render_template('assm_result.html', freq=all_freqs, noms=all_nom, village=village)



if __name__=='__main__':
    app.run(debug=True)

