from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


# from screens.banner import Banner


class Dashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "convertitore di numeri in binario"
        self.hint_binary_number = "inserisci un numero binario"

    def on_enter(self):
        self.app.title = "Dashboard"

    '''def on_kv_post(self, base_widget):
        grid = self.ids["grid_banner"]
        for i in range(6):
            banner = Banner(title=f'Function{i}')
            grid.add_widget(banner)'''

    def is_binary(self, binary_number):
        try:
            decimal = int(binary_number, 2)
            self.ids["solution"].text = f'Risultato: {decimal}'
            self.ids["solution"].text_color = "Primary"
        except ValueError:
            self.ids["solution"].text = "numero incoretto"
            self.ids["solution"].text_color = "Error"
