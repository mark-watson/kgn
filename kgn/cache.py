from sqlite3 import connect, Error
import json
from os import getenv
db_path = '{}/.kgn_hy_cache.db'.format(getenv('HOME'))


def create_db():
    conn = None
    try:
        conn = connect(db_path)
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS dbpedia (query string PRIMARY KEY ASC, data json)')
    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        if conn:
            conn.close()


def save_query_results_dbpedia(query, result):
    conn = None
    try:
        conn = connect(db_path)
        cur = conn.cursor()
        cur.execute('INSERT OR REPLACE INTO dbpedia (query, data) VALUES (?, ?)', [
            query, json.dumps(result)])
        conn.commit()
    except Exception as e:
        print(f"Error saving query results: {e}")
    finally:
        if conn:
            conn.close()


def fetch_result_dbpedia(query):
    results = []
    conn = None
    try:
        conn = connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT data FROM dbpedia WHERE query = ? LIMIT 1', [query])
        d = cur.fetchall()
        if len(d) > 0:
            results = json.loads(d[0][0])
    except Exception as e:
        print(f"Error fetching query results: {e}")
    finally:
        if conn:
            conn.close()
    return results


create_db()

