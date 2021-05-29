from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

# from kivy.clock import Clock

# Clock.max_iteration = 100

Window.size = (300, 500)


class Login(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('login.kv'))
        return screen_manager

    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.18})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": 0.85})
        anim.start(widget)

    def icon_animate(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .82})
        anim.start(widget)

    def text_animate(self, widget):
        anim = Animation(opacity=0, duration=1)
        anim += Animation(opacity=.5)
        anim += Animation(opacity=1)
        anim.start(widget)


Login().run()
