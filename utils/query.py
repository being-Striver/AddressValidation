import requests 
import json 

def validate_postcode(query, api_key):
    url = f"https://api.postcodes.io/places?q={query}"
    payload = json.dumps({
      "api_key": f"{api_key}"
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

postcode = "BT10 0GY"
city = "Belfast"
query="53 Upper lisburn road"
api_key="ak_m7wqmqapavPfaBMYkjj5plGMfDuMZ"
data = validate_postcode(query, api_key)
print(data)
