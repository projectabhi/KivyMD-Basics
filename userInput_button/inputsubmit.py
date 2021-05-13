from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from userInput_button.helpers import username_helper
from kivymd.uix.button import MDRectangleFlatButton


class TextFieldApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Screen()
        # username = MDTextField(text='Enter username', pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        self.username = Builder.load_string(username_helper)
        button = MDRectangleFlatButton(text="Show", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen


    def show_data(self,obj):
        print(self.username.text)

TextFieldApp().run()