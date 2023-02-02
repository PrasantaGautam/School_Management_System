from mysql.connector import (connection)

def connections():
    return connection.MySQLConnection(user='root', password='redhat', host='localhost', database='schoolManagement')

    
# def cursors(query):
#     conn = connections()
#     cursor = conn.cursor()
#     cursor.execute(query)
#     return cursor
class Sql:
    def insert(self, query, values):
        """
        query = "INSERT INTO table_name (cols_name,) VALUES (%s,) " 

        values = (cols_value)

        In query cols_name can be multiple separated by comma 

        Also %s identifies the place of given value for the cols_name
        
        """
        conn = connections()
        cursor = conn.cursor()
        cursor.execute(query, values)
        cursor.close()
        conn.commit()
        conn.close()


    def selectall(self, query):
        """
        query = "SELECT * FROM table_name"


        query = "SELECT col_name FROM table_name"

        query = "SELECT col_name, FROM table_name"
        """
        conn = connections()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return results

    def selectone(self, query):
        """
        query = "SELECT * FROM table_name WHERE Primary_key=''"

        or

        query = "SELECT col_name FROM table_name WHERE Primary_key=''"

        query = "SELECT COUNT(*) FROM table_name "

        Returns Data
        """
        conn = connections()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchone()
        cursor.close()
        conn.commit()
        conn.close()
        return results

    def update(self, query, values):
        """
        query = "UPDATE table_name SET col_name = %s WHERE Primary_key = %s"

        values = (newupdate, Primary_key)
        """
        conn = connections()
        cursor = conn.cursor()
        cursor.execute(query, values)
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, query, values):
        """
        query = "DELETE FROM table_name WHERE Primary_key = %s " 

        values = (Primary_value,)

        
        %s identifies the place of given value for the Primary_key
        
        """
        conn = connections()
        cursor = conn.cursor()
        cursor.execute(query, values)
        cursor.close()
        conn.commit()
        conn.close()



