from decouple import config
import psycopg2

def getConnection():
    try:
        conn = psycopg2.connect(
            config('DATABASE_URL'), 
            sslmode='require'
        )
        return conn
    except Exception as e:
        print(e)
        return None

def executeQuery(query, params=None):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        column_names = [desc[0] for desc in cursor.description]
        response = cursor.fetchall()
        resp = []
        for data in response:
            resp.append(dict(zip(column_names, data)))
        return resp
    except Exception as e:
        print(e)
        return None
    finally:
        if cursor is not None:
            cursor.close()

def executeOneQuery(query, params=None):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return None
    finally:
        if cursor is not None:
            cursor.close()

def executeNonQuery(query, params=None):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return { "success": True }
    except Exception as e:
        print(e)
        return {"success": False, "message": e}
    finally:
        if cursor is not None:
            cursor.close()