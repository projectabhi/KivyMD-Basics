from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "Used for login_page"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""


class TextFieldApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Screen()
        # username = MDTextField(text='Enter username', pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


TextFieldApp().run()
