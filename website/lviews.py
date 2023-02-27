from flask import render_template, request, redirect, url_for, session,flash,Blueprint
from . import dep
from .models import Chemicals,Glasswares,Equipments,Req_lab
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, create_engine, text,func
from datetime import datetime,date,timedelta

lviews=Blueprint('lviews',__name__)

dep_url="mysql+pymysql://root:root@localhost/dep"
engine = create_engine(dep_url, pool_size=5, pool_recycle=3600)
conn = engine.connect()

@lviews.route('/')
def lab_assistant_panel():
    if session:
        sql_text = text("select item_name from dep.chemicals")
        nchemicals = conn.execute(sql_text)
        sql_text = text("select item_name from dep.glasswares")
        nglasswares = conn.execute(sql_text)
        sql_text = text("select item_name from dep.equipments")
        nequipments = conn.execute(sql_text)
        sql_text = text("select * from chemicals where expiry_date between curdate() AND (curdate()+interval 70 day) order by expiry_date limit 4")
        four_abt_expire = conn.execute(sql_text)
        sql_text = text("SELECT * FROM equipments where defective!=0 limit 4")
        defective4table = conn.execute(sql_text)        
        return render_template('/lab/lab_assistant.html',nchemicals=nchemicals.rowcount , nglasswares=nglasswares.rowcount , nequipments=nequipments.rowcount,four_abt_expire=four_abt_expire , defective4table=defective4table)
    else:
        return render_template('login.html')

#_________________________________CHEMICALS________________________________________
#This is the index route where we are going to
#query on all our chemicals data
@lviews.route('/crud_chemicals')
def Index_chemicals():
    all_data = Chemicals.query.all()

    return render_template("/lab/crud_chemicals/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@lviews.route('/insert_chemicals', methods = ['POST'])
def insert_chemicals():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        item_type = request.form['item_type']
        in_stock=request.form['in_stock']
        received_date=request.form['received_date']
        expiry_date=request.form['expiry_date']


        my_data = Chemicals(id, item_name, item_type , in_stock,received_date,expiry_date)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('lviews.Index_chemicals'))


#this is our update route where we are going to update our item
@lviews.route('/update_chemicals', methods = ['GET', 'POST'])
def update_chemicals():

    if request.method == 'POST':
        my_data = Chemicals.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.item_type = request.form['item_type']
        my_data.in_stock = request.form['in_stock']
        my_data.received_date = request.form['received_date']
        my_data.expiry_date = request.form['expiry_date']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('lviews.Index_chemicals'))




#This route is for deleting our item
@lviews.route('/delete_chemicals/<id>/', methods = ['GET', 'POST'])
def delete_chemicals(id):
    my_data = Chemicals.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('lviews.Index_chemicals'))

#about to expire
@lviews.route('/about_to_expire')
def about_to_expire():
    sql_text = text("select * from chemicals where expiry_date between curdate() AND (curdate()+interval 70 day) order by expiry_date")
    abt_expire = conn.execute(sql_text)
    return render_template('/lab/crud_chemicals/abt_expire.html',abt_expire=abt_expire)




#_________________________________GLASSWARES______________________________________

#This is the index route where we are going to
#query on all our glasswares data
@lviews.route('/crud_glasswares')
def Index_glasswares():
    all_data = Glasswares.query.all()

    return render_template("/lab/crud_glasswares/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@lviews.route('/insert_glasswares', methods = ['POST'])
def insert_glasswares():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        defective=request.form['defective']


        my_data = Glasswares(id, item_name, quantity , defective)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('lviews.Index_glasswares'))


#this is our update route where we are going to update our item
@lviews.route('/update_glasswares', methods = ['GET', 'POST'])
def update_glasswares():

    if request.method == 'POST':
        my_data = Glasswares.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.quantity = request.form['quantity']
        my_data.defective = request.form['defective']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('lviews.Index_glasswares'))




#This route is for deleting our item
@lviews.route('/delete_glasswares/<id>/', methods = ['GET', 'POST'])
def delete_glasswares(id):
    my_data = Glasswares.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('lviews.Index_glasswares'))


#_________________________________EQUIPMENTS______________________________________

#This is the index route where we are going to
#query on all our equipments data
@lviews.route('/crud_equipments')
def Index_equipments():
    all_data = Equipments.query.all()

    return render_template("/lab/crud_equipments/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@lviews.route('/insert_equipments', methods = ['POST'])
def insert_equipments():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        defective=request.form['defective']


        my_data = Equipments(id, item_name, quantity , defective)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('lviews.Index_equipments'))


#this is our update route where we are going to update our item
@lviews.route('/update_equipments', methods = ['GET', 'POST'])
def update_equipments():

    if request.method == 'POST':
        my_data = Equipments.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.quantity = request.form['quantity']
        my_data.defective = request.form['defective']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('lviews.Index_equipments'))




#This route is for deleting our item
@lviews.route('/delete_equipments/<id>/', methods = ['GET', 'POST'])
def delete_equipments(id):
    my_data = Equipments.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('lviews.Index_equipments'))

#defective
@lviews.route('/defective')
def defective_equipments():
    sql_text = text("SELECT * FROM equipments where defective!=0")
    defective = conn.execute(sql_text)   
    return render_template('/lab/crud_equipments/defective_equipments.html',defective=defective)