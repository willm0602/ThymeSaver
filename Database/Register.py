from DBHandler import DBHandler
import sys
sys.path.append("..")
from User import User

testUser = User("wmigdol","will.migdol@gmail.com","bman0602")

ADD_USER_QUERY = '''
    insert into User values(
    "{username}",
    "{email}",
    "{password}"
);
'''

viewQuery = '''
    SELECT * FROM USER;
'''

def register(user:User, db:DBHandler):
    _username = user.username
    _email = user.email
    _pass = user.password
    query = ADD_USER_QUERY.format(username=_username,email=_email,password=_pass)
    db.exec(query)
    db.exec(viewQuery)
    