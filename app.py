from flask import Flask,app,jsonify,url_for, render_template, request
import pandas as pd
app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")
 
@app.route("/show",methods = ["post"])
def home():
    nm = request.form['name']
    reg_id = int(request.form['reg_id'])
    sheet_id1='11LNkA1BML-sOJF65XBHSYMV9-s8AVeJhoy-rhgOUfLY'
    sheet_id2 = '1aJFuKyLaZRdWZ-S81T1CylFOOsvZDbVRlvg-pVHTO50'
    df = pd.concat(map(pd.read_csv,[f"https://docs.google.com/spreadsheets/d/{sheet_id1}/export?format=csv", f"https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv"]))
    result1 = df[df['Registration id'] ==reg_id ]
    return result1.to_html()
    
if __name__ == "__main__":
    app.run(debug=True)





