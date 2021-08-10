from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

kv = '''
GameLayout:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
    Image:
        source: "ball.png"
        size_hint: 0.15, 0.15
        x: ball.width/2
        y: 0
        id: ball
'''

class GameLayout(FloatLayout):
    velocidade_y = 25 # posição y
    interval = 0.001
    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        self.velocidade_y = 15
        Clock.schedule_interval(self.jump, self.interval)

    def jump(self, dt):  # função que movimenta objeto
        ball = self.ids.ball
        ball.y += self.velocidade_y # posição y é acrescentada várias vezes
        self.interval = 5

        if ball.y > ball.height: # se a posição y da bola for maior que a propria altura, a velocidade decai
            self.velocidade_y -= 1

        if ball.y <= 0: # se a posição y da bola for menor ou igual a 0, a velocidade é nula
            self.velocidade_y = 0

class Kivy(App):
    def build(self):
        return Builder.load_string(kv)


Kivy().run()
