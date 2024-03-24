import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
api = 'https://geoscience.data.qld.gov.au/api/action/'
# construct our query
query = api + 'package_search?q=cloncurry magnetotelluric&rows=1000'
# make the get request and store it in the response object
response = requests.get(query, headers=headers)

