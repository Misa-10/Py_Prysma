import json
from pprint import pprint


Json_data = None


def Read_json():
    global Json_data
    with open('json_data.json', 'r') as readfile:
        Json_data = json.load(readfile)


def Write_json():

    with open('json_data.json', 'w') as outfile:
        json.dump(Json_data, outfile)
