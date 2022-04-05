# Import of api
import API.Json_API as Json_API
from API.Json_API import *
from pprint import pprint




def Delete_config(radio_choose):

 radio_choose =radio_choose.get()
 del Json_API.Json_data[radio_choose]
 
 Write_json()
 
 

Read_json()