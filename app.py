from flask import Flask,jsonify,request,render_template,url_for,redirect
import pickle
import pandas as pd
import numpy as np
import joblib
import pandas as pd

data = pd.read_csv("Model/Data.csv")
data.index = range(0,1960)

cs = joblib.load("Model/Cosine")

app = Flask(__name__,template_folder="templates",static_folder="static")

# Load the machine learning model
with open("Model/RealERstateAnalysisModel.pkl", 'rb') as file:
    model1 = pickle.load(file)

# Dummy labels, replace it with your actual labels if available
# ith open("Model/labels.pkl","rb") as file:
#     label1 = pickle.load(file)w

@app.route("/")
def home():
    return render_template('./index.html')


@app.route("/predict", methods=["POST"])
def prediction1():
    data  = [int(x) for x in request.form.values()]
    prediction = model1.predict(np.array([data]))
    return render_template("index-1.html", result=prediction[0])


@app.route("/api/predict", methods=["POST"])
def predict1():
    try:
        # Get data from the POST request
        data = request.get_json()


        
        # Extract features from the received data
        deal_satisfaction = data["deal-statisfaction"]
        property_type = data["property_type"]
        area = data["area"]
        sale_month = data["sale_month"]
        sale_weekday = data["sale_weekday"]
        birth_month = data["birth_month"]
        birth_year = data["birth_year"]  # No transformation needed
        birth_weekday = data["birth_weekday"]
        age = data["age"]

        # Make prediction using the model
        prediction = model1.predict(pd.DataFrame([[deal_satisfaction, property_type, area, sale_month, sale_weekday,
                                     birth_month, birth_year, birth_weekday, age]]))

        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction[0]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

model2 = joblib.load("Model/Model - Insta Analysis")

@app.route("/api/predict2", methods=["POST"])
def predict2():
    try:
        # Get data from the POST request
        data = request.get_json()
        # Extract features from the received data
        fromhome = data['From Home']
        fromhastag = data['From Hashtags']
        fromexplore = data['From Explore']
        fromother = data['From Other']
        saves = data['Saves']
        comments = data['Comments']
        shares = data['Shares']  # No transformation needed
        likes = data['Likes']
        visits = data['Profile Visits']
        follows = data['Follows']

        # Make prediction using the model
        prediction = model2.predict(pd.DataFrame([[fromhome,fromhastag,fromexplore,fromother,saves,comments,shares,likes,visits,follows]]))

        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction[0]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/api/predict3",methods=["POST"])
def recommended_system():
    try:
        inputs = str(request.get_json()["Content"]).lower()
        ind = []
        for i in range(0,1960):
            if inputs in data.iloc[i,:]["content"]:
                ind.append(i)
        similarity_scores = list(enumerate(cs[ind[0]]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        i = 0
        result =[]
        for col in similarity_scores:
            
            result.append(data[data.index==col[0]][["Title","Image","Link","Votes","Views"]].values[0])
            i += 1
            if i >6:
                break
        return jsonify({"Result":{
        "Title":[result[0][0],result[1][0],result[2][0],result[3][0],result[4][0],result[5][0]],
        "Image":[result[0][1],result[1][1],result[2][1],result[3][1],result[4][1],result[5][1]],
        "Link": [result[0][2],result[1][2],result[2][2],result[3][2],result[4][2],result[5][2]],
        "Votes": [result[0][3],result[1][3],result[2][3],result[3][3],result[4][3],result[5][3]],
        "Views": [result[0][4],result[1][4],result[2][4],result[3][4],result[4][4],result[5][4]]
    }
    }),200
    except:
        return jsonify({"error": str(f"{inputs} Not Found")})
    
# model-4
from sklearn.preprocessing import LabelEncoder
label = joblib.load("Model/Country")
model4 = joblib.load("Model/Classification")
    
@app.route("/api/predict4",methods=["POST"])
def predict4():
    try:
        # Get data from the POST request
        data = request.get_json()
        # Extract features from the received data
        country= data['country']
        Country = label.transform([country])
        days_on_platform = data['days_on_platform']
        minutes_watched = data['minutes_watched']
        courses_started = data['courses_started']
        practice_exams_started = data['practice_exams_started']
        practice_exams_passed = data['practice_exams_passed']
        minutes_spent_on_exams = data['minutes_spent_on_exams'] 


        df = pd.DataFrame([[Country,days_on_platform,
                                                   minutes_watched,courses_started,
                                                          practice_exams_started,practice_exams_passed,
                                                        minutes_spent_on_exams]])
        # # Make prediction using the model
        prediction = model4.predict(df)
        if prediction == 0:
            result = "Not Purchased"
        else:
            result = "purchased"
        # Return the prediction as a JSON response
        return result, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

model5 = joblib.load("Model/Model-heart_disaese")

@app.route("/api/predict5",methods=["POST"])
def predict5():
    try:
        # Get data from the POST request
        data = request.get_json()
        # Extract features from the received data
        age= data['age']
        sex = data['sex']
        cystolic_pressure = data['cp']
        trtbps = data['trtbps']
        cholesterol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg'] 
        thalachh = data["thalachh"]
        exng = data['exng']
        oldpeak = data['oldpeak']

        slp = data['slp']
        caa = data['caa'] 
        thall = data['thall']

        df = pd.DataFrame([[age,sex,cystolic_pressure,trtbps,cholesterol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]])
        # # Make prediction using the model
        prediction = model5.predict(df)
        if prediction == 0:
            result = "No Disease"
        else:
            result = "Disease"
        # Return the prediction as a JSON response
        return result, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ ==  "__main__":
    app.run(debug=True)