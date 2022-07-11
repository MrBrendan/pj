from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button #класс для создания кнопки
from kivy.uix.boxlayout import BoxLayout #класс для слоя кнопок
from random import randint
from kivy.core.window import Window

Window.size = (300,100)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = 'Парсер "Едадил"'

class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text = "My prog")

    def btn_pressed(self, *args): # метод, который срабатывает при нажатии кнопки
        self.label.color = (randint(0,255)/255, randint(0,255)/255, randint(0,255)/255, 1)


    def build(self):
        box = BoxLayout()  # объект на основе класса BoxLayout
        btn = Button(text = 'Push') # объект кнопки
        btn.bind(on_press = self.btn_pressed) # вешаем на кнопку событие, которое будет срабатывать при нажатии
        box.add_widget(self.label) # помещаем кнопку внутрь BoxLayout
        box.add_widget(btn)

        return box



if __name__ == "__main__":
    MyApp().run()