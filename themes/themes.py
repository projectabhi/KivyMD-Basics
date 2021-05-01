from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class ThemeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '900'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn_rect = MDRectangleFlatButton(text='Click', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_rect)
        return screen


ThemeApp().run()
