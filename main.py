from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.properties import StringProperty

# Classe personnalisée pour l'aperçu des polices dans le menu
class FontListItem(OneLineListItem):
    font_name = StringProperty()

# ENREGISTREMENT DES POLICES
fonts = [
    {"name": "Montserrat", "fn_regular": "assets/fonts/Montserrat.ttf"},
    {"name": "Orbitron", "fn_regular": "assets/fonts/Orbitron.ttf"},
    {"name": "Roboto", "fn_regular": "assets/fonts/Roboto.ttf"},
    {"name": "Playfair", "fn_regular": "assets/fonts/Playfair.ttf"},
    {"name": "OpenSans", "fn_regular": "assets/fonts/OpenSans.ttf"},
]

for font in fonts:
    try:
        LabelBase.register(**font)
    except Exception as e:
        print(f"Erreur sur {font['name']}: {e}")

class CanvaScreen(MDScreen):
    menu = None

    def open_font_menu(self, button):
        font_names = ["Montserrat", "Orbitron", "Roboto", "Playfair", "OpenSans"]
        
        # On crée les items du menu avec l'aperçu visuel
        menu_items = [
            {
                "viewclass": "FontListItem",
                "text": name,
                "font_name": name, 
                "on_release": lambda x=name: self.apply_font(x),
            } for name in font_names
        ]
        
        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def apply_font(self, font_name):
        # Change la police du label qui a l'id 'label_canvas'
        if "label_canvas" in self.ids:
            self.ids.label_canvas.font_name = font_name
        
        if self.menu:
            self.menu.dismiss()

class IdeaSparkApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    IdeaSparkApp().run()
