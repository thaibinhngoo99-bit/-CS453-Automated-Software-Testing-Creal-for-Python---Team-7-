from client_database_connection import mycursor
import os


sql = "INSERT INTO free_node (node_id) VALUES (%s)"
val = (node_id)
mycursor.execute(sql, val)
command = 'python get_code_when_free.py'
os.system(command)