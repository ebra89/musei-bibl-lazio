from kivymd.uix.dialog import ListMDDialogMusei
from kivymd.uix.dialog import ListMDDialogBiblio


class PopupMenuMusei(ListMDDialogMusei):
    def __init__(self, musei_data):
        super().__init__()
        # settare il nome del monumento
        headers = "nome_museo,sito_web,indirizzo,telefno,fax,email"
        headers = headers.split(',')
        for i in range(len(headers)):
            attribut_name = headers[i]
            attribut_value = musei_data[i]
            setattr(self, attribut_name, attribut_value)


class PopupMenuBiblioteche(ListMDDialogBiblio):
    def __init__(self,biblio_data):
        super().__init__()
        headers = "denominazione,tipologia,ente,tip_amministrativa,indirizzo,frazione,cap,telefono,fax,email,sito_web"
        headers = headers.split(',')
        for i in range(len(headers)):
            attribut_name = headers[i]
            attribut_value = biblio_data[i]
            setattr(self,attribut_name,attribut_value)
