__author__ = 'William Coronado'

import xml.etree.ElementTree as ET
import yaml

filename = '../tests/data/Australian_Budget_2015-2016.xml'

tree = ET.parse(filename)
root = tree.getroot()


with open("./config/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
    iPath = cfg[section][path]
    iElement = root.find(iPath)
    for subsection in cfg[section]:
        #print('%s = %s' % (subsection, cfg[section][subsection]))
        print(iElement.get(subsection))



workbook_plataform = root.get('source-platform')
workbook_version = root.get('version')


datasource = root.find('./datasources/datasource')
datasource_name = datasource.get('name')
datasource_caption = datasource.get('caption')
datasource_version = datasource.get('version')

print('Datasource [Caption: %s, Name: %s, Version: %s' % (datasource_caption, datasource_name, datasource_version))

#connection = datasource.find('./connection')
connection = root.find('./datasources/datasource/connection')
conn_dir = connection.get('directory')
conn_filename = connection.get('filename')

print('  |--> Connection [Directory: "%s", Filename: "%s"]' % (conn_dir, conn_filename))

relation = connection.find('./relation')
relation_name = relation.get('name')
relation_table = relation.get('table')
relation_type = relation.get('type')

print('    |--> Relation [Name: %s, Table: %s, Type: %s]' % (relation_name, relation_table, relation_type))

extract_conn = datasource.find('./extract/connection')
extract_conn_dbname = extract_conn.get('dbname')
extract_conn_schema = extract_conn.get('schema')
extract_conn_tablename = extract_conn.get('tablename')
extract_conn_timestamp = extract_conn.get('update-time')

print('      |--> Extract-Connection [DB Name: "%s", Schema: %s, Tablename: %s, Update Time: %s]' % (extract_conn_dbname, extract_conn_schema, extract_conn_tablename, extract_conn_timestamp))




