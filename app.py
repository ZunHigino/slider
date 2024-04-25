from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        self.lab1 = Label(
            text = 'SENAI', color = [1,0,0,1],
            font_size=40, bold=True
    )
        self.lab2 = Label(
            text = 'SESI', color = [0,1,0,1],
            font_size=40, italic=True
    )
        self.lab3 = Label(
            text = 'ENEM', color = [0,0,1,1],
            font_size=40, underline=True,
            font_name = 'Arial'
    )
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return layout
    
if __name__ == "__main__":
    MeuApp().run()