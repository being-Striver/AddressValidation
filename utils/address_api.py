import requests
import pandas as pd
import json
import logging 

postcode="BT10 0GY"
city= "Limavady"
api_key= "ak_m7vtpqn5K47kgmiCugUQ3enRD7XLm"
url=f"https://api.ideal-postcodes.co.uk/v1/postcodes/{postcode}?api_key={api_key}"
response = requests.get(url)
data = response.json()

#count the all addresess
iteration= data["total"]
df= pd.DataFrame(data["result"])
df.drop(["postcode_inward","postcode_outward","double_dependant_locality",\
                 "dependant_thoroughfare","sub_building_name","po_box","department_name",\
                 "organisation_name","udprn","postcode_type","su_organisation_indicator",\
                    'delivery_point_suffix', 'longitude', 'latitude', 'eastings', 'northings', 'district'], axis=1, inplace=True)
print(df)
# print(data['result'])

