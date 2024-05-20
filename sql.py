import sqlite3

#making connect is same as creating db
connection = sqlite3.connect("student.db")

#making cursor is like a mouse cursor to insert things on the db
cursor = connection.cursor()

#creating the structure of the table and defining type of variables
table_info=""" 
            Create Table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),COURSE VARCHAR(25),SECTION VARCHAR(10),MARKS INT);

            """

#excuting the code in db to create empty table
cursor.execute(table_info)

#fill the table with values
cursor.execute('''Insert Into STUDENT Values("BIKRAM","10TH GRADE","DATA SCIENCE" ,"A","90" ) ''')
cursor.execute('''Insert Into STUDENT Values("ROY","10TH GRADE","WEB DEV" ,"B","67") ''')
cursor.execute('''Insert Into STUDENT Values("RIYA","9TH GRADE","CLOUD DEV" ,"C","70")''')
cursor.execute('''Insert Into STUDENT Values("YAMINI","11TH GRADE","IOS DEV" ,"A","85")''')
cursor.execute('''Insert Into STUDENT Values("YASHNA","12TH GRADE","REACT DEV" ,"B","75") ''')
cursor.execute('''Insert Into STUDENT Values("ZYAN","10TH GRADE","LLM" ,"C","82")''')
cursor.execute('''Insert Into STUDENT Values("TINA","11TH GRADE","GENAI" ,"C","77")''')
               
               

#display the tables
print("The Inserted Records are:")
data= cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

#close the connection is like saving shuting off the sql db
connection.commit()
connection.close()





