from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineAvatarListItem,ImageLeftWidget,OneLineListItem


list_helper = """
Screen:
    ScrollView:
        MDList:
            id: list_container
                
"""


class DemoListHelper(MDApp):


    def build(self):
        screen = Builder.load_string(list_helper)

        return screen


    def on_start(self):
        for i in range(20):
            image = ImageLeftWidget(source="emoji.png")
            item = OneLineAvatarListItem(text="Test "+str(i))
            item.add_widget(image)
            self.root.ids.list_container.add_widget(item)

DemoListHelper().run()