__author__ = 'William Coronado'

import xml.etree.ElementTree as ET

filename = '/Users/williamcoronado/Documents/My Tableau Repository/Workbooks/Australian Budget 2015-2016.twb'

tree = ET.parse(filename)
root = tree.getroot()

workbook_plataform = root.get('source-platform')
workbook_version = root.get('version')


datasource = root.find('./datasources[1]/datasource[1]')
datasource_name = datasource.get('name')
datasource_caption = datasource.get('caption')
datasource_version = datasource.get('version')

print('Datasource [Caption: %s, Name: %s, Version: %s' % (datasource_caption, datasource_name, datasource_version))

connection = datasource.find('./connection')
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




