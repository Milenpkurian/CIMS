from flask import render_template, request, redirect, url_for, session,flash,Blueprint
from . import dep
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, create_engine, text,func
from datetime import datetime,date,timedelta

from .models import Furniture,Electronics,Computers,Chemicals,Glasswares,Equipments,Req_lab

hviews=Blueprint('hviews',__name__)

dep_url="mysql+pymysql://root:root@localhost/dep"
engine = create_engine(dep_url, pool_size=5, pool_recycle=3600)
conn = engine.connect()


@hviews.route('/')
def hod_panel():
    if session:

        #No Lab Items
        sql_text = text("select item_name from dep.chemicals")
        nchemicals = conn.execute(sql_text)
        sql_text = text("select item_name from dep.glasswares")
        nglasswares = conn.execute(sql_text)
        sql_text = text("select item_name from dep.equipments")
        nequipments = conn.execute(sql_text)
        nLabItems=nchemicals.rowcount +  nchemicals.rowcount + nequipments.rowcount

        #No of Furniture
        sql_text = text("select quantity from dep.furniture")
        nfurniture=conn.execute(sql_text)
        fsum=0
        for row in nfurniture:
            fsum+=int(row.quantity)

        #No of Electronics
        sql_text = text("select quantity from dep.electronics")
        nelectronics=conn.execute(sql_text)
        esum=0
        for row in nelectronics:
            esum+=int(row.quantity)

        #No of Computers
        sql_text = text("select quantity from dep.computers")
        ncomputers=conn.execute(sql_text)
        csum=0
        for row in ncomputers:
            csum+=int(row.quantity)

        #defective
        sql_text = text("(SELECT * from computers WHERE defective!='0' UNION ALL SELECT * from electronics WHERE defective!='0' UNION ALL SELECT * from equipments WHERE defective!='0' UNION ALL SELECT * from furniture WHERE defective!='0' UNION ALL SELECT * from glasswares WHERE defective!='0') limit 4")
        defective = conn.execute(sql_text)

        return render_template('/hod/hod.html',nLabItems=nLabItems,nfurniture=fsum ,nelectronics=esum, ncomputers=csum,defective=defective)
    else:
        return render_template('login.html')


#_________________________________FURNITURE______________________________________

#This is the index route where we are going to
#query on all our furniture data
@hviews.route('/crud_furniture')
def Index_furniture():
    all_data = Furniture.query.all()

    return render_template("/hod/crud_furniture/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@hviews.route('/insert_furniture', methods = ['POST'])
def insert_furniture():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        defective=request.form['defective']


        my_data = Furniture(id, item_name, quantity , defective)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('hviews.Index_furniture'))


#this is our update route where we are going to update our item
@hviews.route('/update_furniture', methods = ['GET', 'POST'])
def update_furniture():

    if request.method == 'POST':
        my_data = Furniture.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.quantity = request.form['quantity']
        my_data.defective = request.form['defective']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('hviews.Index_furniture'))




#This route is for deleting our item
@hviews.route('/delete_furniture/<id>/', methods = ['GET', 'POST'])
def delete_furniture(id):
    my_data = Furniture.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('hviews.Index_furniture'))


#_________________________________ELECTRONICS______________________________________

#This is the index route where we are going to
#query on all our electronics data
@hviews.route('/crud_electronics')
def Index_electronics():
    all_data = Electronics.query.all()

    return render_template("/hod/crud_electronics/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@hviews.route('/insert_electronics', methods = ['POST'])
def insert_electronics():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        defective=request.form['defective']


        my_data = Electronics(id, item_name, quantity , defective)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('hviews.Index_electronics'))


#this is our update route where we are going to update our item
@hviews.route('/update_electronics', methods = ['GET', 'POST'])
def update_electronics():

    if request.method == 'POST':
        my_data = Electronics.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.quantity = request.form['quantity']
        my_data.defective = request.form['defective']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('hviews.Index_electronics'))




#This route is for deleting our item
@hviews.route('/delete_electronics/<id>/', methods = ['GET', 'POST'])
def delete_electronics(id):
    my_data = Electronics.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('hviews.Index_electronics'))


#_________________________________COMPUTERS______________________________________

#This is the index route where we are going to
#query on all our computers data
@hviews.route('/crud_computers')
def Index_computers():
    all_data = Computers.query.all()

    return render_template("/hod/crud_computers/index.html", items = all_data)



#this route is for inserting data to sqlite database via html forms
@hviews.route('/insert_computers', methods = ['POST'])
def insert_computers():

    if request.method == 'POST':

        id = request.form['id']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        defective=request.form['defective']


        my_data = Computers(id, item_name, quantity , defective)
        dep.session.add(my_data)
        try:
            dep.session.commit()
            flash("Item Inserted Successfully")
        except exc.SQLAlchemyError:
            flash("exc.SQLAlchemyError")

        return redirect(url_for('hviews.Index_computers'))


#this is our update route where we are going to update our item
@hviews.route('/update_computers', methods = ['GET', 'POST'])
def update_computers():

    if request.method == 'POST':
        my_data = Computers.query.get(request.form.get('id'))

        my_data.id=request.form['id']
        my_data.item_name = request.form['item_name']
        my_data.quantity = request.form['quantity']
        my_data.defective = request.form['defective']

        dep.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('hviews.Index_computers'))




#This route is for deleting our item
@hviews.route('/delete_computers/<id>/', methods = ['GET', 'POST'])
def delete_computers(id):
    my_data = Computers.query.get(id)
    dep.session.delete(my_data)
    dep.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('hviews.Index_computers'))

#defective
@hviews.route('/defective')
def defective():
    sql_text = text("SELECT * from computers WHERE defective!='0' UNION ALL SELECT * from electronics WHERE defective!='0' UNION ALL SELECT * from equipments WHERE defective!='0' UNION ALL SELECT * from furniture WHERE defective!='0' UNION ALL SELECT * from glasswares WHERE defective!='0'")
    defective = conn.execute(sql_text)   
    return render_template('/hod/defective.html',defective=defective)