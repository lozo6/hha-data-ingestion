import pandas as pd
import requests
from google.cloud import bigquery
import xlrd

# Section 1
# open_workbook excel file
xls = xlrd.open_workbook("C:\\Users\\loren\\hha-data-ingestion\\data\\big3stocks.xls", on_demand=True)
# finds names of all sheets in excel file
sheet_names = xls.sheet_names()
print(sheet_names)
tab1 = pd.read_excel('~\\hha-data-ingestion\\data\\big3stocks.xls', sheet_name='AAPL')
tab2 = pd.read_excel('~\\hha-data-ingestion\\data\\big3stocks.xls', sheet_name='AMZN')
# print tab1, tab2
print(tab1, '\n', tab2)

# Section 2
#using request module for json api
cms = requests.get('https://data.cms.gov/data-api/v1/dataset/647e8a75-2135-49a0-83a8-f3b12f687d18/data')
apiDataset = cms.json()
# prints data
print(apiDataset)

# Section 3
client = bigquery.Client.from_service_account_json("C:\\Users\\loren\\hha-data-ingestion\\lorenzo-507-5029d33fcb82.json") # connects to GCP
query_stack = client.query("SELECT * FROM `bigquery-public-data.stackoverflow.posts_questions` LIMIT 100") # pulls stackoverflow data from GCP
stackoverflow = query_stack.result() # waits for results
bigquery1 = pd.DataFrame(stackoverflow.to_dataframe()) # puts data in a formatted DataFrame
query_covid = client.query("SELECT * FROM `bigquery-public-data.covid19_open_data.compatibility_view` LIMIT 100") # pulls covid19 data from GCP
covid19 = query_covid.result() # waits for results
bigquery2 = pd.DataFrame(covid19.to_dataframe()) # puts data in a formatted DataFrame
# prints bigquery1, bigquery2
print(bigquery1, '\n', bigquery2)