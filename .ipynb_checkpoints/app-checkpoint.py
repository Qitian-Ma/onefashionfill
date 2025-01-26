import streamlit as st
import pandas as pd
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter


st.title("ONE FASHION 会员卡登记")
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