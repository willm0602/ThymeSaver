import os
import requests
import json

URL = "http://130.157.38.162:5000/executeSqlQuery"
PASSWORD = open('dbpassword.gitignore').read()

class DBHandler:
    def __init__(self, url=URL, pswd = PASSWORD):
        self.url = url
        self.password = pswd

    def exec(self,query):
        try:
            URL = self.url + "/" + query + "/" + self.password
            info = requests.get(URL).content
            jsonifiedData = json.loads(info)
            return(jsonifiedData["entries"])
        except:
            print("Error: SQL Query failed to execute, let Will know if you think this is a problem")
        
DB = DBHandler(URL,PASSWORD)
