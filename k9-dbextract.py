import argparse
import base64
import sqlite3


conn = sqlite3.connect('preferences_storage')
cur = conn.cursor()

a = cur.execute("SELECT value FROM preferences_storage WHERE primkey = 'accountUuids'")
for accID in a.fetchall():
    print(accID)
    print("SELECT value FROM preferences_storage WHERE primkey = '" + accID[0] + ".transportURI'")
    b = cur.execute("SELECT value FROM preferences_storage WHERE primkey = '" + accID[0] + ".transportUri'")
    print(base64.b64decode(b.fetchall()[0][0]))
    

