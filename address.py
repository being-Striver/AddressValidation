import requests
import pandas as pd
import json
import logging 

# postcode="BT10 0GY"
# city= "Limavady"
# api_key= "ak_m7vtpqn5K47kgmiCugUQ3enRD7XLm"
# url=f"https://api.ideal-postcodes.co.uk/v1/postcodes/{postcode}?api_key={api_key}"
# response = requests.get(url)
# data = response.json()

# #count the all addresess
# iteration= data["total"]
# print(data)


url = "https://api.ideal-postcodes.co.uk/v1/cleanse/addresses"

payload = json.dumps({
  "query": "10 Downing Street, London, SW2A 2BN",
  "postcode": "SW1A 2BN",
  "post_town": "London",
  "county": "Kent",
  "api_key": "ak_m7wqmqapavPfaBMYkjj5plGMfDuMZ"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)