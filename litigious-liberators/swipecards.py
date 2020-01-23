from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.animation import Animation
from math import atan2, degrees

class Root(FloatLayout):
    pass

class Card(Widget):
    angle = NumericProperty(0)
    # initial_x = NumericProperty(0)
    # initial_y = NumericProperty(0)
    def on_touch_down(self, touch):
        with self.canvas:
            self.initial_x = touch.x
            # self.initial_y = touch.y

    def on_touch_move(self, touch):
        # if touch.x < self.initial_x:
        #     print("x < initial x")
        #     self.move(-10, 0)
        # elif touch.x > self.initial_x:
        #     print("x > initial x")
        # else:
        #     # no move?
        #     pass
        Animation.cancel_all(self)
        angle = degrees(atan2(touch.y - self.center_y, 
                              touch.x - self.center_x))

        Animation(center=touch.pos, angle=angle).start(self)
        

    # def move(self, x, y):
    #     pass

class SwipeCardApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    SwipeCardApp().run()