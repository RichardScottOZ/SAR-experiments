import requests

# Define the API endpoint for the Cloncurry Extension Magnetotelluric Survey
api_endpoint = "https://geoscience.data.qld.gov.au/data/magnetotelluric/"

# Make a GET request to the API endpoint
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and display the survey data from the response
    survey_data = response.json()
    print(survey_data)
else:
    print("Failed to retrieve survey data. Status code:", response.status_code)
