from config import domain, api_path
import json
import urllib2

rest_api = "/posts"

url = "http://"+ domain + "/"+ api_path + rest_api

data = json.load(urllib2.urlopen(url))

print data