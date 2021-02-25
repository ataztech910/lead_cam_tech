import requests
import re
import json
from bs4 import BeautifulSoup
import ast

def fixCityName(name):
    return name.replace('г..', '').replace('г.', '').replace('пгт', '').replace('с/п', '').replace('с.', '').replace('п.', '').replace('д.', '')

def separateCityAndAddress(addressString):
    splitString = addressString.split(',')
    city = fixCityName(splitString[0])
    separator = ', '
    address = separator.join(splitString[1:])
    return [city, address]

def remapCollectedData(dataArray):
    parsedList = []
    for item in dataArray:
        parsedList.append(separateCityAndAddress(item['title']))
    return parsedList

def parseHtmlFromUrl(urlForParse):
    url = requests.get(urlForParse)
    htmltext = url.text

    soup = BeautifulSoup(htmltext, "html.parser")
    scripts = soup.find_all('script')
    script = scripts[2].string
    sentence = re.sub(r"\s+", "", script, flags=re.UNICODE)

    data = re.findall("data:(.*)],", sentence, re.S) 
    final = "{ \"data\": " +data[0][:-1] + "]}"
    json_data = ast.literal_eval(json.dumps(final))
    json_data = json_data.replace('id:', '"id":')
    json_data = json_data.replace('title:', '"title":')
    json_data = json_data.replace('\'', '"')
    decode = json.loads(json_data)
    return decode['data']

result = remapCollectedData(parseHtmlFromUrl("https://mfc66.ru/otdeleniya"))
print(*result, sep = "\n") 
