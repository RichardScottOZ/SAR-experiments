import requests
import json
from tqdm import tqdm
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
api = 'https://geoscience.data.qld.gov.au/api/action/'
# construct our query
query = api + 'package_search?q=cloncurry magnetotelluric&rows=1000'
# make the get request and store it in the response object
response = requests.get(query, headers=headers)


json_response = json.loads(response.text)
#check if you want

#and get a count of results we can retrieve
total_results = json_response['result']['count']
print(total_results)

getloop = int(total_results/1000) + 1

if getloop > 0:
    results_list = []
    for i in range(getloop):
        loopq = query + "&start=" + str(i*1000)
        print(loopq)
        response = requests.get(loopq, headers=headers)
        #json_response = response.json()
        json_response = json.loads(response.text)

        results_list.append(json_response)


result_ids = []
for batch in tqdm(results_list, total=len(results_list) ):
    results = batch['result']['results']
    for r in results:
        rid = r['id']
        rauthor = r['author']
        rspatial = r['spatial']
        rtype = r['type']
        
        if len(r['resources']) > 0:
            part_list = []
            for part in r['resources']:
                #modify the columns here to include what you want
                df = pd.DataFrame([part])
                df['rid'] = rid
                df['rauthor'] = rauthor
                df['rspatial'] = rspatial
                df['type'] = rtype
                part_list.append(df)
                allparts = pd.concat(part_list)
                
            result_ids.append(allparts)

dfDatasets = pd.concat(result_ids)            


### getting the SiteLocations is what we want
pd.set_option('display.max_columns', 500)


### getting the SiteLocations is what we want
## guess they are generic geospatial formats if sensible
## can also make the initial naive assumption that the geometry is the same

sl = dfDatasets.loc[dfDatasets['name'].str.contains('ocation')]

gdflist = []
import geopandas as gpd
for index, row in sl.iterrows():
    gdf = gpd.read_file(row['url'])
    gdflist.append(gdf)

gdfmt = pd.concat(gdflist)    

import matplotlib.pyplot as plt
gdfmt.plot()
plt.show() #block

# looks good - one outlier that might be wrong?






