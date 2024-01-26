import pickle
import flask 
from flask import *
import pandas as pd
import numpy as np

#load saved model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__,template_folder='template')
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    result = []
    result.append(float(pd.Series(request.form["gender"]).replace({"male":1, "female":2}).values))
    result.append(float(request.form["age"]))
    result.append(float(pd.Series(request.form["hypertension"]).replace({"yes":1, "no":0}).values))
    result.append(float(pd.Series(request.form["heart"]).replace({"yes":1, "no":0}).values))
    result.append(float(pd.Series(request.form["married"]).replace({"yes":1, "no":0}).values))
    result.append(float(pd.Series(request.form["worktype"]).replace({"private":2, "self employee":3, "govt job":0, "childer":4, "never":1}).values))
    result.append(float(pd.Series(request.form["residence"]).replace({"urban":1, "rural":0}).values))
    result.append(float(request.form["glucose"]))
    result.append(float(request.form["bmi"]))
    result.append(float(pd.Series(request.form["smoke"]).replace({'formerly smoker':1, 'never smoker':2, 'smokes':3}).values))
    values = np.array([result])
    pred = model.predict(values)
    print(pred)
    if int(pred) == 0:
        pred = "You Have Not Identified Stroke"
    else:
        pred = "You Identified Stroke"
    return render_template('index.html', prediction_text='{}'.format(pred))
    
if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
