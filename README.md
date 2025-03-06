# plan of action ()
-----------------------------

steps for address validation:
- first validate the given postcode for UK(in case of wrong postcode, we need to verify given city and country and later on add_line1) 
- what if postcode is having null values? How we gonna implement the logic
- important columns to focus on: [country_iso_2, country,line_1, line_2, building_number,post_town, postcode, dependent_locality]
- how to use query api to get desired result.
- how we gonna implement search here to optimize the code
- how we gonna avoid multiple iteration
- can we get our desired result in single api call


# use pandas to extract the result for postcode
logical steps:
- parse the json data correctly in dataframe as per total count(use try except block to handle wrong postcode or call postcode validation function)
- make it generic as we will be calling it based on every postcode as input and later on we will retrun address and compare it with given address in excel file
- what if wrong postcode(can we check query api and corresponding postcode and address)


