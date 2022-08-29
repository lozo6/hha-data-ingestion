import pandas as pd
import json
import requests
from google.cloud import bigquery
import xlrd

# Section 1
# open_workbook excel file
xls = xlrd.open_workbook('/Users/lozo/Developer/AHI_Github/hha-data-ingestion/data/big3stocks.xls', on_demand=True)
# finds names of all sheets in excel file
sheet_names = xls.sheet_names()
print ('These are the names of all sheets in excel file')
print(sheet_names)
tab1 = pd.read_excel('/Users/lozo/Developer/AHI_Github/hha-data-ingestion/data/big3stocks.xls', sheet_name='AAPL')
tab2 = pd.read_excel('/Users/lozo/Developer/AHI_Github/hha-data-ingestion/data/big3stocks.xls', sheet_name='AMZN')
# prints tab1, tab2
print('These are the dataframes from excel file in data directory')
print(tab1, '\n', tab2)

# Section 2
#using request module for json api
cms = requests.get('https://data.cms.gov/data-api/v1/dataset/1fcb1016-612d-4605-8296-6b220d20e851/data')
apiDataset = cms.json()
print('This is the json api dataset')
print(apiDataset)
# tried adding for loop to better format data in terminal but keeps saying the json api dataset is a list not a string
# for key, value in apiDataset.items():
#     print(key, ':', value)

# Section 3
client = bigquery.Client.from_service_account_json("/Users/lozo/Developer/AHI_Github/hha-data-ingestion/lorenzo-507-8637ff59c5f0.json") # connects to GCP
query_stack = client.query("SELECT * FROM `bigquery-public-data.hacker_news.stories` LIMIT 100") # pulls stackoverflow data from GCP
stackoverflow = query_stack.result() # waits for results
bigquery1 = pd.DataFrame(stackoverflow.to_dataframe()) # puts data in a formatted DataFrame
query_covid = client.query("SELECT * FROM `bigquery-public-data.covid19_open_data.compatibility_view` LIMIT 100") # pulls covid19 data from GCP
covid19 = query_covid.result() # waits for results
bigquery2 = pd.DataFrame(covid19.to_dataframe()) # puts data in a formatted DataFrame
# prints bigquery1, bigquery2
print('These are the dataframes collected from bigquery-public-data')
print(bigquery1, '\n', bigquery2)