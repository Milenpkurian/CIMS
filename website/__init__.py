from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from datetime import datetime,date,timedelta
from flask import Flask, render_template, request, redirect, url_for, session,flash
from os import path

dep = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    """Secret Key Generation"""
    import secrets
    secret_key = secrets.token_hex(16)
    # example output, secret_key = 000d88cd9d90036ebdd237eb6b0dep000
    app.config['SECRET_KEY'] = secret_key

    #SqlAlchemy Database Configuration With mysql
    dep_url="mysql+pymysql://root:root@localhost/dep"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{ dep_url }'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    dep.init_app(app)

    from .lviews import lviews
    from .hviews import hviews
    # from .aviews import aviews
    from .cviews import cviews


    app.register_blueprint(lviews,url_prefix='/lab')
    app.register_blueprint(hviews,url_prefix='/hod')
    # app.register_blueprint(aviews,url_prefix='/admin')
    app.register_blueprint(cviews,url_prefix='/common')


    from .models import Chemicals,Glasswares,Equipments

    with app.app_context():
        dep.create_all()



    """Information about users"""
    users = [
        {"id":1,"username":"admin","password": "admin"},
        {"id":2,"username":"hod","password": "hod"},
        {"id":3,"username":"lab","password": "lab"}
    ]

    @app.after_request
    def after_request(response):
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        return response

    @app.route('/')
    @app.route('/login', methods =['GET', 'POST'])
    def login():
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            
            account = next((user for user in users if user["username"]==username and user["password"]==password),None)
            if account:
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                print(session['username'])
                if session['username']=='lab':
                    return redirect(url_for('lviews.lab_assistant_panel'))
                if session['username']=='hod':
                    return redirect(url_for('hviews.hod_panel'))
                if session['username']=='admin':
                    return redirect(url_for('admin_panel'))
        return render_template('login.html')
    

    @app.route('/logout')
    def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)   
        return redirect(url_for('login'))



    return app