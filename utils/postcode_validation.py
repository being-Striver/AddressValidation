import requests 
import json 

def validate_postcode(postcode,api_key):
    url = f"https://api.postcodes.io/postcodes/{postcode}/validate"
    payload = json.dumps({
      "postcode": f"{postcode}",
      "api_key": f"{api_key}"
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    return response.status_code

postcode = "BT10 0GY"
city = "Limavady"
api_key="ak_m7wqmqapavPfaBMYkjj5plGMfDuMZ"
data = validate_postcode(postcode, api_key)
print(data)
