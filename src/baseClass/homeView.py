from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy_garden.mapview import MapView


class HomeMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HomeView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        map_view = HomeMapView()
        self.add_widget(map_view)

    def on_enter(self):
        self.app.title = "Home"

    def zoom_plus(self, widget):
        num = HomeMapView.zoom
        print("plus")

    def zoom_minus(self, widget):
        print("minus")

    # (on_release=self.execute, pos_hint={"center_x":.5,"center_y":.4},size_hint=(.2,.3),icon="arrow-right-bold")

    # on_zoom:self.zoom = 12 if self.zoom < 12 else self.zoom
