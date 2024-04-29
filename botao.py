from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',padding=20)
        slider= Slider(min=0, max=100, value=50, step=0.5)
        slider.bind(value=self.atualizar_label)
        self.label = Label(text = f'Volume:{(slider.value)}')
        
        layout.add_widget(slider)
        layout.add_widget(self.label)
        
        return layout
    
    def atualizar_label(self, instance, valor):
        self.label.text = f'Volume: {(valor)}'
        
MeuApp().run()