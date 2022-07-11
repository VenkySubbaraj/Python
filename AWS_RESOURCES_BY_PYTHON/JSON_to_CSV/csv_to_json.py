import json
import csv

def function_json(csv_file, json_file):
    data = {}
    with open(csv_file, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        for rows in reader:
            key = rows['Id']
            data[key] = rows
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
csv_file = r'sales.csv'
json_file = r'sales.json'

function_json(csv_file,json_file)
        
