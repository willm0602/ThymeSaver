#defines a simple user

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self, name):
        self.name = name
    
    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

