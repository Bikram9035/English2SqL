import os
import sqlite3 
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(".env")

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#defining the prompt that how the llm should respond

prompt=[

	"""
	you are an professional expert in converting english query of user in natural language to SQL query!
the SQL database has the name STUDENT and has the following colums - NAME,CLASS,COURSE,SECTION,MARKS
 \n\n For example, \nExample 1 - How many entries of records are present the sql command will be something like this SELECT COUNT(*) FROM STUDENT;
\nExample 2 - Tell me all the students studying in Data SCience Class?,
the SQL command will be something like this SELECT * FROM STUDEDNT
where CLASS="Data Science";

also the SQL command should not have  ``` in beginning of the SQL QUERY or end and sql word in output

"""
]

#give the user's question,prompt to llm so that it can give sql query
def get_gemini_response(prompt,question):

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response =model.generate_content([prompt[0],question])
    return response.text

#function to retrive the data using the sql db using query provided by llm
def sql_data_retriver(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#ui

st.set_page_config(page_title= "Retrieve data from db using Human Language")
st.header("Natural Human language to SQL by Latest Google-Gemini-Model")
question=st.text_input("input: English to SQL Easily",key="input")
submit= st.button("submit")

if submit:
    response=get_gemini_response(prompt,question)
    print(response)
    data = sql_data_retriver(response, "student.db")
    st.subheader("the response is")
    for row in data:
        print(row)
        st.header(row)

    





