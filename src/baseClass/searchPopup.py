from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest


from baseClass.homeView import HomeView, HomeMapView
from baseClass.museiMapView import MuseiMapView
from baseClass.museiView import MuseiView
from baseClass.bibliotecaView import BibliotecaView
from baseClass.bibliotecaMapView import BibliotecaMapView


class SearchPopup(MDInputDialog):
    title = "Cerca per Comune"
    text_button_ok = 'Cerca'


    def __init__(self):
        super().__init__()
        self.size_hint = [.7, .3]

        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
        self.text_field.text = " "
        print(address)

    def geocode_get_lat_lon(self, address):
        with open('src/APIHere/app_id.txt', 'r') as f:
            app_id = f.read()
        with open('src/APIHere/app_code.txt', 'r') as f:
            app_code = f.read()
        address = parse.quote(address)
        # url = 'https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=%s'%(app_id,app_code,address)
        url = 'https://geocode.search.hereapi.com/v1/geocode?q=%s+Italy&apiKey=%s' % (address, app_code)
        print(url)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest, result):
        print('Successo')
        lat = result['items'][0]['position']['lat']
        lon = result['items'][0]['position']['lng']
        print(result)

        # home
        map_view = HomeMapView(lat=lat, lon=lon, zoom=11)
        # .__init__(lat=lat,lon=lon)
        # map_view.center_on(lat,lon)
        home = HomeView().app.root.ids.home_view
        home.add_widget(map_view)


        # musei
        musei_map = MuseiMapView(lat=lat, lon=lon, zoom=11)
        musei_view = MuseiView().app.root.ids.musei_view
        musei_view.add_widget(musei_map)

        # biblioteche
        biblio_map = BibliotecaMapView(lat=lat,lon=lon, zoom=11)
        biblio_view = BibliotecaView().app.root.ids.biblioteca_view.ids.biblioteca_screen
        biblio_view.add_widget(biblio_map)

    def failure(self, urlrequest, result):
        print('Failure')
        print(result)

    def error(self, urlrequest, result):
        print('Error')
        print(result)
