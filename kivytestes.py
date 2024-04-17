from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Olá Mundo! Esse é meu programa em Kivy. \n Sou um aluno sesi e amo meu professor!")

if __name__ == '__main__':
    MyApp().run()