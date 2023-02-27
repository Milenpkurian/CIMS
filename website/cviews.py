from flask import render_template, request, redirect, url_for, session,flash,Blueprint
from . import dep
from .models import Chemicals,Glasswares,Equipments,Req_lab
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, create_engine, text,func
from datetime import datetime,date,timedelta
import re

cviews=Blueprint('cviews',__name__)

dep_url="mysql+pymysql://root:root@localhost/dep"
engine = create_engine(dep_url, pool_size=5, pool_recycle=3600)
conn = engine.connect()

@cviews.route('/')
def req_lab():
    all_data = Req_lab.query.all()
    if session['username']=='hod':
        return render_template('req_lab.html',items=all_data)
    elif session['username']=='lab':
        return render_template('req_lab.html',items=all_data)
    else:
        return "<h1>Else Req_lab</h1>"

@cviews.route('/make_request',methods=['POST'])
def lab_make_req():
    if request.method=='POST':
        id = request.form['id']
        item_name = request.form['item_name']
        item_type = request.form['item_type']
        req_qty=request.form['req_qty']
        req_qty=int(re.search(r'\d+', req_qty).group())
        need_for=request.form['need_for']

        sql_text=text(f'select * from req_lab where id=\'{id}\'')
        row=conn.execute(sql_text)

        if row.id==id and row.item_name==item_name and row.item_type==item_type and int(re.search(r'\d+', row.req_qty).group())>=req_qty :
            return "less"


        return "<h1>Requeted</h1>"

@cviews.route('/insert_request',methods=['POST'])
def insert_request():
    return None