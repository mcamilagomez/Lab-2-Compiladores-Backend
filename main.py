from get_info_from_json import get_info_from_json
from validate_regex import validate_regex
from Alphabet_from_regex import alphabet_from_regex
import json

#Obtain the Json file, delete it latter, it's just for testing
with open('prueba.json') as json_file:
    data = json.load(json_file)

#Get the information from the Json file
regex = get_info_from_json(data)
#Validate the regex expresion 
print(validate_regex(regex))
print(alphabet_from_regex(regex))