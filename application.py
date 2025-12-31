from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



application = Flask(__name__)
app = application

## import ridge regresson and standardscaler pickle

ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open("models/scaler.pkl",'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods = ['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        temp = float(request.form["temperature"])
        rh = float(request.form["rh"])
        wind = float(request.form["wind"])
        rain = float(request.form["rain"])
        ffmc = float(request.form["ffmc"])
        dmc = float(request.form["dmc"])
        dc = float(request.form["dc"])
        isi = float(request.form["isi"])
        classes = float(request.form["classes"])

        new_data_scaled = standard_scaler.transform([[temp,rh,wind,rain,ffmc,dmc,dc,isi,classesgit  ]])
        prediction = round(ridge_model.predict(new_data_scaled)[0],2)

        return render_template("home.html",prediction = prediction)
    
    else:
        return render_template('home.html')
    



if __name__ == "__main__":
    app.run(host = "0.0.0.0")