import sqlite3 as sq

DATABASENAME = 'database.db'
TABLENAME = 'users'
COLID = 'id'
COLNAME = 'full name'
COLEMAIL = 'email address'
COLUSERNAME = 'username'
COLPHONE =  'phone number'
COLDATEREG = 'date registered'

connection = sq.connect(DATABASENAME)#creating our database
curs = connection.cursor()#creating connection for cursor

#create querry
def createTable():
    sql = f'''CREATE TABLE IF NOT EXISTS {TABLENAME}(
        {COLID} INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        {COLNAME} TEXT NOT NULL,
        {COLEMAIL} TEXT UNIQUE NOT NULL,
        {COLUSERNAME} TEXT UNIQUE NOT NULL,
        {COLPHONE} TEXT NOT NULL,
        {COLDATEREG} TEXT NOT NULL
        )'''
    curs.execute(sql)#creating our table in the database created above

def insertData(name, email, username, phone):
    import datetime as dt
    sql = f'''
        INSERT INTO {TABLENAME} VALUES (
            NULL, {name}, {email}, {username}, {phone}, {dt.datetime.now()}
        )
    ''' 
    curs.execute(sql)
    connection.commit()

def retrievData(username, email):
    sql = f'''
        SELECT * FROM {TABLENAME} WHERE {COLUSERNAME} = {username} AND
        {COLEMAIL} = {email} 
    '''
    rsData = curs.execute(sql).fetchone()
    print(rsData)
    return rsData

if __name__ == '__main__':
    createTable()