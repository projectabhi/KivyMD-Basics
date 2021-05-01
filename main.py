import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello world', halign='center', theme_text_color='Custom',
                        text_color=(
                        54 / 255.0, 36 / 255.0, 53 / 255.0, 1),
                        )  # theme_text_color=Primary,Secondary,Hint,Error
        return label


# https://github.com/attreyabhatt/KivyMD-Basics
DemoApp().run()
