import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Valid Python variable names
sql_server = "idmp.database.windows.net"
sql_database = "idmp"
driver = "ODBC Driver 17 for SQL Server"  # Match from pyodbc.drivers()
# Build connection string
params = f"""
    Driver={{{driver}}};
    Server=idmp.database.windows.net;
    Database=idmp;
    Authentication=ActiveDirectoryInteractive;
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
"""
sql_conn_str = create_engine(
    f"mssql+pyodbc:///?odbc_connect={quote_plus(params)}",
)

#Note for Kesav: This script was orginally created to load a specific Excel file into the database. 
# However, this script can be modified to load any dataframe into the database. 
# For example, if you have a dataframe named "df" that you want to load into the database, you can use the following code:
#df.to_sql(name="table_name", con=sql_conn_str, schema="schema_name", if_exists="replace", index=False)


# Step 2: Load Excel file
#excel_file = r"C:\Users\anilp\OneDrive\Documents\IDMP\Substance_GroupV2.xlsx"

#sheet_name = "Sheet1"
#df_excel = pd.read_excel(excel_file, sheet_name=sheet_name)
#df_excel.head()


#Step 2: Create the Dataframe from the PDF File. 

df_pdf = pd.read_pdf("SPC.PDF") ##This is wrong step

df_pdf.to_sql(
    name="SMPC", 
    con=sql_conn_str,
    schema="Staging", 
    if_exists="replace", index=False)
