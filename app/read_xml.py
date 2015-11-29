__author__ = 'William Coronado'

import xml.etree.ElementTree as ET
import yaml

filename = '../tests/data/Australian_Budget_2015-2016.xml'

tree = ET.parse(filename)
root = tree.getroot()


with open("./config/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def print_all_leaf_nodes(data, level):

    if isinstance(data, dict):
        path = '.'
        #print(str(data))
        print(data.items())
        path = data.get('path')
        for key, item in data.items():

            if isinstance(item, str) and key != 'path':
                e = root.find(path)
                print(level*'   ' + key+'= '+e.get(key) )

            print_all_leaf_nodes(item, level+1)

    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            print_all_leaf_nodes(item, level+1)


print_all_leaf_nodes(cfg, 0)

# for i in cfg:
#     print(i)
#     iPath = cfg[i]['path']
#     iElement = root.find(iPath)
#     for ii in cfg[i]:
#         print('   %s = %s' % (ii, iElement.get(ii)))
#         iiPath = cfg[i][ii]['path']
#         iiElement = root.find(iiPath)
#         for iii in cfg[i][ii]:
#             print('      %s = %s' % (iii, iElement.get(iii)))

