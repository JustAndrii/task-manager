import psycopg2            

conn = psycopg2.connect(
    database="your_database",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor() 

