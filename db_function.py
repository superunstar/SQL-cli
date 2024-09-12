import sqlite3

db = 'database.db'

def create_db(name):
    conn = sqlite3.connect(f'{name}.db')
    conn.commit()
    conn.close()
    
def create_table(db, table, column, typ):
    typ = typ.upper()
    conn = sqlite3.connect(f'{db}.db')
    cur = conn.cursor()
    
    query = f'CREATE TABLE IF NOT EXISTS {table} ({column} {typ})'
    
    cur.execute(query)
    conn.commit()
    conn.close()
    
def create_column(db, table, column, typ):
    typ = typ.upper()
    conn = sqlite3.connect(f'{db}.db')
    cur = conn.cursor()
    
    query = f'ALTER TABLE {table} ADD COLUMN {column} {typ}'
    
    cur.execute(query)
    conn.commit()
    conn.close()


def write_data(table, column, value):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'''INSERT INTO {table} ({column})
                VALUES LOWER(?)
                '''
    
    cur.execute(query, (value,))            
    conn.commit()
    conn.close()
    
def read_spec_data(table, column, value):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'''
                SELECT * FROM {table}
                WHERE LOWER({column}) = LOWER(?)
                '''
    
    cur.execute(query, (value,))
    user = cur.fetchone()
    
    conn.close()
    
    return user

def read_all_data(table, column):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'SELECT * FROM {table}' ({column})
    
    cur.execute(query)
    user = cur.fetchall()
    
    conn.close()
    
    return user

    
def delete_data (column):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    cur.execute('''
                DELETE FROM utilisateurs
                WHERE LOWER(nom) = LOWER(?)
                ''', (column,))
    conn.close()
    
def delete_all_table (table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'DELETE FROM {table}'
    
    cur.execute(query)
    conn.commit()
    conn.close()
    
def delete_all_column (table, column):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'DELETE FROM {table} ({column})'
    
    cur.execute(query)
    conn.commit()
    conn.close()
    
def db_to_list():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    tache_list = []
    
    cur.execute('SELECT * FROM taches')
    users = cur.fetchall()
    
    for user in users:
        tache_list.append(user)

    print(tache_list)
    
    conn.close()