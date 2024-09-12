import sqlite3

db = 'database.db'

def write_data(table, name, value):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'''INSERT INTO {table} ({name})
                VALUES (LOWER(?))
                '''
    
    cur.execute(query, (value,))
                
    conn.commit()
    conn.close()
    
def read_spec_data(table, name, value):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'''
                SELECT * FROM {table}
                WHERE LOWER({name}) = LOWER(?)
                '''
    
    cur.execute(query, (value,))
    user = cur.fetchone()
    
    conn.close()
    
    return user

def read_all_data(table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'SELECT * FROM {table}'
    
    cur.execute(query)
    user = cur.fetchall()
    
    conn.close()
    
    return user

    
def delete_data (name):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    cur.execute('''
                DELETE FROM utilisateurs
                WHERE (LOWER)nom = LOWER(?)
                ''', (name,))
    conn.close()
    
def delete_all_data (table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = f'DELETE FROM {table}'
    
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
    
delete_all_data('taches')
write_data('taches', 'tache', "vaisselle")
write_data('taches', 'tache', "balai")
write_data('taches', 'tache', "cuisine")
write_data('taches', 'tache', "toilette")
write_data('taches', 'tache', "aspirateur")

print(db_to_list())