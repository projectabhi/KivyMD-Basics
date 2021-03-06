import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello world', halign='center', theme_text_color='Custom',
                        text_color=(
                            54 / 255.0, 36 / 255.0, 53 / 255.0, 1),
                        font_style='H5')  # theme_text_color=Primary,Secondary,Hint,Error
        icon_lab = MDIcon(icon='account-clock', halign='center', theme_text_color='Error')
        return icon_lab


# https://github.com/attreyabhatt/KivyMD-Basics
DemoApp().run()
