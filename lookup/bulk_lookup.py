import pandas as pd
import requests
import json
import logging

api_key="ak_m7wqmqapavPfaBMYkjj5plGMfDuMZ"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting the bulk address lookup using postcodes.io api")

df_add=pd.read_csv('C:/Users/shudh/OneDrive/Desktop/Nike/data/data1.csv', sep="\t")
df_add["building_number"] = df_add["addressLine1"].str.extract(r'(\d+)')
df_add["address"]=df_add["addressLine1"].str.replace(r'\d+', '', regex=True)

postcodes_list= df_add["postcode"].tolist()
address_list= df_add["address"].tolist()
building_number_list= df_add["building_number"].tolist()  

# create an empty dataframe to store the valid address
schema =['FailureDate', 'EnterpriseCode', 'SalesOrderNo', 'PurchaseOrderNo',\
       'EDD', 'ErrorCode', 'ErrorMsg', 'CarrierServiceCode', 'addressLine1',\
       'building_number', 'address',
       'addressLine2', 'additionalName', 'city', 'Country', 'zipCode',\
       'phoneNumber', 'contactName', 'Unnamed: 16', 'Unnamed: 17'\
       ]
df_valid_address = pd.DataFrame(columns=schema) 


logger.info(f"Total postcodes to lookup: {len(postcodes_list)}") 

def read_address_data(postcode, api_key)->pd.DataFrame:
    '''This function reads the address data from the postcodes.io api'''
    url = f"https://api.ideal-postcodes.co.uk/v1/postcodes/{postcode}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    df= pd.DataFrame(data["result"])
    # drop unnecessary columns to save space
    df.drop(["postcode_inward","postcode_outward","double_dependant_locality",\
                 "dependant_thoroughfare","sub_building_name","po_box","department_name",\
                 "organisation_name","udprn","postcode_type","su_organisation_indicator",\
                  'longitude', 'latitude', 'eastings', 'northings', 'district', 'country_code'], axis=1, inplace=True)
    
    return df


def validate_postcode(postcode,api_key):
    '''This function validates the postcode using postcodes.io api'''

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

for postcode in postcodes_list:
    status_code = validate_postcode(postcode, api_key)
    if status_code == 200:
        logger.info(f"Postcode {postcode} is valid")
        df=read_address_data(postcode, api_key)
        
        postcode_building_number = df["building_number"].tolist()
        postcode_address = df["line_1"].tolist()
        # postcode_city = df["post_town"].tolist()
        # postcode_country = df["country_iso_2"].tolist()
        search_address=postcode_address[postcode]
        search_building_number=postcode_building_number[postcode]

        # Now we will apply conditional logic to validate building number and address
        if len(search_building_number) > 0 and search_building_number is not None:
            # search the building number in the dataframe
            df1=df[df["building_number"].str.contains(search_building_number, case=False, na=False)]

            logger.info(f"Building number {search_building_number} is valid")

        search_address = address_list[postcode]
        df_add = df[df["line_1"].str.contains(search_address, case=False, na=False)]
        logger.info(f"Address {search_address} is valid")    
    else:
         
        logger.error(f"Postcode {postcode} is invalid")
    

if __name__ == "__main__":
    pass