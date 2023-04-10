import pymysql


def get_connection():
  return pymysql.connect(host='localhost', user='admin',password='admin', db='itfip')