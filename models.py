from email.headerregistry import Address
from db import db


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    eq = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String, nullable=False)
    fathername = db.Column(db.String, nullable=False)
    mothername = db.Column(db.String, nullable=False)
    guardian = db.Column(db.String, nullable=True)
    mno = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=True)
    dob = db.Column(db.Text, nullable=False)
    aadhar = db.Column(db.Integer, unique=True, nullable=False)
    district = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    img = db.Column(db.Text, unique=True, nullable=False)
    sig = db.Column(db.Text, unique=True, nullable=False)

class veInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carname = db.Column(db.String, nullable=False)
    AofO = db.Column(db.String, nullable=False)
    Vt = db.Column(db.String, nullable=False)
    Mv = db.Column(db.String, nullable=False)
    Mn = db.Column(db.String, nullable=False)
    yom = db.Column(db.Text, nullable=False)
    yofm = db.Column(db.String, nullable=False)
    nofc = db.Column(db.String, nullable=False)
    Sc = db.Column(db.String, nullable=False)
    Hp = db.Column(db.String, nullable=False)
    Fe = db.Column(db.String, nullable=True)
    cofb = db.Column(db.Integer, nullable=False)
    vwbm = db.Column(db.String, nullable=True)
    vwtr = db.Column(db.Text, nullable=False)
    carimg = db.Column(db.Text, unique=True, nullable=False)