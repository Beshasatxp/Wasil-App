import os
import time
import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class GlassCard(BoxLayout):
    def __init__(self, bg_color=(0.07, 0.09, 0.14, 0.85), border_color=(0.15, 0.2, 0.3, 0.5), radius=[18], **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.border_color = border_color
        self.radius = radius
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
            Color(*self.border_color)
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, self.radius[0]), width=1.1)

class WasilApp(App):
    def build(self):
        Window.clearcolor = (0.03, 0.04, 0.07, 1)
        root = FloatLayout()
        main_layout = BoxLayout(orientation='vertical', padding=[20, 15, 20, 15], spacing=15)

        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        title_box = BoxLayout(orientation='vertical')
        app_title = Label(text="Wasil [color=00f2ff]PRO[/color]", markup=True, font_size='22sp', bold=True)
        app_sub = Label(text="محسن الشبكة الذكي", font_size='12sp', color=(0.55, 0.6, 0.7, 1))
        title_box.add_widget(app_title)
        title_box.add_widget(app_sub)
        header.add_widget(title_box)
        main_layout.add_widget(header)

        gauge_container = FloatLayout(size_hint_y=0.45)
        self.speed_val_label = Label(text="86.7", font_size='48sp', bold=True, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        gauge_container.add_widget(self.speed_val_label)
        main_layout.add_widget(gauge_container)

        opt_btn = Button(text="تسريع الشبكة الآن", size_hint=(1, 0.12), background_color=(0, 0.8, 0.9, 1), bold=True)
        main_layout.add_widget(opt_btn)

        root.add_widget(main_layout)
        return root

if __name__ == '__main__':
    WasilApp().run()
