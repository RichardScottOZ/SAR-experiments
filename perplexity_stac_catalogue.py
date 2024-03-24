import requests

# Define the search parameters for Sentinel-1 data covering Cloncurry, Queensland
search_params = {
    "collection": "sentinel-1",
    "bbox": [140.5, -21.5, 141.5, -20.5],  # Bounding box coordinates for Cloncurry, Queensland
    "limit": 1  # Limit the number of results to 1
}

# Define the base URL for the AWS Open Data Collection STAC API
base_url = "https://example.aws.opendata.stac.cloud"

# Make a GET request to search for Sentinel-1 data
response = requests.get(f"{base_url}/search", params=search_params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and display the Sentinel-1 data information from the response
    sentinel_data = response.json()
    print(sentinel_data)
else:
    print("Failed to retrieve Sentinel-1 data. Status code:", response.status_code)
