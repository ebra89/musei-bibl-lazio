from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView
import sqlite3

from baseClass.dashboard import Dashboard
from baseClass.settings import SttingsScreen
from baseClass.homeView import HomeView
from baseClass.museiView import MuseiView
from baseClass.bibliotecaView import BibliotecaView
from baseClass.searchPopup import SearchPopup


class MainApp(MDApp):
    search_menu = None
    connection = None
    cursor = None
    #biblio = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("main.kv")

    def on_start(self):
        # conessione a db
        self.connection = sqlite3.connect("src/csv/app.db")
        self.cursor = self.connection.cursor()
        print("connesso a app.db")

        # call searchpopupmenu
        self.search_menu = SearchPopup()


MainApp().run()
