from hashlib import new
import json
from typing import IO
from urllib.request import urlopen

people_string ='''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone"  : "615-555-7164",
            "emails" :  ["johnsmith@bogusemail.com" ,  "john.smith@xyz.com"],
            "has_license" : false
        },
        {
            "name": "Jane Doe",
            "phone"  : "560-555-5153",
            "emails" : null,
            "has_license" : true
         
        }
    ]
   
} 
'''
# data=json.loads(people_string)
# # print(type(data))
# # print(data)
# for person in data["people"]:
#     del person['phone']
   

# # new_string=json.dumps(data)

# new_string=json.dumps(data,indent=2,sort_keys=True)
# print(new_string)


with open('states.json') as f:
    data=json.load(f)

for states in data['states']:
    print(states['name'])

# for state in data["states"]:
#     # print(state['name'],state['abbreviation'])
#       del state['area_codes']

# with open('new_states.json','w') as f:
#     json.dump(data,f, indent=2) 


# with urlopen("https://careers.invesco.com/") as response:
#     source = response.read()
# data=json.loads(source)

# print(json.dumps(data,indent=2))






 
    
