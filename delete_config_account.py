# Import of api
import Json_API
from Json_API import *
from pprint import pprint


def Delete_config(radio_choose):

 radio_choose =radio_choose.get()
 del Json_API.Json_data[radio_choose]
 
 Write_json()
 

Read_json()