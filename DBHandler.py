import mariadb

PASSWORD = 'stanJT370'
HOST = 'database-1.cuyobspht0m2.us-east-2.rds.amazonaws.com'
USERNAME = 'cookcook'

class DBHandler:
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
    def exec(self, query):
        cursor = self.conn.cursor()
        cursor.execute("Use Thymesaver;")
        cursor.execute(query)
        val = None
        if not 'insert' in query.lower():
            print(cursor.rowcount)
            val = list(cursor)   
        cursor.close()
        self.conn.commit()
        return(val)
    
        
handler = DBHandler()
names = handler.exec("INSERT INTO User VALUES('testUser', 'test@test.com', PASSWORD('TEST!'))")
print(names)