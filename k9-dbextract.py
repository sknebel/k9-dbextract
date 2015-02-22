import argparse
import base64
import sqlite3


def keyLookup(cursor, key):
    return cur.execute("SELECT value FROM preferences_storage where primkey=:key", {"key": key}).fetchone()[0]

conn = sqlite3.connect("preferences_storage")
cur = conn.cursor()

accountList = keyLookup(cur, "accountUuids").split(",")
for accID in accountList:
    name = keyLookup(cur, accID + ".description")
    b64 = keyLookup(cur, accID + ".transportUri")
    print(name,":", base64.b64decode(b64).decode("utf-8"))
    
cur.close()
