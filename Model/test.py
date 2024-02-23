import requests

# Model1...................................................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
url = "http://127.0.0.1:5000/api/predict"
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
            print("Prediction-1:", prediction)
        except ValueError:
            # If parsing as JSON fails, handle the non-JSON response
            print("Non-JSON response:", response.text)
    else:
        # Handle non-200 status code responses
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    # Handle request exceptions (e.g., connection errors)
    print("Request error:", e)

# Model2 ............................>>>>>>>

url = "http://127.0.0.1:5000/api/predict2"
data = {
    "From Home":2586,"From Hashtags":1028,"From Explore":619,"From Other":56,"Saves":98,
"Comments":9,"Shares":5,"Likes":162,"Profile Visits":35,"Follows":2
}

# 3920										
try:
    # Send the POST request
    response = requests.post(url, json=data)

    # Check if the response status code is OK (200)
    if response.status_code == 200:
        try:
            # Try to parse the response as JSON
            prediction = response.json()["prediction"]
            print("Prediction-2:", prediction)
        except ValueError:
            # If parsing as JSON fails, handle the non-JSON response
            print("Non-JSON response:", response.text)
    else:
        # Handle non-200 status code responses
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    # Handle request exceptions (e.g., connection errors)
    print("Request error:", e)

#Model3 <...............>
    
input = {"Content":"datascience"}

url = "http://127.0.0.1:5000/api/predict3"
try:
    result = requests.post(url,json=input)
    if result.status_code == 200:
        try:
            final =result.json()
        except:
            print("Content Not Found")

        print("Title:",final["Result"]["Title"])
        print("Link:",final["Result"]["Link"])
        print("Votes:",final["Result"]["Votes"])
        print("Views:",final["Result"]["Views"])
        print("Image:",final["Result"]["Image"])
    else:
        print("Error:", result.status_code, result.text)
except:
    print("Content error")


# Model3 <...............>
    
input = {'country':"IN", 'days_on_platform':320, 'minutes_watched':200,
    'courses_started':1, 'practice_exams_started':2, 'practice_exams_passed':2,'minutes_spent_on_exams':16}

url = "http://127.0.0.1:5000/api/predict4"
result = requests.post(url,json=input)
if result.status_code == 200:
    try:
        final =result.text
        print(final)
    except:
        print("Content Not Found")