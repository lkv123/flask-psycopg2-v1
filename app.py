import os
import psycopg2
from flask import Flask
import urlparse
from os.path import exists
from os import makedirs

url = urlparse.urlparse(os.environ.get('DATABASE_URL'))

db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg2.connect(db)

cur = conn.cursor()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/contacts')
def contacts():
    cur.execute("""SELECT name from salesforce.contact""")
    rows = cur.fetchall()
    response = ''
    
    for row in rows:
      response = response + row[0] + ', '
    
    return response

if __name__ == '__main__':
    app.run()

	
