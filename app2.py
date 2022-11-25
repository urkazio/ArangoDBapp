from arango import ArangoClient
from flask import Flask

app = Flask(__name__)

@app.route('/')

def crearInsertar():

    # Initialize the ArangoDB client.
    client = ArangoClient()

    # Connect to "_system" database as root user.
    sys_db = client.db('_system', username='root', password='password')

    # Create a new database named "upv" if it does not exist.
    if not sys_db.has_database('upv'):
        sys_db.create_database('upv')

    # Connect to "upv" database as root user.
    db = client.db('upv', username='root', password='password')

    # Create a new collection named "students" if it does not exist.
    if db.has_collection('students'):
        students = db.collection('students')
    else:
        students = db.create_collection('students')
        
    # Create some test documents to play around with.
    urko = {'_key': 'urko', 'NOTA': 8.5, 'first': 'Urko', 'last': 'Garcia'}
    unai = {'_key': 'unai', 'NOTA': 6.2, 'first': 'Unai', 'last': 'Lopez'}
    nerea = {'_key': 'nerea', 'NOTA': 9.6, 'first': 'Nerea', 'last': 'Martin'}
    elena = {'_key': 'elena', 'NOTA': 4.0, 'first': 'Elena', 'last': 'Nito'}

    # Insert all new documents.
    students.insert(urko)
    students.insert(unai)
    students.insert(nerea)
    students.insert(elena)
    
    return "Todo ok"
