from pyArango.connection import *
import time
from datetime import datetime

time.sleep(15)
conn = Connection(arangoURL="http://34.76.56.173:8529/", username="root", password="password")

# crear base de datos y coleccion
db = conn.createDatabase(name="AS2022")
db = conn["AS2022"]
Students = db.createCollection(name="Students")
db["Students"]

# crear y ejecutar la query AQL
doc = {'_key': 'denisdiderot', 'name': 'Denis Diderot', 'gpa': 3.7}
bind = {"doc": doc}
aql = "INSERT @doc INTO Students LET newDoc = NEW RETURN newDoc"
queryResult = db.AQLQuery(aql, bindVars=bind)

# guardar en log para mostrar en web
now = datetime.now()
time = now.strftime("%H:%M:%S")
a = open('/home/urko/proyecto/3app/logs.txt','a')
a.write('\n' +time+ ' ' +aql)
a.close()
