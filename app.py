import streamlit as st
import pandas as pd
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from datetime import date
import sqlite3

connection = sqlite3.connect("tessera.db")
cursor = connection.cursor()

file_name="carta_della_famiglia_adobe.pdf"
st.title("ONE FASHION")
submitted = False


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id_carta INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    codice_fiscale TEXT,
    sex TEXT CHECK(sex IN ('M', 'F')),
    birthdate TEXT,
    address TEXT,
    city TEXT,
    province TEXT,
    postalcode INTEGER,
    phonenumber INTEGER,
    email TEXT
)
""")
connection.commit()
connection.close()
st.write("Registrazione della tessera associativa")
st.info("Refresh this page after download.")


with st.form("my_form", clear_on_submit=False):
    sesso = "F"
    info = "Si"
    privacy = "Si"

    carta_n = st.text_input("NUMERO della CARTA")
    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("NOME")

    with col2:
        cognome = st.text_input("COGNOME")

    col3, col4, col5 = st.columns([5, 1, 2])

    with col3:
        cf = st.text_input("CODICE FISCALE")

    with col4:
        sesso = st.selectbox(
    "SESSO",
    ("F", "M"),
)
    with col5:
        dn = st.date_input("DATA di NASCITA", value="1980-01-01")

    col6, col7, col8, col9 = st.columns([5, 1.5, 1.5, 1.5])

    with col6:
        indirizzo = st.text_input("INDIRIZZO")

    with col7:
        citta = st.text_input("CITTA")

    with col8:
        provincia = st.text_input("PROVINCIA")

    with col9:
        cap = st.text_input("CAP")

    col10, col11 = st.columns([3, 7])

    with col10:
        cellulare = st.text_input("CELLULARE")

    with col11:
        email = st.text_input("EMAIL")


    privacy = st.selectbox(
    "Autorizzo al trattamento dei miei dati personali per la registrazione come cliente, nel rispetto della legge sulla privacy (barrare la scelta desiderata):",
    ("Si", "No"),
)
    info = st.selectbox(
    "Autorizzo ad inserire i miei dati nelle liste per l'invio di materiale informativo, pubblicitario o promozionale (barrare la scelta desiderata):",
    ("Si", "No"),
)
    

    submitted = st.form_submit_button("Submit", type="primary")
    if submitted:
        pass_flag = True
        carta_n = carta_n.strip()
        if not carta_n.isdigit() or carta_n == "":
            pass_flag = False
            st.error('NUMERO della CARTA errato', icon="🚨")

        if pass_flag:
            with open("carta_della_famiglia_adobe.pdf", "rb") as infile:
                reader = PdfReader(infile)
                writer = PdfWriter()

                # Copy all pages from reader to writer
                for page in reader.pages:
                    writer.add_page(page)

                # Update form fields
                writer.update_page_form_field_values(writer.pages[0], {
                    "INDIRIZZO": str(indirizzo),
                    "CELLULARE": str(cellulare),
                    "EMAIL": str(email),
                    "COGNOME": str(cognome),
                    "NOME": str(nome),
                    "CODICE_FISCALE": str(cf),
                    "CARTA_N": str(carta_n),
                    "DATA_DI_NASCITA": str(dn),
                    "CITTA": str(citta),
                    "PROVINCIA": str(provincia),
                    "CAP": str(cap),
                    "Data_PRIVACY": str(date.today().strftime("%d-%b-%Y")),
                    "Data_INFO": str(date.today().strftime("%d-%b-%Y")),
                })

                if sesso == "M":
                    writer.update_page_form_field_values(writer.pages[0], {
                    "SESSO_M": "X"
                })
                else:
                    writer.update_page_form_field_values(writer.pages[0], {
                    "SESSO_F": "X"
                })

                if privacy == "Si":
                    writer.update_page_form_field_values(writer.pages[0], {
                    "PRIVACY_SI": "X"
                })
                else:
                    writer.update_page_form_field_values(writer.pages[0], {
                    "PRIVACY_NO": "X"
                })

                if info == "Si":
                    writer.update_page_form_field_values(writer.pages[0], {
                    "INFO_SI": "X"
                })
                else:
                    writer.update_page_form_field_values(writer.pages[0], {
                    "INFO_NO": "X"
                })

            file_name = nome + "_" + cognome + "_" + cf + ".pdf"
            # Write out the updated PDF
            with open(file_name, "wb") as outfile:
                writer.write(outfile)
            connection = sqlite3.connect("tessera.db")
            cursor = connection.cursor()
            try:
                cursor.execute("""
                INSERT INTO users (
                    id_carta,
                    firstname,
                    lastname,
                    codice_fiscale,
                    sex,
                    birthdate,
                    address,
                    city,
                    province,
                    postalcode,
                    phonenumber,
                    email
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (carta_n, nome, cognome, cf, sesso, dn, indirizzo, citta, provincia, cap, cellulare, email))

        # Commit the transaction and close the connection
                connection.commit()
                connection.close()
            except:
                connection.close()

if submitted and pass_flag:
    col12, col13 = st.columns(2)
    with col12:
        with open(file_name, "rb") as file:
            pdf_content = file.read()

            # Create a download button
            st.download_button(
                label="Download PDF",
                data=pdf_content,
                file_name=file_name,
                mime="application/pdf")
            


# records_df = pd.read_csv("Generated_Company_Records.csv")
# fields_df = pd.read_csv("fields.csv")

# st.write("Please try the following records.")
# st.write(1234)
# st.write(
#     pd.DataFrame(
#         {
#             "first column": [1, 2, 3, 4],
#             "second column": [10, 20, 30, 40],
#         }
#     )
# )
# st.dataframe(records_df)

# proveedor = st.text_input("Enter Proveedor here:")

# st.write("Retrieved result:")
# record = records_df[records_df["Proveedor"] == proveedor]
# st.write(record)

# if proveedor in records_df["Proveedor"].tolist():
    
# # Open the original PDF
#     with open("blank_example_with_textField.pdf", "rb") as infile:
#         reader = PdfReader(infile)
#         writer = PdfWriter()

#         # Copy all pages from reader to writer
#         for page in reader.pages:
#             writer.add_page(page)

#         # Update form fields
#         writer.update_page_form_field_values(writer.pages[0], {
#             fields_df['name'][1]: str(record["Fecha"].values[0]),
#             fields_df['name'][2]: str(record["Proveedor"].values[0]),
#             fields_df['name'][3]: str(record["Marca"].values[0]),
#             fields_df['name'][9]: str(record["Nombre de la Empresa"].values[0]),
#             fields_df['name'][10]: str(record["Direccion"].values[0]),
#             fields_df['name'][11]: str(record["Cif"].values[0]),
#             fields_df['name'][12]: str(record["Telefono"].values[0]),
#             fields_df['name'][13]: str(record["Fax"].values[0]),
#             fields_df['name'][14]: str(record["Contacto Comercial"].values[0]),
#             fields_df['name'][15]: str(record["Email Comercial"].values[0]),
#             fields_df['name'][16]: str(record["Telefono Comercial"].values[0])
#         })

#         # Write out the updated PDF
#         with open("updated_example.pdf", "wb") as outfile:
#             writer.write(outfile)
        
#         with open("updated_example.pdf", "rb") as file:
#             pdf_content = file.read()

#             # Create a download button
#             st.download_button(
#                 label="Download PDF",
#                 data=pdf_content,
#                 file_name="filled.pdf",
#                 mime="application/pdf"
#             )