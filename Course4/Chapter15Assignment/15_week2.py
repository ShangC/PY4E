#use following directory to access the txt file if RUNNING the .py file in VS Code Terminal
#c:/Users/AdminWLGlobal/Desktop/PY4E/Course4/Chapter15Assignment/mbox.txt

#If running the .py in actual cmd, no need to add path.

import sqlite3
import re

conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()
cur.execute(
    '''DROP TABLE IF EXISTS Counts
    ''')
cur.execute(
    '''CREATE TABLE Counts (org TEXT, count, INTEGER)
    ''')

print('''Use c:/Users/AdminWLGlobal/Desktop/PY4E/Course4/Chapter15Assignment/mbox.txt 
to test the code in VS Code terminal''')

print("If running in system cmd, simply use mbox.txt")

TxtName = input("Enter File Name:")
TxtHandle = open(TxtName)
print("\nPlease Wait, start Processing File",TxtName,"...\n")
for line in TxtHandle:
    if not line.startswith("From: "):
        continue

    '''
    If using below method, extracted data will exclude [''], 
    but it seems not to be an efficient way
    '''
    # atpos = line.find("@")
    # sppos = line.find(" ", atpos)
    # org = line[atpos+1 : sppos]

    '''
    Below method is good, but everything will carry [''] around the text
    '''
    orgRaw = re.findall("From: \S+@(\S+)",line)
    org = str(orgRaw).strip("'[]")
    # print(org)
    # print(orgRaw)


    cur.execute(
        '''SELECT count FROM Counts 
        WHERE org = ?''', (str(org),)
        )
    row = cur.fetchone()
    if row is None:
        cur.execute(
            '''INSERT INTO Counts (org, count) 
            VALUES (?, 1)''', (str(org),)
            )   
    else:
        cur.execute('''UPDATE Counts 
        SET count = count +1 
        WHERE org = ?''', (str(org),)
        )
    conn.commit()
sqlstr ='''SELECT org, count 
        FROM Counts 
        ORDER BY count 
        DESC LIMIT 10
        '''
        #DESC LIMIT 10
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
print("\nProcessing",TxtName,"completed, result shown above.")
