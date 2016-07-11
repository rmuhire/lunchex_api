from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import unittest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lunchex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class LunchexUser(db.Model):
    lxu_id = db.Column(db.Integer, primary_key = True)
    lxu_fullname = db.Column(db.String(120))
    lxu_dob = db.Column(db.DateTime)
    lxu_username = db.Column(db.String(80), unique = True)
    lxu_password = db.Column(db.String(40))
    lxu_email = db.Column(db.String(120), unique = True)
    lxu_phone = db.Column(db.String(25))
    lxu_regDate = db.Column(db.DateTime)


    def __init__(self, lxu_fullname, lxu_dob, lxu_username, lxu_password, lxu_email, lxu_phone, lxu_regDate = None):
        self.lxu_fullname = lxu_fullname
        self.lxu_dob = lxu_dob
        self.lxu_username = lxu_username
        self.lxu_password = lxu_password
        self.lxu_email = lxu_email
        self.lxu_phone = lxu_phone

        if lxu_regDate is None:
            lxu_regDate = datetime.utcnow()

        self.lxu_regDate = lxu_regDate

    def __repr__(self):
        return '<LunchexUser %r>' % self.lxu_username


class LunchexGroup(db.Model):
    lxg_id = db.Column(db.Integer, primary_key = True)
    lxg_name = db.Column(db.String(80))
    lxg_menber = db.column(db.Text)
    lgx_admin = db.Column(db.Text)
    lxg_regDate = db.Column(db.DateTime)

    def __init__(self, lxg_id, lxg_name, lxg_menber, lgx_admin, lxg_regDate = None):
        self.lxg_id = lxg_id
        self.lxg_name = lxg_name,
        self.lxg_menber = lxg_menber
        self.lgx_admin = lgx_admin,

        if lxg_regDate is None:
            lxg_regDate = datetime.utcnow()

        self.lxg_regDate = lxg_regDate

    def __repr__(self):
        return '<LunchexGroup %r>' % self.lxg_name


class LunchexMenu(db.Model):
    lxm_id = db.Column(db.Integer, primary_key = True)
    lxm_name = db.Column(db.String(80))
    lxm_listItem = db.Column(db.Text)
    lxm_img = db.Column(db.String(30))
    lxm_regDate = db.Column(db.DateTime)

    def __init__(self, lxm_id, lxm_name, lxm_listItem, lxm_img, lxm_regDate = None):
        self.lxm_id = lxm_id
        self.lxm_name = lxm_name
        self.lxm_listItem = lxm_listItem
        self.lxm_img = lxm_img

        if lxm_regDate is None:
            lxm_regDate = datetime.utcnow()

        self.lxm_regDate = lxm_regDate


    def __repr__(self):
        return '<LunchexMenu %r>' % self.lxm_name


class LunchexShared(db.Model):
    lxs_id = db.Column(db.Integer, primary_key = True)
    lxs_lunchTime = db.Column(db.DateTime)
    lxs_participant = db.Column(db.Text)
    lxs_regDate = db.Column(db.DateTime)

    groupe_id = db.Column(db.Integer)
    menu_id = db.Column(db.Integer)



    def __init__(self, lxs_id, lxs_lunchTime, lxs_participant, groupe_id, menu_id, lxs_regDate = None):
        self.lxs_id = lxs_id
        self.lxs_lunchTime = lxs_lunchTime
        self.lxs_participant = lxs_participant

        if lxs_regDate is None:
            lxs_regDate = datetime.utcnow()

        self.lxs_regDate = lxs_regDate
        self.groupe_id = groupe_id
        self.menu_id = menu_id

    def __repr__(self):
        return '<LunchexShared %r>' % self.lxs_lunchTime


class LunchexItem(db.Model):
    lxi_id = db.Column(db.Integer, primary_key = True)
    lxi_name = db.Column(db.String(100))
    lxi_regDate = db.Column(db.DateTime)

    def __init__(self, lxi_id, lxi_name, lxi_regDate):
        self.lxi_id = lxi_id
        self.lxi_name = lxi_name

        if lxi_regDate is None:
            lxi_regDate = datetime.utcnow()

        self.lxi_regDate = lxi_regDate

    def __repr__(self):
        return '<LunchexShared %r>' % self.lxi_name



