import json
import sqlite3
import os

CurrentPath = os.path.dirname(__file__)
ConnPath = os.path.join(CurrentPath,"C16W5DB.sqlite")
conn = sqlite3.connect(ConnPath)
cur = conn.cursor()

