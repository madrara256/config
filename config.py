from contextlib import contextmanager
import pyodbc

#@contextmanager
def open_br_db_connection(commit=False):
    print('********** ESTABLISHING CONNECTION **********')

    conn = None
    FreeTDS_DRIVER = 'FreeTDS'
    SQL_SERVER_HOST = 'localhost'
    SQL_SERVER_UID = 'sa'
    SQL_SERVER_PWD = 'password'

    quoted_connection = ';'.join(
    [
    'DRIVER={}'.format(FreeTDS_DRIVER),
    'SERVER={}'.format(SQL_SERVER_HOST),
    'DATABASE=AdventureWorks2017',
    'UID={}'.format(SQL_SERVER_UID),
    'PWD={}'.format(SQL_SERVER_PWD),
    'PORT=1433',
    'TDS_VERSION=8.0'
    ])
    conn = pyodbc.connect(quoted_connection)
    cursor = conn.cursor()
    try:
        yield cursor
        print('********** CONNECTION ESTABLISHED **********')
    except pyodbc.DatabaseError as err:
        print(err)
        cursor.execute('ROLLBACK')
        raise err
    else:
        if commit:
            cursor.execute('COMMIT')
        else:
            cursor.execute('ROLLBACK')
    finally:
        conn.close()

open_br_db_connection(commit=False)

"Proof connection at pyodbc level."
# Test pyodbc connection. Result is 42.
# Note parameters in connection string, <PARAMETER>.

# import pyodbc
#
#
# conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=localhost;PORT=1433;DATABASE=AdventureWorks2017;UID=sa;PWD=passW0rd&&!!4;TDS_Version=8.0;')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM HumanResources.JobCandidate')
# records = cursor.fetchall()
# for i in records:
#     print(i)

