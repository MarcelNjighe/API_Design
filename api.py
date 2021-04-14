import requests
import json

parameters={
    "amount":5, 
    "category":18,
     "difficulty":'hard',
     "type":'multiple',
     "encode":''
     }
response =requests.get("https://opentdb.com/api.php?", 
params=parameters)
if response.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /parameters/ {}'.format(response.status_code))
def jprint(obj):
    data = json.dumps(obj, sort_keys=True, indent=2,)
    print(data)

jprint(response.json())
