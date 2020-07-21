import json
import csv

csvFilePath = 'datasets\dataset_date_formatted_nv_dis.csv'

jsonFilePath = 'datasets\json_file_name.json'

data = {}

csvfile = open(csvFilePath, 'r')
jsonfile = open('datasets\json_file_name.json', 'w')

# Date,Miles,Tonnes,Mile-tons,CO2
fieldnames = ("Date", "Miles", "Tonnes", "Mile-Tons", "CO2")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
