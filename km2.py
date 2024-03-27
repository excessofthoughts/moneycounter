from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class Moneycounter2024App(App):
    nom = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]
    def calculate(self, nom, tis):
        total = 0
        for i in range(len(nom)):
            value = tis[i].text
            if value == '':
                value = 0
            try:
                total += int(value) * self.nom[i]
                error = False
            except ValueError:
                error = True
        if error:
            ppp = Popup(title='Warning!', content=Label(text='Введите корректное числовое значение'), size_hint=(None, None), size=(600, 300))
            ppp.open()
        else:
            self.empty_space.text = str(total)
    def build(self):
        layout = GridLayout(rows=14, spacing=10, padding=10)
        pic1 = Image(source='1.jpeg', size=(125, 125))
        ti1 = TextInput(multiline=False, height=20)
        setattr(self, 'ti1', ti1)
        pic2 = Image(source='2.jpeg', size=(125, 125))
        ti2 = TextInput(multiline=False, height=20)
        setattr(self, 'ti2', ti2)
        pic5 = Image(source='5.jpeg', size=(125, 125))
        ti5 = TextInput(multiline=False, height=20)
        setattr(self, 'ti5', ti5)
        pic10 = Image(source='10.jpeg', size=(125, 125))
        ti10 = TextInput(multiline=False, height=20)
        setattr(self, 'ti10', ti10)
        pic50 = Image(source='50.jpeg', size=(250, 125))
        ti50 = TextInput(multiline=False, height=20)
        setattr(self, 'ti50', ti50)
        pic100 = Image(source='100.jpeg', size=(250, 125))
        ti100 = TextInput(multiline=False, height=20)
        setattr(self, 'ti100', ti100)
        pic200 = Image(source='200.jpeg', size=(250, 125))
        ti200 = TextInput(multiline=False, height=20)
        setattr(self, 'ti200', ti200)
        pic500 = Image(source='500.jpeg', size=(250, 125))
        ti500 = TextInput(multiline=False, height=20)
        setattr(self, 'ti500', ti500)
        pic1000 = Image(source='1000.jpeg', size=(250, 125))
        ti1000 = TextInput(multiline=False, height=20)
        setattr(self, 'ti1000', ti1000)
        pic2000 = Image(source='2000.jpeg', size=(250, 125))
        ti2000 = TextInput(multiline=False, height=20)
        setattr(self, 'ti2000', ti2000)
        pic5000 = Image(source='5000.jpeg', size=(250, 125))
        ti5000 = TextInput(multiline=False, height=20)
        setattr(self, 'ti5000', ti5000)

        self.empty_space = Label(text='Введите количество монет или купюр каждого номинала и нажмите на кнопку, чтобы посчитать сумму', halign='center', size_hint=(None, None), size=(800, 50), text_size=(800, None))
        baton = Button(text='Посчитать!')
        baton.bind(on_press=lambda instance: self.calculate(self.nom, [self.ti1, self.ti2, self.ti5, self.ti10, self.ti50, self.ti100, self.ti200, self.ti500, self.ti1000, self.ti2000, self.ti5000]))

        layout.add_widget(pic1)
        layout.add_widget(ti1)
        layout.add_widget(pic2)
        layout.add_widget(ti2)
        layout.add_widget(pic5)
        layout.add_widget(ti5)
        layout.add_widget(pic10)
        layout.add_widget(ti10)
        layout.add_widget(pic50)
        layout.add_widget(ti50)
        layout.add_widget(pic100)
        layout.add_widget(ti100)
        layout.add_widget(pic200)
        layout.add_widget(ti200)
        layout.add_widget(pic500)
        layout.add_widget(ti500)
        layout.add_widget(pic1000)
        layout.add_widget(ti1000)
        layout.add_widget(pic2000)
        layout.add_widget(ti2000)
        layout.add_widget(pic5000)
        layout.add_widget(ti5000)
        layout.add_widget(self.empty_space)
        layout.add_widget(baton)
        return layout

if __name__ == '__main__':
    Moneycounter2024App().run()