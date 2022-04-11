import json
from pprint import pprint
from json.decoder import JSONDecodeError


Json_data = None
Json_data2 = None
Json_data3 = None



def Read_json():
    global Json_data
    global Json_data2
    global Json_data3
    try:
       with open('Data/json_data.json', 'r') as readfile:
        try:
           Json_data = json.load(readfile)
        except JSONDecodeError:
           pass
       
       with open('Data/Config_Pixel_Connection.json', 'r') as readfile:
        try:
           Json_data2 = json.load(readfile)
        except JSONDecodeError:
           pass
       
       with open('Data/Config_other.json', 'r') as readfile:
        try:
           Json_data3 = json.load(readfile)
        except JSONDecodeError:
           pass
    except FileNotFoundError:
     pass


def Write_json():

    with open('Data/json_data.json', 'w') as outfile:
        json.dump(Json_data, outfile)
        
def Write_json_Config_Pixel_Connection():

    with open('Data/Config_Pixel_Connection.json', 'w') as outfile:
        json.dump(Json_data2, outfile)

def Write_json_Config_other():

    with open('Data/Config_other.json', 'w') as outfile:
        json.dump(Json_data3, outfile)
