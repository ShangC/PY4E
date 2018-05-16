import json
import sqlite3
import os

CurrentPath = os.path.dirname(__file__)
ConnPath = os.path.join(CurrentPath,"C15W4DB.sqlite")
conn = sqlite3.connect(ConnPath)
cur = conn.cursor()

cur.executescript(
    '''DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEST UNIQUE
    );

    CREATE TABLE Course (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title   TEST UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTERGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    );
''')

JsonPath = os.path.join(CurrentPath,"roster_data.json")
RawData = open(JsonPath).read()
JsonData = json.loads(RawData)

for item in JsonData:
    name = item[0]
    title = item[1]
    role = int(item[2])

    print((name, title, role))

    cur.execute(
        '''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name,)
    )
    cur.execute(
        '''SELECT id FROM User
        WHERE name = ?''', (name,)
    )
    user_id = cur.fetchone()[0]

    cur.execute(
        '''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title,)
    )
    cur.execute(
        '''SELECT id FROM Course
        WHERE title = ?''', (title,)
    )
    course_id = cur.fetchone()[0]

    cur.execute(
        '''INSERT OR REPLACE INTO Member 
        (user_id, course_id, role)
        VALUES (?, ?, ?)'''
        , (user_id, course_id, role)
    )

    conn.commit()
