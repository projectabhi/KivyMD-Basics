from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem,ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView


class TestApp(MDApp):

    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            item = OneLineListItem(text="Item "+str(i))
            list_view.add_widget(item)

        item2 = TwoLineListItem(text="Two Line item1",secondary_text="Hello world")
        item3 = ThreeLineListItem(text="Three Line item1",secondary_text="Hello world",tertiary_text="Sample text")
        icon = IconLeftWidget(icon="android")
        itemicon = ThreeLineIconListItem(text="Three Line item1",secondary_text="Hello world",tertiary_text="Sample text")
        itemicon.add_widget(icon)

        list_view.add_widget(item2)
        list_view.add_widget(item3)
        list_view.add_widget(itemicon)
        screen.add_widget(scroll)
        return screen


TestApp().run()