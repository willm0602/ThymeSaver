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
import Database.DBHandler as DB
import Database.Register as Register
from User import User


def register_user():
    print("REGISTERING")
    
REGISTRATION = '''

BoxLayout:
    orientation: "vertical"
    MDLabel:
        text: "Register"
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
    
    #email   
    MDTextField: 
        hint_text: "Email"
        id: email
        halign: "center"
        valign: "middle"
        color_mode: "primary"
        mode: "rectangle"
        hint_text_color: "black"
        theme_text_color: "Custom"
        text_color: 0, 0.5, 0, 1 
    
    #submit
    MDFillRoundFlatButton:
        id: "submit"
        text: "Register"
        font_size: "30"
        color: (0, 0.5, 0)
        halign: "center"
        pos: self.parent.pos
        on_release:
            app.register(user.text,password.text, email.text)
        
'''


class DemoApp(MDApp):
    def register(self, username, password, email):
        db = DB.DatabaseHandler()
        user = User(username,email,password)
        Database.Register.register(user,db)
        print("Registered!")
        print(username,email,password)
    
        
    def build(self):
        return builder.Builder.load_string(REGISTRATION)
          

DemoApp().run()
