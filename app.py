from audioop import add
from fileinput import filename
from flask import Flask,redirect,render_template,url_for,request,g,session
from werkzeug.utils import secure_filename
from db import db_init, db
from models import Info, veInfo
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/DELL/Desktop/RTO/static/image'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'somesecretkeythatonlyishouldknow'
db_init(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/image/<filename>')
def get(filename):
    return os.path.join(app.config['UPLOAD_FOLDER'], filename)

@app.route("/admin/driving licence log",methods=['GET','POST'])
def admin():
    file_url= url_for('get', filename=Info.img)
    allUsers = Info.query.all()
    return render_template('admin.html', allUsers=allUsers, file_url=file_url)

@app.route("/admin/vehicle registration log",methods=['GET','POST'])
def admin1():
    file_url= url_for('get', filename=veInfo.carimg)
    allUsers = veInfo.query.all()
    return render_template('admin1.html', allUsers=allUsers, file_url=file_url)

@app.route("/registration", methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        fname = request.form['FName']
        lname = request.form['LName']
        dob = request.form['Dob']
        aadhar = request.form['Aadhar']
        eq = request.form['Educational Qualification']
        mobile = request.form['Mobile number']
        email = request.form['Email']
        city = request.form['City']
        gender = request.form['Gender']
        fathername = request.form['Father']
        mothername = request.form['Mother']
        guardian = request.form['Guardian']
        address = request.form['Address']
        district = request.form['District']
        pic1 = request.files['pic1']
        pic2 = request.files['pic2']
        file1 = secure_filename(pic1.filename)
        pic1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1))
        file2 = secure_filename(pic2.filename)
        pic2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2))
        user = Info(fname=fname,lname=lname,dob=dob,eq=eq,mno=mobile,address=address,email=email,gender=gender,aadhar=aadhar,district=district,fathername=fathername,mothername=mothername,guardian=guardian,city=city,img=file1,sig=file2)
        db.session.add(user)
        db.session.commit()
    return render_template('registration.html')

@app.route("/vehicle", methods=['GET','POST'])
def vehicle_reg():
    if request.method == 'POST':
        vehiclename = request.form['Owner']
        AofO = request.form['Owner Age']
        Vt = request.form['Vehicle type']
        Mv = request.form['Motor vehicle']
        Mn = request.form['Maker']
        yom = request.form['Year']
        yofm = request.form['number of cylinders']
        nofc = request.form['Seating']
        Sc = request.form['Energy']
        Hp = request.form['Fuel']
        Fe = request.form['Colour']
        cofb = request.form['Registration number']
        vwbm = request.form['weight by manufacturer']
        vwtr = request.form['weight to registered']
        
        carimg = request.files['Car image']
        carfile = secure_filename(carimg.filename)
        carimg.save(os.path.join(app.config['UPLOAD_FOLDER'], carfile))
        vehicle = veInfo(carname=vehiclename,AofO=AofO,Vt=Vt,Mv=Mv,Mn=Mn,yom=yom,yofm=yofm,nofc=nofc,Sc=Sc,Hp=Hp,Fe=Fe,cofb=cofb,vwbm=vwbm,vwtr=vwtr,carimg=carfile)
        db.session.add(vehicle)
        db.session.commit()
    return render_template('vehicle_registration.html')

@app.route('/delete/<int:id>')
def deleteV(id):
    user = veInfo.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/vehicle")

@app.route('/delete/<int:id>')
def delete(id):
    user = Info.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('admin.html')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        fname = request.form['FName']
        lname = request.form['LName']
        dob = request.form['Dob']
        aadhar = request.form['Aadhar']
        eq = request.form['Educational Qualification']
        mobile = request.form['Mobile number']
        email = request.form['Email']
        city = request.form['City']
        gender = request.form['Gender']
        fathername = request.form['Father']
        mothername = request.form['Mother']
        guardian = request.form['Guardian']
        address = request.form['Address']
        district = request.form['District']
        pic1 = request.files['pic1']
        pic2 = request.files['pic2']
        file1 = secure_filename(pic1.filename)
        file2 = secure_filename(pic2.filename)
        user = Info(fname=fname,lname=lname,dob=dob,eq=eq,mno=mobile,address=address,email=email,gender=gender,aadhar=aadhar,district=district,fathername=fathername,mothername=mothername,guardian=guardian,city=city,img=file1,sig=file2)
        user.FName = fname
        user.FName = lname
        user.Dob = dob
        user.Aadhar = aadhar
        user.EducationalQualification = eq
        user.Mobilenumber = mobile
        user.Email = email
        user.City = city
        user.Gender = gender 
        user.Father = fathername  
        user.Mother = mothername  
        user.Guardian = guardian 
        user.Address = address  
        user.District = district
        delete(id)
        db.session.add(user)
        db.session.commit()
        return redirect('admin.html')
    user = Info.query.filter_by(id=id).first()
    return render_template('update.html', user=user)

#admin
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('Registered'))

        return redirect(url_for('login'))

    return render_template('login.html')

#nav_bar setup
@app.route("/")
def Home():
    return render_template('Home.html')

@app.route("/about_us")
def About_us():
    return render_template('About_us.html')

@app.route("/contect")
def Contect():
    return render_template('contect.html')

@app.route("/licence")
def Licence():
    return render_template('licence_1.html')

@app.route("/licence/FORM-2.pdf")
def DLForm():
    return redirect("https://auto.economictimes.indiatimes.com/tag/rto", code=302)

@app.route("/CNG Maker")
def CNG():
    return render_template('cng.html')

@app.route("/Homologation")
def Homologation():
    return render_template('Homologation.html')

@app.route("/registered")
def Registered():
    return render_template('registered.html')

@app.route("/registration/learning licence")
def Ll():
    return render_template('learning_licence.html')

@app.route("/registration/driving licence renewal")
def dlr():
    return render_template('dl_renewal.html')

@app.route("/registration/duplicate driving licence")
def Ddl():
    return render_template('duplicate_dl.html')

if __name__ == "__main__":
    app.run(debug=True)