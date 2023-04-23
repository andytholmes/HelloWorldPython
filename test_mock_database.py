import os
#import pyodbc

server = 'localhost'
database = 'test_onprem'
username = 'sa '
password = 'MyPass@word'
# DB setting for non-test env
#if not os.environ.get('TEST'):
#    dbc = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#    dbc.autocommit = True
#else:
	# if we are in test return dummy object we will override by mock
#	dbc = None

#def test_program():
	# this test is using mocked database connection.
#	assert True