from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from baseClass.bibliotecaMapView import BibliotecaMapView


class BibliotecaView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        map_view = BibliotecaMapView()
        self.add_widget(map_view)

    def on_enter(self):
        self.app.title = "Biblioteche"
