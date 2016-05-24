import urllib.request
import json
import codecs
import pickle
import time

#f = urllib.request.urlopen('http://api.wunderground.com/api/944b3f3c879d2394/geolookup/forecast10day/q/IA/Cedar_Rapids.json')

#loc_list = ['Berlin', 'Munich', 'Hamburg', 'Cologne', 'Frankfurt', 'Stuttgart', 'Bremen', 'Leipzig', 'Hannover', 'Nuremberg', 'Dortmund', 'Dresden', 'Kassel', 'Kiel', 'Bielefeld', 'Saarbruecken', 'Rostock', 'Freiburg', 'Erfurt', 'Magdeburg']
loc_list = ['Berlin', 'Munich', 'Hamburg']

#download daily 10 day forecast
for loc in loc_list:
    #get the json object
    f = urllib.request.urlopen('http://api.wunderground.com/api/944b3f3c879d2394/geolookup/forecast10day/q/Germany/'+loc+'.json')
    #need to convert byte object to string
    reader = codecs.getreader('utf-8') #how is data encoded? 
    parsed_json = json.load(reader(f)) 
    filename = './10days/wunderground_10days_{}_{}.pkl'.format(time.strftime('%d_%m_%Y_%H_%M'), loc)
    with open(filename, 'wb') as p:
        pickle.dump(parsed_json, p, pickle.HIGHEST_PROTOCOL)
    print (parsed_json['location']['city'] + '10 days downloaded')
    time.sleep(10)
    
#hourly data
    f = urllib.request.urlopen('http://api.wunderground.com/api/944b3f3c879d2394/geolookup/hourly/q/Germany/'+loc+'.json')
    reader = codecs.getreader('utf-8') #how is data encoded? 
    parsed_json = json.load(reader(f)) 
    filename = './hourly/wunderground_hourly_{}_{}.pkl'.format(time.strftime('%d_%m_%Y_%H_%M'), loc)
    with open(filename, 'wb') as p:
        pickle.dump(parsed_json, p, pickle.HIGHEST_PROTOCOL)
    print (parsed_json['location']['city'] + 'hourly downloaded')
    time.sleep(10)
    



f.close()
