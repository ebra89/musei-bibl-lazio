"""
Components/Dialog
=================

.. seealso::

    `Material Design spec, Dialogs <https://material.io/components/dialogs>`_


.. rubric:: Dialogs inform users about a task and can contain critical
    information, require decisions, or involve multiple tasks.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialogs.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.dialog import MDDialog

    KV = '''
    FloatLayout:

        MDFlatButton:
            text: "ALERT DIALOG"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()
    '''


    class Example(MDApp):
        dialog = None

        def build(self):
            return Builder.load_string(KV)

        def show_alert_dialog(self):
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Discard draft?",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color
                        ),
                        MDFlatButton(
                            text="DISCARD", text_color=self.theme_cls.primary_color
                        ),
                    ],
                )
            self.dialog.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/alert-dialog.png
    :align: center
"""

__all__ = ("MDDialog",)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.button import BaseButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import BaseListItem
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDTextButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.theming import ThemableBehavior
from kivymd import images_path
from kivymd.material_resources import DEVICE_IOS

# nome_museo,sito_web,statale_non_statale,omr,sistema_museale_territoriale,sistema_museale_urbano,
# sistema_museale_tematico,casa_museo,indirizzo,localita,ubicazione,cap,telefno,fax,email
Builder.load_string(
    """
#:import images_path kivymd.images_path
<ContentInputDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)
    MDLabel:
        font_style: 'H6'
        text: root.title
        halign: 'left' if not root.device_ios else 'center'
    BoxLayout:
        id: box_input
        size_hint: 1, None
    Widget:
    Widget:
    MDSeparator:
        id: sep
    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0
#:import webbrowser webbrowser
#:import parse urllib.parse
<ThinLabel@MDLabel>:
    size_hint: 1, None
    valign: 'middle'
    height: self.texture_size[1]
<ThinLabelButton@ThinLabel+MDTextButton>:
    size_hint_y: None
    valign: 'middle'
    height: self.texture_size[1]
<ThinBox@BoxLayout>:
    size_hint_y: None
    height: self.minimum_height
    padding: dp(0), dp(0), dp(10), dp(0)
    
<ListMDDialogMusei>:
    title: ""
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)
    
        MDLabel:
            id: title
            text: root.title
            font_style: 'H6'
            halign: 'left' if not root.device_ios else 'center'
            valign: 'top'
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
    
        ScrollView:
            id: scroll
            size_hint_y: None
            height:
                root.height - (title.height + dp(48)\
                + sep.height)
    
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    #source: '{}dialog_in_fade.png'.format(images_path)
                    source: '{}transparent.png'.format(images_path)
    
            MDList:
                id: list_layout
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(15)
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    Color:
                        rgba: [1,0,0,.5]   
                ThinBox:
                    ThinLabel:
                        text: "Nome Museo: "
                    ThinLabelButton:
                        text: root.nome_museo
                        on_release:
                            webbrowser.open("http://maps.apple.com/?address="+parse.quote(self.text))
                ThinBox:
                    ThinLabel:
                        text: "Sito Web: "
                    ThinLabelButton:
                        text: root.sito_web
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Statale o Non Statale: "
                    ThinLabel:
                        text: root.statale_non_statale
                ThinBox:
                    ThinLabel:
                        text: "omr: "
                    ThinLabel:
                        text: root.omr
                ThinBox:
                    ThinLabel:
                        text: "Sistema Museale Teritoriale: "
                    ThinLabel:
                        text: root.sistema_museale_territoriale
                ThinBox:
                    ThinLabel:
                        text: "Sistema Museale Urbano: "
                    ThinLabel:
                        text: root.sistema_museale_urbano
                ThinBox:
                    ThinLabel:
                        text: "Sistema Museale Tematico: "
                    ThinLabel:
                        text: root.sistema_museale_tematico
                ThinBox:
                    ThinLabel:
                        text: "Casa Museo: "
                    ThinLabel:
                        text: root.casa_museo
                ThinBox:
                    ThinLabel:
                        text: "Indirizzo: "
                    ThinLabel:
                        text: root.indirizzo
                ThinBox:
                    ThinLabel:
                        text: "Località: "
                    ThinLabel:
                        text: root.localita
                ThinBox:
                    ThinLabel:
                        text: "Ubicazione: "
                    ThinLabel:
                        text: root.ubicazione
                ThinBox:
                    ThinLabel:
                        text: "CAP: "
                    ThinLabel:
                        text: root.cap
                ThinBox:
                    ThinLabel:
                        text: "Telefono: "
                    ThinLabel:
                        text: root.telefno
                ThinBox:
                    ThinLabel:
                        text: "Fax: "
                    ThinLabel:
                        text: root.fax
                ThinBox:
                    ThinLabel:
                        text: "Email: "
                    ThinLabel:
                        text: root.email
                ThinBox:
                    ThinLabel:
                        text: "Facebook: "
                    ThinLabelButton:
                        text: root.Facebook
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Twitter: "
                    ThinLabelButton:
                        text: root.Twitter
                        on_release:
                            webbrowser.open(self.text)
               
                   

        MDSeparator:
            id: sep
##denominazione,tipologia,ente,tip_amministrativa,indirizzo,frazione,cap,telefono,fax,email,sito_web,Twitter,Facebook
<ListMDDialogBiblio>:
    title: ""
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)
    
        MDLabel:
            id: title
            text: root.title
            font_style: 'H6'
            halign: 'left' if not root.device_ios else 'center'
            valign: 'top'
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
    
        ScrollView:
            id: scroll
            size_hint_y: None
            height:
                root.height - (title.height + dp(48)\
                + sep.height)
    
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    #source: '{}dialog_in_fade.png'.format(images_path)
                    source: '{}transparent.png'.format(images_path)

##denominazione,tipologia,ente,tip_amministrativa,indirizzo,frazione,cap,telefono,fax,email,sito_web,Twitter,Facebook
            MDList:
                id: list_layout
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(15)
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    Color:
                        rgba: [1,0,0,.5]   
                ThinBox:
                    ThinLabel:
                        text: "Denominazione: "
                    ThinLabelButton:
                        text: root.denominazione
                        on_release:
                            webbrowser.open("http://maps.apple.com/?address="+parse.quote(self.text))
                ThinBox:
                    ThinLabel:
                        text: "Tipologia: "
                    ThinLabel:
                        text: root.tipologia
                ThinBox:
                    ThinLabel:
                        text: "Ente: "
                    ThinLabel:
                        text: root.ente
                ThinBox:
                    ThinLabel:
                        text: "Tipologia Amministrativa: "
                    ThinLabel:
                        text: root.tip_amministrativa
                ThinBox:
                    ThinLabel:
                        text: "Indirizzo: "
                    ThinLabel:
                        text: root.indirizzo
                ThinBox:
                    ThinLabel:
                        text: "Localià: "
                    ThinLabel:
                        text: root.frazione
                ThinBox:
                    ThinLabel:
                        text: "CAP: "
                    ThinLabel:
                        text: root.cap
                ThinBox:
                    ThinLabel:
                        text: "Telefono: "
                    ThinLabel:
                        text: root.telefono
                ThinBox:
                    ThinLabel:
                        text: "Fax: "
                    ThinLabel:
                        text: root.fax
                ThinBox:
                    ThinLabel:
                        text: "Email: "
                    ThinLabel:
                        text: root.email
                ThinBox:
                    ThinLabel:
                        text: "Sito Web: "
                    ThinLabelButton:
                        text: root.sito_web
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Facebook: "
                    ThinLabelButton:
                        text: root.Facebook
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Twitter: "
                    ThinLabelButton:
                        text: root.Twitter
                        on_release:
                            webbrowser.open(self.text)
                
                
               
                   

        MDSeparator:
            id: sep
            

<ContentMDDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)
    text_button_ok: ''
    text_button_cancel: ''
    MDLabel:
        id: title
        text: root.title
        font_style: 'H6'
        halign: 'left' if not root.device_ios else 'center'
        valign: 'top'
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]
    ScrollView:
        id: scroll
        size_hint_y: None
        height:
            root.height - (box_buttons.height + title.height + dp(48)\
            + sep.height)
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                #source: f'{images_path}dialog_in_fade.png'
                source: f'{images_path}transparent.png'
        MDLabel:
            text: '\\n' + root.text + '\\n'
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'top'
            halign: 'left' if not root.device_ios else 'center'
            markup: True
    MDSeparator:
        id: sep
    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0
"""
)


class BaseDialog(ThemableBehavior, ModalView):
    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class MDDialog(BaseDialog):
    title = StringProperty()
    """
    Title dialog.

    .. code-block:: python

        self.dialog = MDDialog(
            title="Reset settings?",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-title.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text = StringProperty()
    """
    Text dialog.

    .. code-block:: python

        self.dialog = MDDialog(
            title="Reset settings?",
            text="This will reset your device to its default factory settings.",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    radius = ListProperty([7, 7, 7, 7])
    """
    Dialog corners rounding value.

    .. code-block:: python

        self.dialog = MDDialog(
            text="Oops! Something seems to have gone wrong!",
            radius=[20, 7, 20, 7],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    buttons = ListProperty()
    """
    List of button objects for dialog.
    Objects must be inherited from :class:`~kivymd.uix.button.BaseButton` class.

    .. code-block:: python

        self.dialog = MDDialog(
            text="Discard draft?",
            buttons=[
                MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
            ],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-buttons.png
        :align: center

    :attr:`buttons` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    items = ListProperty()
    """
    List of items objects for dialog.
    Objects must be inherited from :class:`~kivymd.uix.list.BaseListItem` class.

    With type 'simple'
    -----------------

    .. code-block:: python

        from kivy.lang import Builder
        from kivy.properties import StringProperty

        from kivymd.app import MDApp
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.list import OneLineAvatarListItem

        KV = '''
        <Item>

            ImageLeftWidget:
                source: root.source


        FloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_simple_dialog()
        '''


        class Item(OneLineAvatarListItem):
            divider = None
            source = StringProperty()


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_simple_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Set backup account",
                        type="simple",
                        items=[
                            Item(text="user01@gmail.com", source="user-1.png"),
                            Item(text="user02@gmail.com", source="user-2.png"),
                            Item(text="Add account", source="add-icon.png"),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-items.png
        :align: center

    With type 'confirmation'
    -----------------------

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.list import OneLineAvatarIconListItem

        KV = '''
        <ItemConfirm>
            on_release: root.set_icon(check)

            CheckboxLeftWidget:
                id: check
                group: "check"


        FloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_confirmation_dialog()
        '''


        class ItemConfirm(OneLineAvatarIconListItem):
            divider = None

            def set_icon(self, instance_check):
                instance_check.active = True
                check_list = instance_check.get_widgets(instance_check.group)
                for check in check_list:
                    if check != instance_check:
                        check.active = False


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_confirmation_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Phone ringtone",
                        type="confirmation",
                        items=[
                            ItemConfirm(text="Callisto"),
                            ItemConfirm(text="Luna"),
                            ItemConfirm(text="Night"),
                            ItemConfirm(text="Solo"),
                            ItemConfirm(text="Phobos"),
                            ItemConfirm(text="Diamond"),
                            ItemConfirm(text="Sirena"),
                            ItemConfirm(text="Red music"),
                            ItemConfirm(text="Allergio"),
                            ItemConfirm(text="Magic"),
                            ItemConfirm(text="Tic-tac"),
                        ],
                        buttons=[
                            MDFlatButton(
                                text="CANCEL", text_color=self.theme_cls.primary_color
                            ),
                            MDFlatButton(
                                text="OK", text_color=self.theme_cls.primary_color
                            ),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-confirmation.png
        :align: center

    :attr:`items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    type = OptionProperty(
        "alert", options=["alert", "simple", "confirmation", "custom"]
    )
    """
    Dialog type.
    Available option are `'alert'`, `'simple'`, `'confirmation'`, `'custom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'alert'`.
    """

    content_cls = ObjectProperty()
    """
    Custom content class.

    .. code-block::

        from kivy.lang import Builder
        from kivy.uix.boxlayout import BoxLayout

        from kivymd.app import MDApp
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.dialog import MDDialog

        KV = '''
        <Content>
            orientation: "vertical"
            spacing: "12dp"
            size_hint_y: None
            height: "120dp"

            MDTextField:
                hint_text: "City"

            MDTextField:
                hint_text: "Street"


        FloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_confirmation_dialog()
        '''


        class Content(BoxLayout):
            pass


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_confirmation_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Address:",
                        type="custom",
                        content_cls=Content(),
                        buttons=[
                            MDFlatButton(
                                text="CANCEL", text_color=self.theme_cls.primary_color
                            ),
                            MDFlatButton(
                                text="OK", text_color=self.theme_cls.primary_color
                            ),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-custom.png
        :align: center

    :attr:`content_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `'None'`.
    """

    _scroll_height = NumericProperty("28dp")
    _spacer_top = NumericProperty("24dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.size_hint == [1, 1] and DEVICE_TYPE == "mobile":
            self.size_hint = (None, None)
            self.width = dp(280)
        elif self.size_hint == [1, 1] and DEVICE_TYPE == "desktop":
            self.size_hint = (None, None)
            self.width = dp(560)

        if not self.title:
            self._spacer_top = 0

        if not self.buttons:
            self.ids.root_button_box.height = 0
        else:
            self.create_buttons()

        if self.type in ("simple", "confirmation"):
            if self.type == "confirmation":
                self.ids.spacer_top_box.add_widget(MDSeparator())
                self.ids.spacer_bottom_box.add_widget(MDSeparator())
            self.create_items()
        if self.type == "custom":
            if self.content_cls:
                self.ids.container.remove_widget(self.ids.scroll)
                self.ids.container.remove_widget(self.ids.text)
                self.ids.spacer_top_box.add_widget(self.content_cls)
                self._spacer_top = self.content_cls.height + dp(24)
                self.ids.spacer_top_box.padding = (0, "24dp", "16dp", 0)
        if self.type == "alert":
            self.ids.scroll.bar_width = 0

    def on_open(self):
        # TODO: Add scrolling text.
        self.height = self.ids.container.height

    def set_normal_height(self):
        self.size_hint_y = 0.8

    def get_normal_height(self):
        return (
                (Window.height * 80 / 100)
                - self._spacer_top
                - dp(52)
                - self.ids.container.padding[1]
                - self.ids.container.padding[-1]
                - 100
        )

    def edit_padding_for_item(self, instance_item):
        instance_item.ids._left_container.x = 0
        instance_item._txt_left_pad = "56dp"

    def create_items(self):
        self.ids.container.remove_widget(self.ids.text)
        height = 0

        for item in self.items:
            if issubclass(item.__class__, BaseListItem):
                height += item.height  # calculate height contents
                self.edit_padding_for_item(item)
                self.ids.box_items.add_widget(item)

        if height > Window.height:
            self.set_normal_height()
            self.ids.scroll.height = self.get_normal_height()
        else:
            self.ids.scroll.height = height

    def create_buttons(self):
        for button in self.buttons:
            if issubclass(button.__class__, BaseButton):
                self.ids.button_box.add_widget(button)


if DEVICE_IOS:
    Heir = BoxLayout
else:
    Heir = MDCard


# FIXME: Not work themes for iOS.
class BaseDialog(ThemableBehavior, ModalView):
    def set_content(self, instance_content_dialog):
        def _events_callback(result_press):
            self.dismiss()
            if result_press and self.events_callback:
                self.events_callback(result_press, self)

        if self.device_ios:  # create buttons for iOS
            self.background = self._background

            if isinstance(instance_content_dialog, ContentInputDialog):
                self.text_field = MDTextFieldRect(
                    pos_hint={"center_x": 0.5},
                    size_hint=(1, None),
                    multiline=False,
                    height=dp(33),
                    cursor_color=self.theme_cls.primary_color,
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(33)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )

            if self.text_button_cancel != "":
                anchor = "left"
            else:
                anchor = "center"
            box_button_ok = AnchorLayout(anchor_x=anchor)
            box_button_ok.add_widget(
                MDTextButton(
                    text=self.text_button_ok,
                    font_size="18sp",
                    on_release=lambda x: _events_callback(self.text_button_ok),
                )
            )
            instance_content_dialog.ids.box_buttons.add_widget(box_button_ok)

            if self.text_button_cancel != "":
                box_button_ok.anchor_x = "left"
                box_button_cancel = AnchorLayout(anchor_x="right")
                box_button_cancel.add_widget(
                    MDTextButton(
                        text=self.text_button_cancel,
                        font_size="18sp",
                        on_release=lambda x: _events_callback(
                            self.text_button_cancel
                        ),
                    )
                )
                instance_content_dialog.ids.box_buttons.add_widget(
                    box_button_cancel
                )

        else:  # create buttons for Android
            if isinstance(instance_content_dialog, ContentInputDialog):
                self.text_field = MDTextField(
                    size_hint=(1, None),
                    height=dp(48),
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(48)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )
                instance_content_dialog.ids.box_buttons.remove_widget(
                    instance_content_dialog.ids.sep
                )

            box_buttons = AnchorLayout(
                anchor_x="right", size_hint_y=None, height=dp(30)
            )
            box = BoxLayout(size_hint_x=None, spacing=dp(5))
            box.bind(minimum_width=box.setter("width"))
            button_ok = MDRaisedButton(
                text=self.text_button_ok,
                on_release=lambda x: _events_callback(self.text_button_ok),
            )
            box.add_widget(button_ok)

            if self.text_button_cancel != "":
                button_cancel = MDFlatButton(
                    text=self.text_button_cancel,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: _events_callback(
                        self.text_button_cancel
                    ),
                )
                box.add_widget(button_cancel)

            box_buttons.add_widget(box)
            instance_content_dialog.ids.box_buttons.add_widget(box_buttons)
            instance_content_dialog.ids.box_buttons.height = button_ok.height
            instance_content_dialog.remove_widget(
                instance_content_dialog.ids.sep
            )


# nome_museo,sito_web,statale_non_statale,omr,sistema_museale_territoriale,sistema_museale_urbano,
# sistema_museale_tematico,casa_museo,indirizzo,localita,ubicazione,cap,telefno,fax,email
class ListMDDialogMusei(BaseDialog):
    nome_museo = StringProperty("Dati Mancanti")
    sito_web = StringProperty("Dati Mancanti")
    statale_non_statale = StringProperty("Dati Mancanti")
    omr = StringProperty("Dati Mancanti")
    sistema_museale_territoriale = StringProperty("Dati Mancanti")
    sistema_museale_urbano = StringProperty("Dati Mancanti")
    sistema_museale_tematico = StringProperty("Dati Mancanti")
    casa_museo = StringProperty("Dati Mancanti")
    indirizzo = StringProperty("Dati Mancanti")
    localita = StringProperty("Dati Mancanti")
    ubicazione = StringProperty("Dati Mancanti")
    cap = StringProperty("Dati Mancanti")
    telefno = StringProperty("Dati Mancanti")
    fax = StringProperty("Dati Mancanti")
    email = StringProperty("Dati Mancanti")
    Facebook = StringProperty("Dati Mancanti")
    Twitter = StringProperty("Dati Mancanti")
    background = StringProperty('{}ios_bg_mod.png'.format(images_path))


#denominazione,tipologia,ente,tip_amministrativa,indirizzo,frazione,cap,telefono,fax,email,sito_web,Twitter,Facebook
class ListMDDialogBiblio(BaseDialog):
    denominazione = StringProperty("Dati Mancanti")
    tipologia = StringProperty("Dati Mancanti")
    ente = StringProperty("Dati Mancanti")
    tip_amministrativa = StringProperty("Dati Mancanti")
    indirizzo = StringProperty("Dati Mancanti")
    frazione = StringProperty("Dati Mancanti")
    cap = StringProperty("Dati Mancanti")
    telefono = StringProperty("Dati Mancanti")
    fax = StringProperty("Dati Mancanti")
    email = StringProperty("Dati Mancanti")
    sito_web = StringProperty("Dati Mancanti")
    Twitter = StringProperty("Dati Mancanti")
    Facebook = StringProperty("Dati Mancanti")
    background = StringProperty('{}ios_bg_mod.png'.format(images_path))


class MDInputDialog(BaseDialog):
    title = StringProperty("Title")
    hint_text = StringProperty()
    text_button_ok = StringProperty("Ok")
    text_button_cancel = StringProperty()
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.content_dialog = ContentInputDialog(
            title=self.title,
            hint_text=self.hint_text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(self.content_dialog)
        self.set_content(self.content_dialog)
        Clock.schedule_once(self.set_field_focus, 0.5)

    def set_field_focus(self, interval):
        self.text_field.focus = True


class MDDialog(BaseDialog):
    title = StringProperty("Title")
    text = StringProperty("Text dialog")
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty("Ok")
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content_dialog = ContentMDDialog(
            title=self.title,
            text=self.text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(content_dialog)
        self.set_content(content_dialog)


class ContentInputDialog(Heir):
    title = StringProperty()
    hint_text = StringProperty()
    text_button_ok = StringProperty()
    text_button_cancel = StringProperty()
    device_ios = BooleanProperty()


class ContentMDDialog(Heir):
    title = StringProperty()
    text = StringProperty()
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty()
    device_ios = BooleanProperty()
