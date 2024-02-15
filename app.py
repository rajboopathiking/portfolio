from flask import Flask,jsonify,request,render_template,url_for,redirect
import pickle
import pandas as pd
import numpy as np
app = Flask(__name__,template_folder="templates",static_folder="static")

# Load the machine learning model
with open("Model/RealERstateAnalysisModel.pkl", 'rb') as file:
    model1 = pickle.load(file)

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


if __name__ ==  "__main__":
    app.run(debug=True)
