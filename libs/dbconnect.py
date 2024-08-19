import sqlalchemy
from sqlalchemy import create_engine
from google.cloud.sql.connector import Connector
import pymysql
import json

'''
  Abstraction of a DB connector that could be
  used to connect to a MySQL DB hosted in GCP.
  This class establishes and manages connection.
'''
class DbConnector:
  def __init__(self,db_cfg):
    self.conname=f'''{db_cfg['project_id']}:{db_cfg["region"]}:{db_cfg["instance_name"]}'''
    self.user=db_cfg["user"]
    self.password=db_cfg['passwd']
    self.db=db_cfg['name']
    self.connector=Connector()

  # Gets a connection
  def __get_connection__(self):
    try:
      # Connect to DB
      conn = self.connector.connect( self.conname, "pymysql", user=self.user, password=self.password, db=self.db)
      print(f'''Successfully connected to '{self.db}' database!! ''')
      return conn
    except:
      print(f'''[ERROR]: Failed to connect to database '{self.db}' !! Check inputs & ensure database is running !! ''')
      print(f'''[ERROR]: Connection parameters used db='{self.db}', user='{self.user}', conname='{self.conname}' !! Check inputs & ensure database is running !! ''')

  # Creates a pool of connections, each connection obtained using the above function
  def __get_connection_pool__(self):
    try:
      # Create a DB connection pool and return a connection from the pool
      pool=create_engine("mysql+pymysql://", creator=self.__get_connection__)
      return pool.connect()
    except:
      print(f'''[ERROR]: Failed to create connection pool !''')
      print(f'''[ERROR]: Connection parameters: db='{self.db}', user='{self.user}', conname='{self.conname}' !! Check inputs & ensure database is running !! ''')

  def connect(self):
    return self.__get_connection_pool__()

