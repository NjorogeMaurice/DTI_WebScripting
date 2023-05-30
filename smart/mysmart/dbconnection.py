import psycopg2

def dbConnect():
    connection = psycopg2.connect(host='127.0.0.1', user='postgres',
                              password='postgres',
                              dbname='defaultertracking', port=5432)
    return connection