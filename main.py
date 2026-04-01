from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.core.text import LabelBase

# 1. ENREGISTREMENT DES POLICES
# On le fait en dehors de la classe pour que ce soit chargé dès le début
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
        print(f"Erreur chargement {font['name']}: {e}")

class CanvaScreen(MDScreen):
    menu = None

    def open_font_menu(self, button):
        # Liste des noms de polices pour le menu
        font_names = ["Montserrat", "Orbitron", "Roboto", "Playfair", "OpenSans"]
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": name,
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
        # On change la police de l'élément texte sur le canva
        # Vérifie que tu as bien 'id: label_canvas' dans ton fichier .kv
        if "label_canvas" in self.ids:
            self.ids.label_canvas.font_name = font_name
        
        if self.menu:
            self.menu.dismiss()

class IdeaSparkApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        
        # Charge ton fichier KV ici
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    IdeaSparkApp().run()
        styles = ["H3", "H4", "H5", "H6", "Button"]
        idx = styles.index(self.font_style)
        self.font_style = styles[(idx + 1) % len(styles)]

    def change_photo(self):
        self.current_img = "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=500"

if __name__ == "__main__":
    IdeaSparkStudio().run()

