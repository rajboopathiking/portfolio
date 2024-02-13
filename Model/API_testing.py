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
