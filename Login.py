from kivy.core import text
from kivy.core.window import Window
from kivy.lang import builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from DBHandler import DB
from User import User


def register_user():
    print("REGISTERING")
    
LOGIN = '''

BoxLayout:
    orientation: "vertical"
    MDLabel:
        text: "Login"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0.5, 0, 1
        
    #username
    MDTextField:
        hint_text: "Username"
        id: user
        halign: "center"
        valign: "middle"
        color_mode: "primary"
        mode: "rectangle"
        hint_text_color: "black"
        theme_text_color: "Custom"
        text_color: 0, 0.5, 0, 1  
        
    #password
    MDTextField: 
        hint_text: "Password"
        id: password
        halign: "center"
        valign: "middle"
        color_mode: "primary"
        mode: "rectangle"
        hint_text_color: "black"
        theme_text_color: "Custom"
        text_color: 0, 0.5, 0, 1 
        password: True 
    
    #submit
    MDFillRoundFlatButton:
        id: "submit"
        text: "Register"
        font_size: "30"
        color: (0, 0.5, 0)
        halign: "center"
        pos: self.parent.pos
        on_release:
            print(app.login(user.text,password.text))
        
'''


class LoginApp(MDApp):
    def login(self, username, password):
        query = f"SELECT COUNT(*) FROM User WHERE username = '{username}' AND password = PASSWORD('{password}')"
        count = DB.exec(query)
        if count[0][0]:
            return True
        return(False)
        
    def build(self):
        return builder.Builder.load_string(LOGIN)
          
LoginApp().run()