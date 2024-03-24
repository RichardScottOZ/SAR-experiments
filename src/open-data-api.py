import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
api = 'https://geoscience.data.qld.gov.au/api/action/'
# construct our query
query = api + 'package_search?q=cloncurry magnetotelluric&rows=1000'
# make the get request and store it in the response object
response = requests.get(query, headers=headers)

import json
from tqdm import tqdm
import pandas as pd

json_response = json.loads(response.text)

#and get a count of results we can retrieve
total_results = json_response['result']['count']
print(total_results)



