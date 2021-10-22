from tkinter import messagebox as msb
import re

#function to clear data after inserting into database
#TODO later to make it work
def clearFields(log_type, name = None, email = None, username = None, phone = None):
    if log_type == 'registration':
        name.delete(0, 'end')
        email.delete(0, len(email))
        username.delete(0, len(username))
        phone.delete(0, len(phone))
    elif log_type == 'login':
        email.delete(0, len(email))
        username.delete(0, len(username))

#template function to alert the message box 
def alertMessageBox(title, message, message_type):
    if message_type == 'error_message':
        msb.showerror(title, message)
    elif message_type == 'success_message':
        msb.showinfo(title, message)
    elif message_type == 'warning_message':
        msb.showwarning(title, message)

#function to check for error in when running the sql querry
def checkSqlError(e):
    if str(e).endswith('users.email_address'):
        alertMessageBox('Email Error', 'Email already in use, please use another email', 'error_message')
    elif str(e).endswith('users.username'):
        alertMessageBox('Username Error', 'Username already in use, please use another username', 'error_message')
    else:
        alertMessageBox('Error', 'Please check the inserted data or you ommit some field', 'error_message')

#check the data in each text field if valid
def checkFields(name, email, username, phone):
    if len(name.strip()) < 3 and len(email.strip()) < 3 and len(username.strip()) < 3 and len(phone.strip()) < 3:
        return alertMessageBox('Error', 'All field are required', 'error_message')
    if len(name.strip()) < 3:
        return alertMessageBox('Invalid Name', 'Name is too short or empty', 'error_message')
    if len(email.strip()) < 5 or re.search('@',email) == None:
        return alertMessageBox('Invalid Email Adrress', 'Email Address is invalid', 'error_message')
    if len(username.strip()) < 3:
        return alertMessageBox('Invalid Username', 'Username is too short', 'error_message')
    if len(phone) < 10:
        return alertMessageBox('Invalid Phone', 'Phone number is too short', 'error_message')

    return True