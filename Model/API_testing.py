# """
# At the command line, only need to run once to install the package via pip:

# $ pip install google-generativeai
# """

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyDlQRDX-j-HIexDnWj15wXPrSGsF26IEds")

# # Set up the model
# generation_config = {
#   "temperature": 0.9,
#   "top_p": 1,
#   "top_k": 1,
#   "max_output_tokens": 2048,
# }

# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]

# model = genai.GenerativeModel(model_name="gemini-pro",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)

# prompt_parts = [
#   "from flask import Flask,jsonify,request,render_template,url_for,redirect\nimport pickle\nimport pandas as pd\napp = Flask(__name__,template_folder=\"templates\",static_folder=\"static\")\n\n# Load the machine learning model\nwith open(\"RealERstateAnalysisModel.pkl\", 'rb') as file:\n  model1 = pickle.load(file)\n\n# Dummy labels, replace it with your actual labels if available\nwith open(\"labels.pkl\",\"rb\") as file:\n  label1 = pickle.load(file)\n\n@app.route(\"/\")\ndef home():\n  return render_template('./index.html')\n\n@app.route(\"/api/predict1\", methods=[\"POST\"])\ndef predict1():\n  try:\n    # Get data from the POST request\n    data = request.get_json()\n\n    # Extract features from the received data\n    deal_satisfaction = data[\"deal_satisfaction\"]\n    property_type = data[\"property_type\"]\n    area = data[\"area\"]\n    sale_month = data[\"sale_month\"]\n    sale_weekday = data[\"sale_weekday\"]\n    birth_month = data[\"birth_month\"]\n    birth_year = data[\"birth_year\"] # No transformation needed\n\n    birth_weekday = data[\"birth_weekday\"]\n    age = data[\"age\"]\n\n    # Make prediction using the model\n    prediction = model1.predict(pd.DataFrame([[deal_satisfaction, property_type, area, sale_month, sale_weekday,\n                   birth_month, birth_year, birth_weekday, age]]))\n\n    # Return the prediction as a JSON response\n    return jsonify({\"prediction\": prediction[0]}), 200\n\n  except Exception as e:\n    return jsonify({\"error\": str(e)}), 500\n\n\nif __name__ == \"__main__\":\n  app.run(debug=True) render templates ('index.html , prediction=prediction[0])\n",
# ]

# response = model.generate_content(prompt_parts)
# print(response.text)


import requests
url = "https://portfolio-project-1.onrender.com/api/predict"
data = {
    "deal-statisfaction":4,"property_type":51,"area":1608,"sale_month":3,"sale_weekday":3,
"birth_month":5,"birth_year":1962,"birth_weekday":5,"age":39
}
try:
    # Send the POST request
    response = requests.post(url, json=data)

    # Check if the response status code is OK (200)
    if response.status_code == 200:
        try:
            # Try to parse the response as JSON
            prediction = response.json()["prediction"]
            print("Prediction:", prediction)
        except ValueError:
            # If parsing as JSON fails, handle the non-JSON response
            print("Non-JSON response:", response.text)
    else:
        # Handle non-200 status code responses
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    # Handle request exceptions (e.g., connection errors)
    print("Request error:", e)
