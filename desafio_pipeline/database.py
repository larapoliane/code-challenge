import psycopg2
from dotenv import load_dotenv
import os 

load_dotenv()

connection = psycopg2.connect(database=os.getenv('POSTGRES_DB'), 
                              user=os.getenv('POSTGRES_USER'), 
                              password=os.getenv('POSTGRES_PASSWORD'), 
                              host='localhost', 
                              port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers LIMIT 10;")

record = cursor.fetchall()

print("Data from Database:- ", record)