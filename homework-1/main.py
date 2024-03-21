"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


conn_params = {'host': "localhost",
               'database': "north",
               'user': "postgres",
               'password': "newpasswod"}

data = {'customers': ['north_data/customers_data.csv', '%s, %s, %s'],
        'employees': ['north_data/employees_data.csv', '%s, %s, %s, %s, %s, %s'],
        'orders': ['north_data/orders_data.csv', '%s, %s, %s, %s, %s']}

try:
    with psycopg2.connect(**conn_params) as conn:  # connect to database
        for table_name, link in data.items():
            with conn.cursor() as cur, open(link[0], 'r', encoding="utf-8") as f:
                header = next(f)
                reader = csv.reader(f)
                for row in reader:
                    query = f"""
                        INSERT INTO {table_name} ({header})
                        VALUES ({link[1]})
                    """
                    cur.execute(query, row)
        conn.commit()
finally:
    conn.close()
