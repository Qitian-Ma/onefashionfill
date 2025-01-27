import pandas as pd
import mysql
import mysql.connector
from mysql.connector import Error
import streamlit as st



host = "sql8.freesqldatabase.com"
database = "sql8759807"
user = "sql8759807"
password = "QfIfIBAswz"
port = 3306

pw = st.text_input("Password")

if pw == "123456":
    # Database connection
    connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=port
)

    # Fetch table data
    query = "SELECT * FROM users"
    df = pd.read_sql(query, connection)

    # Close the connection
    st.write(df)
    connection.close()
    