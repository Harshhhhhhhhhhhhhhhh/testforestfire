import pickle
from flask import Flask,jsonify,request,render_template
import pandas as pd
import numpy

application = Flask(__name__)

app = application

ridge_model = pickle.load(open('Models/ridge_model.pkl','rb'))
standar_scaler = pickle.load(open('Models/scaler.pkl','rb'))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_data():
    if request.method == 'POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_data_scaled = standar_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)
        
        return render_template('predict.html',result =result[0])
    else:
        return render_template('predict.html')
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)    
    
   