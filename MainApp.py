from Food import Food
from User import User
from MainAppScreen import KV #file for screen display

from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
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
from kivy.core.window import Window
Window.size = (400, 650)

KV = '''

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

    
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "CaptainWheezeopp.png"

    MDLabel:
        text: "A$AP Sidebar"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "SadWill@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list
Screen:
    MDList:
        id:container

    NavigationLayout:

#This probably won't be useful here but might be useful for what Katie is doing
    #takes the user list and adds and item "new thing" to it and then adds it to the list on the screen
    # user.localList.append(self.food_name) #Requires self. to work here
    # self.screen.ids.md_list.add_widget(
    #     SwipeItem(text = user.localList[-1])
    # )
#end comments




Window.size = (400, 650)

user = User("PeterParker","spidyman@gmail.com","password")

class SwipeItem(MDCardSwipe):
    '''' Card with behavior '''
    text = StringProperty()
    icon = StringProperty('android')

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''' list item '''
    icon = StringProperty('android')

class ContentNavigationDrawer(BoxLayout):
    pass

class RightCheckBox(IRightBodyTouch,MDCheckbox):
    '''' right container '''

class Registration(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
class ItemDrawer(OneLineIconListItem): # icons and names in the nav list
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1)) #colors gets set back to black after click?


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class dialog_content(BoxLayout):
    pass

class App(MDApp):
    instance = "database"
    bufferDate = None
    data = {
        'emoticon-angry': "WILL, I'LL END YOUR BLOODLINE",
        'database-plus': 'Add all checked to Pantry',
        'delete': 'Delete all checked',
        'plus':'Add item to list',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def JSON_maker(self,food,date):
        print(self.food_name)  #returns the food name, will need to change the variable name of this
        if self.bufferDate != None:
            print(self.bufferDate)

        if self.bufferDate != None:
            exp_bool = True
        else:
            exp_bool = False

        JSON = {
            "Owner" : user.username,
            "Name" : self.food_name,
            "Expires": exp_bool,
            "Exp_date": self.bufferDate,
            "Quantity": 1,
            "Type": None
            }

        print(JSON)

    def got_date(self, the_date):
        print(the_date)
        self.bufferDate = the_date
        return(self.bufferDate)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.got_date)
        date_dialog.open()

    def callback(self,instance): #when you press on one of the items in the circle button it prints the name of the icon being used
        print(instance.icon)
    
    def add_pantry_item(self,instance):
        self.bufferDate = None #reset bufferdate back to null when dialog box opens
        self.food_name = instance.text #this gets the title of the item clicked
        self.test = instance
        print(self.test)
        #So looks like variables need to use self. to be able to use elsewhere
        close_button = MDRectangleFlatButton(text = 'Close', on_release=self.close_dialog)
        submit_button = MDRectangleFlatButton(text = 'Submit', on_release =self.submit_dialog)
        self.dialog = MDDialog(
            title = "Add item to Pantry?",
            size_hint=(0.8,1),
            type="custom",
            content_cls = dialog_content(),
            buttons=[submit_button,close_button]
        )
        self.dialog.open()
        # open thingy that prompts for more info and then creates a food object which is then sent to the food handler

    def close_dialog(self,instance):
        self.dialog.dismiss()

    def submit_dialog(self,instance):
        self.JSON_maker(self.food_name,self.bufferDate) #send collected info to be made into JSON type beat

        #after submitting, remove the item and close the box
        self.remove_item(self.test) #removes the item from the list when button is pressed
        self.dialog.dismiss()


    def remove_item(self,instance):
        self.screen.ids.md_list.remove_widget(instance)


    def on_start(self):
        
        icons_item = {
            "food-apple": "Food",
            "pasta": "Recipes",
            "database": "Pantry",
            "brush": "Theme", #completely unesccesary but would be cool to customize colors of the app
            #see MDThemePicker https://kivymd.readthedocs.io/en/latest/components/pickers/index.html
            "logout": "Log out",
        }

        itemsList = [
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
        
        for i in itemsList:
            user.localList.append(i)

        for i in user.localList: #prints all the items in user local list
            self.screen.ids.md_list.add_widget(
                SwipeItem(text = i)
            )

        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

App().run() #changed the name here, make a note in your git push