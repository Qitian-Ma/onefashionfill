import pandas as pd
import sqlite3
import streamlit as st

password = st.text_input("Password")

if password == "123456":

    connection = sqlite3.connect("tessera.db")

    query = "SELECT * FROM users"

    # Execute the query and load the result into a DataFrame
    df = pd.read_sql_query(query, connection)

    st.write(df)
    # Close the connection
    connection.close()