import json


komputer={
    'proc':"pentium",
    'karta':"gtx",
    'ram':"hyperx",
    'plyta':"asus pp67",
    'ssd':"crucial"
    }


with open("komputer.json","w") as f:
    json.dump(komputer,f,indent=4)