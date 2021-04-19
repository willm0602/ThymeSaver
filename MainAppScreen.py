KV = '''

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48) #48


<dialog_content>
    orientation:"vertical"
    spaceing: "12dp"
    size_hint_y: None
    height: "120dp"
    
    MDLabel:
        text: "Does this item expire?"
        valign: "top"
    
    # BoxLayout:

    #     BoxLayout:
    #         MDLabel:
    #             text: "Yes"
    #             halign:"center"
    #         Check:
    #             active: True
    #             halign:"left"

    #     BoxLayout:
    #         MDLabel:
    #             text: "No"
    #             halign:"center"
    #         Check:
    #             halign:"left"
    

    MDRaisedButton:
        text: "Select an expiration date"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
    
    MDTextField:
        hint_text: "Quantity"


# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>: #All of the info in the nav drawer
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image: #User image, not necessary but could be cool. Current Captain Wheeze
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "CaptainWheezeopp.png"

    MDLabel: # This will eventually be the username of the user
        text: "A$AP Sidebar"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel: # and this will be the users email
        text: "SadWill@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView: #This is the nav list in the navbar, probably doesn't need a scrollview
        DrawerList:
            id: md_list

<ListItemWithCheckbox>:
    IconLeftWidget:
        icon: root.icon
    RightCheckbox:

<SwipeItem>:

    size_hint_y: 1
    height: content.height
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": 0.5}
            on_release: app.remove_item(root)

        MDIconButton:
            icon: "database-plus"
            pos_hint: {"center_y": 0.5}
            on_release: app.add_pantry_item(root)
            

    MDCardSwipeFrontBox:
        OneLineListItem: # was OneLineListItem
            id: content
            text: root.text
            icon: root.icon
            _no_ripple_effect: True

        RightCheckBox:
MDScreen: #main screen
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"

    ScrollView:
        scroll_timeout: 100

        MDList:
            id:md_list
            padding: 0

    MDFloatingActionButtonSpeedDial:
        data: app.data
        callback: app.callback #testing here
        root_button_anim: True
        hint_animation: True

    
    NavigationLayout: # This is the top bar for naviagation, currently blue

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Yung Money -- The List"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer: # This is the ||| button on the top left that makes the nav bar work
            id: nav_drawer

            ContentNavigationDrawer: # This is the contents that live inside it
                id: content_drawer
'''