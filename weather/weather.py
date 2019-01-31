import xml.etree.ElementTree as ET
import json

def getValue(element):
    result = dict()
    for child in element:
        result[child.tag] = getValue(child)
    
    result.update(element.attrib)
    
    if len(result) == 0:
        result = element.text
        
    return result


tree = ET.parse('weather.xml')
root = tree.getroot()
obj = getValue(root)

with open('weather.json', 'w') as fp:
    json.dump(obj, fp)
