import streamlit as st
import pyodbc
import pandas as pd
# Initialize connection.
# Uses st.experimental_singleton to only run once.


@st.experimental_singleton
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()
# server = 'gvs72069.inc.hpicorp.net,2048' 
# database = 'GABI-P' 
# username = 'GABI_STG_RW_1' 
# password = 'fT7_E*4U6k_m' 
# odbc_GABI_P = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

dynamic_sql = '''
SELECT top 10 * from [DMINDWNG_SCHEMA].[V_Quality_Status_Change_Reason_Dimension_Hierarchy]
'''

pandas_read_pdf = pd.read_sql_query(sql = dynamic_sql,\
                                        con = conn)

st.dataframe(pandas_read_pdf)
# # Perform query.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT tpp 10 from [DMINDWNG_SCHEMA].[V_Quality_Status_Change_Reason_Dimension_Hierarchy];")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")