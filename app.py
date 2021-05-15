
from flask import Flask, render_template, request
import json
from datetime import datetime


f=open('userdata.json',)
data=json.load(f)


app = Flask(__name__)

@app.route('/')
def home():
    
    id=[]
    for i in data['profile']:
        id.append(i)
    return render_template('index.html',id=id)



@app.route('/profile',methods=['POST'])
def profile():
    uid=request.form.get('uid')
    
    return render_template('profile.html',data=[data['profile'][uid],uid])


@app.route('/update',methods=['POST'])
def update():
    id=[]
    for i in data['profile']:
        id.append(i)
    write=open('userdata.json','w')
    
    
    uid=request.form.get('uid')
    now = datetime.now()
     
    #Update
    data['profile'][uid]['user']['name']['first']=request.form.get('fname')
    data['profile'][uid]['user']['name']['last']=request.form.get('lname')
    data['profile'][uid]['user']['name']['short']=request.form.get('sname')
    data['profile'][uid]['user']['name']['title']=request.form.get('title')
    
    data['profile'][uid]['user']['email']=request.form.get('email')
    data['profile'][uid]['user']['contact']=request.form.get('cnum')
    data['profile'][uid]['user']['contact-ext']=request.form.get('cext')
    data['profile'][uid]['user']['join-date']=request.form.get('jdate')
    
    data['profile'][uid]['team']=request.form.get('team')
    data['profile'][uid]['job-title']=request.form.get('jtitle')
    data['profile'][uid]['last-login']['datetime']=now.strftime("%Y-%d-%m %H:%M:%S")
    
    
    
    json.dump(data, write)
    
    
    write.close()
    return render_template('index.html',id=id)


@app.route('/back',methods=['POST'])
def back():
    
    
    id=[]
    for i in data['profile']:
        id.append(i)
    return render_template('index.html',id=id)


f.close()    
    
if __name__ == "__main__":
    app.run()
