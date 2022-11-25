from pyArango.connection import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def crearInsertar():

    conn = Connection(username="root", password="root_passwd")  # conectarse a arangodb

    # crear base de datos y coleccion
    self.db = conn.createDatabase(name="AS2022")
    self.db = conn["AS2022"]
    studentsCollection = self.db.createCollection(name="Estudiantes")
    self.db["Estudiantes"]


    # crear documento y añadir clave
    doc = coleccion.createDocument()
    doc["nombre"] = "Urko"
    doc["apellido"] = "Garcia"
    doc["edad"] = "20"
    doc._key = "urkogarcia"
    doc.save()

    # crear y ejecutar la query AQL
    bind = {"doc": doc}
    aql = "INSERT @doc INTO Estudiantes LET newDoc = NEW RETURN newDoc"
    queryResult = self.db.AQLQuery(aql, bindVars=bind)
    queryResult[0]  # comprobar si se ha insertado correctamente
