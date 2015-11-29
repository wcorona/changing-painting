__author__ = 'William Coronado'

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
    for subsection in cfg[section]:
        print('   %s = %s' % (subsection, cfg[section][subsection]))


