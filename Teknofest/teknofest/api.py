from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2 import sql

app = FastAPI()

cargoData = []

app.db_connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="vdmuy3rg.",
    host="localhost",
    port="5432"
    )

cursor = app.db_connection.cursor()
cursor.execute("SELECT * FROM cargo")
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
result = [dict(zip(column_names, row)) for row in rows]
cursor.close()
app.db_connection.close()
cargoData = result
print (cargoData)
