from flask import Flask,app,jsonify,url_for, render_template, request
import pandas as pd
app=Flask(__name__)
@app.route("/")
def fun1():
    return render_template("info.html")
@app.route("/show",methods = ["post"])
def home():
   # nm = request.form['name']
    reg_id = int(request.form['reg_id'])
    #sheet_id1='1H-rkyHggDJJI-QNh5SgG9u4zzQCEiow79mCMY_8I9CI'
   
    #df = pd.concat(map(pd.read_csv,[f"https://docs.google.com/spreadsheets/d/{sheet_id1}/export?format=csv"]))
    #df = pd.read_csv("mockdata.csv")
    #result1 = df[df['Registration id'] == reg_id ]
    #return result1.to_html()
    

    df = pd.read_csv("mockdata.csv")
    result1 = df[df['Registration id'] ==reg_id]    
    return '<h1> Welcome, Your Mock Interview Scores are as follows</h1><br/>'+result1.to_html() 
    
    
    
    #def do_lower(name):
        #return name.lower()

    #df['Student Name']=df["Student Name"].apply(do_lower)
    #result1 = df[df['Registration id'] ==reg_id]
    #name = nm.lower()
    #result2 = result1[result1["Student Name"].str.contains(name)]
      
    #return '<h1> Welcome {}, Your Mock Interview Scores are as follows</h1>'.format(name)+"<br/>"+result2.to_html()+"<br/><br/> If you have provided correct name then infomation will display otherwise not" 
        
if __name__ == "__main__":
    app.run(debug=True)





