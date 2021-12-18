import json
import requests

headers = {"Authorization":input("Token")} 

para = {
        "name": "venkat"
        }
files = {
        'data':('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./Venkat.xls","rb")
        }
r = requests.post (
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers = headers,
        files = files
        )
print(r.text)

