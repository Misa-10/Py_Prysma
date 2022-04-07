import json
from pprint import pprint
from json.decoder import JSONDecodeError


Json_data = None



def Read_json():
    global Json_data
    with open('Data/json_data.json', 'r') as readfile:
     try:
        Json_data = json.load(readfile)
     except JSONDecodeError:
        pass


def Write_json():

    with open('Data/json_data.json', 'w') as outfile:
        json.dump(Json_data, outfile)
        
def Write_json_Config_Pixel_Connection():

    with open('Data/Config_Pixel_Connection.json', 'w') as outfile:
        json.dump(Json_data, outfile)
