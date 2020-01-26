import json

with open('notowania.json') as json_file:
    data = json.load(json_file)
    
    
 
lst=data[0]["rates"]
for i in range(len(lst)):
    print(lst[i]["mid"],lst[i]["currency"])