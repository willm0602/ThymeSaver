#Imports that the team built
from Food import Food
from User import User
from DBHandler import DBHandler
from MainAppScreen import KV #file for screen display

#Imports from the kivy library
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition) 
from kivy.uix import anchorlayout
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import IconRightWidget
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
#End imports from kivy library
#idk why this is saying it's an error, it runs fine with it there


#Window size restrictions
Window.size = (400, 650)

#SCREEN DEFINITIONS
class Registration(Screen): # Registration Window
    def register(self, username, password, email):
        query = f"INSERT INTO User VALUES('{username}', '{email}', PASSWORD('{password}'));"
        DB = DBHandler()
        if self.valid(username,DB):
            DB.exec(query)

    def valid(self, username, db):
        users = db.exec(f"SELECT * FROM User WHERE username = '{username}'")
        if len(users) > 0:
            self.errorDialog()
            return(False)
        return(True)

    def errorDialog(self):
        self.dialog = MDDialog(
            text = "ERROR: Username already registered"
        )
        self.dialog.open()

class Login(Screen): # Login Window
    def login(self, username, password):
        db = DBHandler()

        if self.valid(username, password):
            email = self.getEmail(username, db)
            user = User(username, email, password)
            App.user = user
        else:
            self.errorDialog()

    def errorDialog(self):
        self.dialog = MDDialog(
            text = "ERROR: Invalid login information"
        )
        self.dialog.open()


    def getEmail(self, username, db:DBHandler):
        query = f"SELECT email FROM User where username = '{username}'"
        email = db.exec(query)[0]
        return(email)

    def valid(self, username, password):
        query = f"SELECT COUNT(*) FROM User WHERE username = '{username}' AND password = PASSWORD('{password}')"
        DB = DBHandler()
        count = DB.exec(query)
        if count[0][0]:
            return True
        return(False)

class Recipes(Screen): # Recipe Window
    pass

class Pantry(Screen): # Pantry Window
    pass

class Window1(Screen): # WELCOME WINDOW
    pass


class Window2(Screen): #Main List Window -- CHANGE NAME LATER
    #class variable definitions
    data = {
        'database-plus': 'Add all checked to Pantry',
        'delete': 'Delete all checked',
        'plus':'Add item to list',
    }
    
    bufferDate = None
    container = ObjectProperty()
    quantity = ObjectProperty()
    alreadyCheck = False
    alreadyCheckNav = False

    localList = [
            "", #empty item because the positioning puts it under the nav bar
            "pizza",
            "Banana",
            "Lamb",
            "Chicky nuggies",
            "Gogurt",
            "Cheeze stick",
            "Cold pasta sauce",
            "Spam",
            "Paimon",
            "Shallot",
            "Carrot",
            "Way too many green onions",
            "Chili",
            "Paprika",
            "Flour",
            "Sugar",
            "Apples",
            "Sour patch kids"
        ]
    def on_enter(self):
        icons_item = { #This needs extra items at the bottom to fill out the nav bar - mid priority bug to be fixed later
            "food-apple": "Food",
            "pasta": "Recipes",
            "database": "Pantry",
            "brush": "Theme", #completely unesccesary but would be cool to customize colors of the app
            #see MDThemePicker https://kivymd.readthedocs.io/en/latest/components/pickers/index.html
            "logout": "log out",
            "a":"",
            "b":"",
            "c":"",
            "d":"",
        }

        if self.alreadyCheckNav == False: #If the navbar is already full, don't fill it again
            for icon_name in icons_item.keys():
                self.ids.content_drawer.add_widget(
                    ItemDrawer(icon=icon_name, text=icons_item[icon_name])
                )
            self.alreadyCheckNav = True

        if self.alreadyCheck == False:
            for i in self.localList: #prints all the items in user local list
                self.ids.container.add_widget(
                    SwipeItem(text = i)
                )
            self.alreadyCheck = True

    def remove_item(self,instance): #callback function to remove widgets, used for deleting items from the list
        self.ids.container.remove_widget(instance)

    def JSON_maker(self,food,date,quant):
        #debug
        print(food)  #returns the food name, will need to change the variable name of this
        #debug
        print("date in JSON maker: " + str(date))
        
        if date != None:
            print(date) #debug

        if date != None: #if the date is not empty then set the expires boolean to true
            exp_bool = 1
        else:
            exp_bool = 0 #otherwise set it to false

        if date != None: #2 different queries have to be called based on whether a date was given or not
            App.db.exec(f"INSERT INTO Food(owner,name,expired,exp_date) VALUES('{App.user.username}', '{food}', '{exp_bool}', '{date}')")
        else:
            App.db.exec(f"INSERT INTO Food(owner,name,expired) VALUES('{App.user.username}', '{food}', '{exp_bool}')")

        JSON = { #debug
            "Owner" : App.user.username,
            "Name" : food,
            "Expires": exp_bool,
            "Exp_date": date,
            "Quantity": quant,
            "Type": None
            }

        print(JSON) #debug

    def got_date(self, the_date): #gets date from the calender
        self.bufferDate = the_date
        return(self.bufferDate)

    def show_date_picker(self): #opens up the calender
        date_dialog = MDDatePicker(callback=self.got_date)
        date_dialog.open()

    def add_pantry_item(self,instance):#Opens dialog box and prompts for additional information needed for the add to pantry functionality
        
        self.bufferDate = None #reset bufferdate back to null when dialog box opens
        self.food_name = instance.text #this gets the title of the item clicked
        self.pantry_item_instance = instance

        #So looks like variables need to use self. to be able to use elsewhere
        close_button = MDRectangleFlatButton(text = 'Close', on_release=self.close_dialog)
        submit_button = MDRectangleFlatButton(text = 'Submit', on_release=self.submit_dialog)
        self.dialog = MDDialog(
            title = "Add item to Pantry?",
            size_hint=(0.8,1),
            type="custom",
            content_cls = dialog_content(),
            buttons=[submit_button,close_button],
        )
        self.dialog.open()
        # open thingy that prompts for more info and then creates a food object which is then sent to the food handler


    def close_dialog(self,instance): #closes the dialog box
        self.dialog.dismiss()

    def submit_dialog(self,instance):
        #quant = self.dialog.content_cls.ids.quantity.text
        
        if App.sm.get_screen("window2").bufferDate: #if a date was selected assign it to a nicer variable name
            date = App.sm.get_screen("window2").bufferDate
        else: #else let it be empty
            date = None
        
        if self.dialog.content_cls.ids.quantity.text: #If quantity was chosen assign it to a nicer variable name
            quant = self.dialog.content_cls.ids.quantity.text
        else: #else it defaults to 1
            quant = 1



        self.JSON_maker(self.food_name,date,quant) #send collected info to be sent to the database
        #after submitting, remove the item and close the box
        self.remove_item(self.pantry_item_instance) #removes the item from the list when button is pressed
        self.dialog.dismiss()

    def call_back(self,instance):#debug
        if (instance.icon == 'delete'):
            self.deletion()
        else:
            self.show_data(self)

    def deletion(self):
        for delete in CheckedItemsList:
            self.localList.remove(delete)
            self.alreadyCheck = False;
            self.ids.container.clear_widgets()
            if self.alreadyCheck == False:
                for i in self.localList: #prints all the items in user local list
                    self.ids.container.add_widget(
                        SwipeItem(text = i)
                    )
            self.alreadyCheck = True
        CheckedItemsList.clear()
        print(*self.localList, sep='\n')

    def show_data(self, obj):
        close_button = MDRectangleFlatButton(
            text = "Add",
            pos_hint = {"center_x": 0.5, "center_y": 0.4},
            on_press = self.close_dialog,
            on_release = self.add_to_list
        )
        self.alreadyCheck = False

        x_button = MDFlatButton(
            text = "X",
            pos_hint = {"center_x": 1.0, "center_y": 3.5},
            on_press = self.close_dialog
        )

        self.foodItem = MDTextField(
            hint_text = "Enter an item",
            helper_text = "e.g. apples, bananas, orange, etc.",
            helper_text_mode = "on_focus",
            # icon_right_color = app.theme_cls.primary_color,
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            size_hint_x = None,
            width = 250
        )

        self.dialog = MDDialog(
            title = "Enter an item:",
            size_hint = (0.7, 1),
            buttons = [close_button, x_button]
        )

        self.dialog.add_widget(self.foodItem)

        self.dialog.open()


    def add_to_list(self, obj):
        self.localList.append(self.foodItem.text)
        self.ids.container.add_widget(
            SwipeItem(text = self.foodItem.text)
        )


#DIALOG BOX
class dialog_content(BoxLayout):
    quantity = ObjectProperty()



#MAIN LIST CLASSES

# Contains a list of names of the checked items
CheckedItemsList = []

class SwipeItem(MDCardSwipe):
    '''' Card with behavior '''
    text = StringProperty()
    icon = StringProperty('android')

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''' list item '''
    icon = StringProperty('android')

class RightCheckBox(IRightBodyTouch,MDCheckbox):
    '''' right container '''

    def CheckedItems(self, food):
        """
        This will run whenever the Check Box is pushed, and will determine if the item is
        already checked or not. If it is, the program will remove the item from the
        CheckedItemsList. Otherwise, it will add it to the tail end of the list.
        """
        if food in CheckedItemsList:
            CheckedItemsList.remove(food)
        else:
            CheckedItemsList.append(food)



#NAVIGATION DRAWER CLASSES
class ItemDrawer(OneLineIconListItem): # icons and names in the nav list
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1)) #colors gets set back to black after click?

    def on_press(self): #This controls what screen the user goes to when they click on each option in the 
        print(self.icon)
        if self.icon == "pasta":
            self.parent.parent.parent.parent.parent.current = "recipes"
        elif self.icon == "database":
            self.parent.parent.parent.parent.parent.current = "pantry"
        elif self.icon == "food-apple":
            self.parent.parent.parent.parent.parent.current = "window2"


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ContentNavigationDrawer(BoxLayout):
    pass



#MAIN APP
class App(MDApp):
    #initialize user
    user = User("PeterParker","spidyman@gmail.com","password")
    #initialize database
    db = DBHandler()
    #SCREEN MANAGER AND SCREENS
    sm = ScreenManager()
    sm.add_widget(Window1(name="window1"))
    sm.add_widget(Window2(name="window2"))
    sm.add_widget(Login(name="login"))
    sm.add_widget(Registration(name="registration"))
    sm.add_widget(Recipes(name="recipes"))
    sm.add_widget(Pantry(name="pantry"))
    
    def build(self):
        screen = Builder.load_file('test.kv')
        return screen

App().run() #runs the app