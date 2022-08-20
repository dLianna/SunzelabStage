# This code consumes an API, in this it case is 'https://aztro.sameerkumar.website/'.
import requests
import json

# Parameters to pass in endpoint
params = (
    ('sign', 'sagittarius'),
    ('when', 'today'),
)

response = requests.post('https://aztro.sameerkumar.website/', params=params)

# Now it stamps all response's content in text format
# print(response.text)

# Here it load, and it stamps all the content in text format
response_json = json.loads(response.text)
# print(response_json)

# It stamps only the "description" of json file
print(response_json['description'])
