'''
Created on 2018. 8. 21.

@author: cskim

Modified in 2020.11.22.

@author: Young-Jun Park
'''
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

import dbconfig
from dbhelper import DBHelper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x6vGZrpUtoMGo+T+uFrkxQ9DLh7F8qSM'

DB = DBHelper()

@app.route("/", methods=['GET','POST'])
def home():
        
    if request.method == 'POST':
        gubun = request.form.get('gubun')
        grade = request.form.get('grade')
        stu_dept = request.form.get('stu_dept')
        stu_name = request.form.get('stu_name')
        queryObj = {'gubun':gubun, 'grade': grade, 'stu_dept':stu_dept, 'stu_name':stu_name}
        print ('queryObj=', queryObj)        
        session['queryObj'] = queryObj
        return redirect(url_for('home'))

    home_param = None
    if session.get('queryObj'):
        home_param = session.get('queryObj')
    
    # 기본 설정이 안되어 있는 전공으로 check
    if home_param.get('stu_dept') == None:
        session.clear()
        return render_template("home.html")    

    return render_template("home.html", home_param=home_param)

@app.route("/listprice", methods=['GET','POST'])
def listprice():
    #
    if request.method == 'POST':
        jm_code = request.form.get('jm_code')
        jm_name = request.form.get('jm_name')
        start_day = request.form.get('start_day')
        end_day = request.form.get('end_day')
        query_limit = request.form.get('limit')
        queryObj = {'jm_code':jm_code, 'jm_name':jm_name, 'start_day':start_day, 'end_day':end_day, 'limit':query_limit}
        print ('queryObj=', queryObj)        
        session['queryObj'] = queryObj
        return redirect(url_for('listprice'))
    
    price_param = None
    price_list = None
    if session.get('queryObj'):
        price_param = session.get('queryObj')
        print ('price_param=', price_param)  
        price_list = DB.getPriceByQuery(queryObj=price_param)
        
    if price_list == None:
        price_list=DB.get_n_price(lim=100)
    # print len(price_list)
    return render_template("list_price_tab.html", price_param=price_param, price_list=price_list)

if __name__ == '__main__':
    app.run(port=5005, debug=True)
