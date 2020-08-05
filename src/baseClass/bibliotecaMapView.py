from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.clock import Clock
from kivy.app import App
from baseClass.locationPopupMenu import PopupMenuBiblioteche


class BibliotecaMapView(MapView):
    getting_timer = None
    biblio_names = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_getting_biblio_in_fov(self):
        # dopo un secondo prende la psizione del field of view
        try:
            self.getting_timer.cancel()
        except:
            pass

        self.getting_timer = Clock.schedule_once(self.get_biblio_in_fov, 1)

    def get_biblio_in_fov(self, *args):
        # prende la reference da main app e il cursore di db
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()

        app = App.get_running_app()
        sql_statement = "SELECT * FROM biblioteche WHERE Longitudine > %s AND Longitudine < %s AND Latitudine> %s AND Latitudine < %s " % (
            min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)

        biblioteche = app.cursor.fetchall()
        for biblio in biblioteche:
            name = biblio[4]
            # print(name)
            if name in self.biblio_names:
                continue
            else:
                self.add_biblio(biblio)

    def add_biblio(self, biblio):
        # creazione marker per ogni sito
        # da monument prendiamo latitudine e longitudine
        lat, lon = biblio[-2], biblio[-1]

        # passiamo al marker posizione dei siti
        marker = MuseoMarker(lat=lat, lon=lon)
        marker.biblio_data = biblio[:-2]

        # aggiungere il marker alla mappa

        self.add_widget(marker)

        # tenere la traccia di ogni sito solo una volta per evitare di replicare
        name = biblio[0]
        self.biblio_names.append(name)


class MuseoMarker(MapMarkerPopup):
    # source = "assets/geo-recinto.png"
    source = "img/marker-30.png"
    biblio_data = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_release(self):
        # aprire popup di location
        menu = PopupMenuBiblioteche(self.biblio_data)
        menu.size_hint = [.8, .9]
        menu.open()
