import mariadb

#Note: we included the login information for the project, however when we deploy the project we would use environment variables or gitignore to keep this information private
PASSWORD = 'stanJT370'
HOST = 'database-1.cuyobspht0m2.us-east-2.rds.amazonaws.com'
USERNAME = 'cookcook'

class DBHandler:
    '''
    Constructor, connects database handler to the mariadb database
    '''
    def __init__(self,username = USERNAME, pswd = PASSWORD, host = HOST):
        host = HOST
        user = username
        paswd = pswd
        self.conn = mariadb.connect(
            user = user,
            password = paswd,
            port = 3306,
            host = host
        )
        
    #executes a query and returns the result
    def exec(self, query):
        cursor = self.conn.cursor()
        cursor.execute("Use Thymesaver;")
        cursor.execute(query)
        val = None #checks if it returns a result
        if not 'insert' in query.lower():
            val = list(cursor)   
        cursor.close()
        self.conn.commit()
        return(val)
    