import json
from xml.dom.minidom import Element
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

##### load the username and password that is in the JSON

loginInfo = json.load(open('login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

sf = Salesforce(username=username, password=password, security_token = security_token)

### gettting of attribute values 

for values in dir(sf):
    if not values.startswith('_'):
        if isinstance(getattr(sf, values), str):
            ## print the values that not starts with underscore
            print(isinstance)

            
metadata_org = sf.describe()
print(metadata_org['encoding'])
print(metadata_org['maxBatchSize'])
print(metadata_org['sobjects'])

## Attaching the dataframe

sobject_with_data = pd.DataFrame(metadata_org['sobjects'])
sobject_with_data.to_csv(metadata_org.csv, index=False)
