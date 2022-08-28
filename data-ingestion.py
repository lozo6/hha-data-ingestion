import pandas as pd ## import pandas for general file types
import requests
from google.cloud import bigquery
import json

# Section 1
# read excel file
tab1 = pd.read_excel('~\\hha-data-ingestion\\data-ingestion.xlsx', sheet_name='Sheet1')
tab2 = pd.read_excel('~\\hha-data-ingestion\\data-ingestion.xlsx', sheet_name='Sheet2')
# print tab1, tab2
print(tab1, '\n', tab2)

# # Section 2
#using request module for json api
cms = requests.get('https://data.cms.gov/data-api/v1/dataset/647e8a75-2135-49a0-83a8-f3b12f687d18/data')
apiDataset = cms.json()
# prints data
print(apiDataset)

# Section 3
client = bigquery.Client.from_service_account_json(r"C:\Users\loren\hha-data-ingestion\lorenzo-507-5029d33fcb82.json")
query_job = client.query("SELECT * FROM `bigquery-public-data.stackoverflow.posts_questions` LIMIT 100") #error db-types
results = query_job.result()
bigquery1 = pd.DataFrame(results.to_dataframe()) #error db-types