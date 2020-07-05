from urllib.request import urlopen
import json


def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def update_ip_info():

    domainName = 'whoisxmlapi.com';
    apiKey = 'Your API key'

    url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?' \
          + 'domainName=' + domainName + '&apiKey=' + apiKey + \
          "&outputFormat=JSON" + "&ip=1"

    data = urlopen(url).read().decode('utf8')
    print(type(json.loads(data)))
