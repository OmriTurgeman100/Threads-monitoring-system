import psycopg2  
from creds import DB_HOST, DB_NAME, DB_USER, DB_PASS

def get_database_connection(): # * config
    try:
        postgres = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return postgres
    
    except Exception as e:
        print(e)

    