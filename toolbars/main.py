from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: print('menu clicked')]]
            right_action_items: [["dots-vertical", lambda x: app.click_dot()],["clock", lambda x: app.callback_2()]]
            elevation: 10
        MDLabel:
            text: 'Hello world'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["help", lambda x: print('help clicked')]]
                mode: 'end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.callback3()
"""


class ToolbarSample(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen

    def click_dot(self):
        print("dot clicked")

    def callback_2(self):
        print("Clock clicked")

    def callback3(self):
        print("Bottom-right button click")

ToolbarSample().run()
