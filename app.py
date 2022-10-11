from flask import Flask,app,jsonify,url_for, render_template, request
import pandas as pd
app=Flask(__name__)
@app.route("/")
def fun1():
    return render_template("info.html")
@app.route("/show",methods = ["post"])
def home():
    nm = request.form['name']
    reg_id = request.form['reg_id']
    #sheet_id1='1H-rkyHggDJJI-QNh5SgG9u4zzQCEiow79mCMY_8I9CI'
   
    #df = pd.concat(map(pd.read_csv,[f"https://docs.google.com/spreadsheets/d/{sheet_id1}/export?format=csv"]))
    df = pd.read_csv("mockdata.csv")
    result1 = df[df['Registration id'] ==reg_id ]
    return result1.to_html()
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8888')





