from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton,MDFloatingActionButton


class ButtonApp(MDApp):
    def build(self):
        screen = Screen()
        btn_rect = MDRectangleFlatButton(text='Click Me', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_flat = MDFlatButton(text='Click Me', pos_hint={'center_x': 0.5, 'center_y': 0.6})
        btn_icon = MDIconButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn_flt = MDFloatingActionButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        screen.add_widget(btn_rect)
        screen.add_widget(btn_icon)
        screen.add_widget(btn_flt)
        return screen


ButtonApp().run()
