import kivy
import kivymd

from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog




class PantryApp(MDApp):

    Window.size = (400, 650)
    def build(self):
        self.theme_cls.primary_palette = 'Yellow' #changes color of button
        self.theme_cls.primary_hue = 'A700' #changes darkness of button color
        self.theme_cls.theme_style = "Dark" #changes background of screen
        appScreen = Screen()
        scrollList = ScrollView()
        checkedOffList = MDList()
        scrollList.add_widget(checkedOffList)



        label = MDLabel(text = 'Add All Checked Items to Pantry', halign = 'center',
                                                                  theme_text_color = 'Custom',
                                                                  text_color =(255/255.0, 197/255.0, 0, 1),
                                                                  pos_hint={'center_x': 0.5,
                                                                 'center_y': 0.98},
                                                                  font_style ='Body1')

        cancelBttn = MDRectangleFlatButton(text = 'Cancel', pos_hint = {'center_x':0.86,
                                                                      'center_y':0.06})


        confirmBttn = MDRectangleFlatButton(text = 'Confirm', pos_hint = {'center_x':0.65,
                                                                      'center_y':0.06})


        appScreen.add_widget(label)
        appScreen.add_widget(cancelBttn)
        appScreen.add_widget(confirmBttn)


        item1 = OneLineListItem(text = 'Banana',size_hint_x = None, width = 300)
        item2 = OneLineListItem(text='Flour', size_hint_x = None, width=300)
        item3 = OneLineListItem(text='Butter', size_hint_x = None, width=300)
        item4 = OneLineListItem(text='Baking Soda', size_hint_x = None, width=300)
        item5 = OneLineListItem(text='Salt', size_hint_x = None, width=300)
        item6 = OneLineListItem(text='Sugar', size_hint_x = None, width=300)
        item7 = OneLineListItem(text='Dozen Eggs', size_hint_x = None, width=300)

        checkedOffList.add_widget(item1)
        checkedOffList.add_widget(item2)
        checkedOffList.add_widget(item3)
        checkedOffList.add_widget(item4)
        checkedOffList.add_widget(item5)
        checkedOffList.add_widget(item6)
        checkedOffList.add_widget(item7)


        appScreen.add_widget(scrollList)

        icon1 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint = {'center_x': 0.30,
                                                                                'center_y': 0.95},
                                                                                size_hint_x = None,
                                                                                on_release = self.show_data)

        icon2 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.88},
                                                                            size_hint_x = None,
                                                                            on_release = self.show_data)

        icon3 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.8},
                                                                            size_hint_x=None,
                                                                            on_release=self.show_data)

        icon4 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.73},
                                                                            size_hint_x=None,
                                                                            on_release=self.show_data)

        icon5 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.65},
                                                                            size_hint_x=None,
                                                                            on_release=self.show_data)

        icon6 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.58},
                                                                            size_hint_x=None,
                                                                            on_release=self.show_data)

        icon7 = MDIconButton(icon = 'dots-vertical-circle-outline', pos_hint={'center_x': 0.30,
                                                                            'center_y': 0.51},
                                                                            size_hint_x=None,
                                                                            on_release=self.show_data)
        appScreen.add_widget(icon1)
        appScreen.add_widget(icon2)
        appScreen.add_widget(icon3)
        appScreen.add_widget(icon4)
        appScreen.add_widget(icon5)
        appScreen.add_widget(icon6)
        appScreen.add_widget(icon7)

        return appScreen



    def show_data(self, obj):

        closeConfirm = MDRectangleFlatButton(text = 'Confirm', on_release = self.close_dialog)
        closeCancel = MDRectangleFlatButton(text = 'Cancel', on_release = self.close_dialog)
        self.dialog = MDDialog(
            title = 'Enter Quantity & Exp Date',
            buttons = [closeConfirm, closeCancel],
            size_hint = (0.7, 1))
        self.dialog.open()

    def close_dialog(self, obj):
      self.dialog.dismiss()




PantryApp().run()
