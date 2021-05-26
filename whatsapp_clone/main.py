from kivymd.app import MDApp
from kivymd.uix import FloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem, ImageLeftWidget, IconRightWidget


class Tab(FloatLayout, MDTabsBase):
    pass


class TabWithIcon(MDFloatLayout, MDTabsBase):
    pass


class DemoTab(MDApp):

    def build(self):
        screen = Builder.load_file('main.kv')
        return screen

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        if (instance_tab.icon):
            print(instance_tab.icon)
            instance_tab.ids.icon.icon = ""
        else:
            print(tab_text)
            instance_tab.ids.label.text = ""

    def new_message(self, name, text, image_location):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=text)
        new_message.add_widget(ImageLeftWidget(source=image_location))
        new_message.add_widget(IconRightWidget(icon="minus"))
        self.root.ids.list.add_widget(new_message)

    def on_start(self):
        # set color
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"

        # Add messages
        self.new_message("Abhijit", "Said hi", "emoji.png")


DemoTab().run()
