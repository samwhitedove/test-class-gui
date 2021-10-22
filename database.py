import sqlite3 as sq
import datetime as dt
from functions import alertMessageBox, checkFields, checkSqlError, clearFields

DATABASENAME = 'database.db'
TABLENAME = 'users'
COLID = 'id'
COLNAME = 'full_name'
COLEMAIL = 'email_address'
COLUSERNAME = 'username'
COLPHONE =  'phone_number'
COLDATEREG = 'date_registered'

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
    #check if the user data for each field if its empty or by checking the length
    try:
        #checks the field for any invalid data
        if checkFields(name, email, username, phone):
            sql = f'''
                INSERT INTO {TABLENAME} VALUES (
                    NULL, "{name}", "{email}", "{username}", "{phone}", "{dt.datetime.now()}"
                )
            ''' 
            rs = curs.execute(sql)
            #check if data has been inserted into the database successfuly
            if rs != None:
                alertMessageBox('Registration Successful', 'You can now log in with your credentials', 'success_message')
                #clearing the fields after a succesful registration
                clearFields('register', name, email, username, phone )
            connection.commit()
    except Exception as e:
        print(e)
        checkSqlError(e)
        


def retrieveData(username, email):
    sql = f'''
        SELECT {COLUSERNAME},{COLEMAIL} FROM {TABLENAME}
         WHERE  "{COLUSERNAME}" = "{username}" AND "{COLEMAIL}" = "{email}"
    '''
    #fetch data from the database
    rsData = curs.execute(sql).fetchone()
    #checking if data is returned
    if rsData == None:
        alertMessageBox('Login Error', 'Invalid login credentials', 'error_message')
        #clearing the login fields
        clearFields('login', email, username)
    else:
        alertMessageBox('Login Successful', 'Here are your details on the left Panel', 'success_message')

if __name__ == '__main__':
    createTable()
    # insertData("sdsssde", "", "dddd", "0808282833")
    # retrieveData("mike_username", "mike@email.com")