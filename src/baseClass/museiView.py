from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from baseClass.museiMapView import MuseiMapView


class MuseiView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        map_view = MuseiMapView()
        self.add_widget(map_view)

    def on_enter(self):
        self.app.title = "Musei"
