from tkinter import *
import sqlite3

# Create the connection with the database.
conn = sqlite3.connect('HTLMgmt.db')
print('Connected\n')

# Create a cursor object.
cursor = conn.cursor()