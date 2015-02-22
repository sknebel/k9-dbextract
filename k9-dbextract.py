import argparse
import base64
import sqlite3


conn = sqlite3.connect('preferences_storage')
cur = conn.cursor()

a = cur.execute("SELECT value FROM preferences_storage WHERE primkey = 'accountUuids'")
for accID in a.fetchall()[0][0].split(","):
    b = cur.execute("SELECT value FROM preferences_storage WHERE primkey = '" + accID + ".transportUri'")
    print(base64.b64decode(b.fetchall()[0][0]))
    

