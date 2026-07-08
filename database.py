import psycopg2            

conn = psycopg2.connect(   
database="learning_sql",   
user="postgres" ,           
password="1234567"  ,      
host="localhost"  ,        
port="5432"                
)

cursor = conn.cursor() 

