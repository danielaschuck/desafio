
import psycopg2

# conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    port="5433",
    database="analytics_db",
    user="user",
    password="password"
)

# execução da consulta
cur = conn.cursor()
cur.execute("SELECT * FROM table;")
rows = cur.fetchall()
for row in rows:
    print(row)
