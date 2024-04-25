from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def botao_pressionado(instance):
    print('Botão foi pressionado!')

class MeuApp(App):
    def build(self):
        btn = Button(text='Clique em mim!')
        btn.bind(on_press=botao_pressionado)
        return btn
    
MeuApp().run()