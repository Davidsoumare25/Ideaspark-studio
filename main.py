from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.uix.behaviors import DragBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import colorsys

# Interface Canva Ultra-Stable
KV = """
MDFloatLayout:
    md_bg_color: 0.05, 0.05, 0.1, 1

    MDTopAppBar:
        title: "IdeaSpark : Studio Pro"
        pos_hint: {"top": 1}
        elevation: 4
        right_action_items: [["image-plus", lambda x: app.change_photo()]]

    # ZONE DE TRAVAIL (CANVAS)
    MDCard:
        id: cover
        size_hint: None, None
        size: ("280dp", "420dp") if app.is_portrait else ("420dp", "280dp")
        pos_hint: {"center_x": .5, "center_y": .6}
        md_bg_color: app.bg_color
        radius: [15]
        elevation: 8
        clip_children: False # Crucial pour que le texte ne disparaisse pas

        MDFloatLayout:
            # IMAGE DE FOND (DRAGGABLE)
            DragImage:
                size_hint: None, None
                size: app.img_scale, app.img_scale
                pos: 50, 100
                drag_rectangle: [self.x, self.y, self.width, self.height]
                FitImage:
                    source: app.current_img
                    radius: [10]

            # TITRE (TOUJOURS AU PREMIER PLAN)
            DragLabel:
                text: app.ebook_title if app.ebook_title else "MON TITRE"
                size_hint: None, None
                size: "260dp", "100dp" # Largeur fixe pour éviter le texte vertical
                pos: 10, 280
                drag_rectangle: [self.x, self.y, self.width, self.height]
                halign: "center"
                font_style: app.font_style
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True

    # BARRE D'OUTILS (BAS)
    MDCard:
        size_hint_y: 0.3
        radius: [25, 25, 0, 0]
        md_bg_color: 0.1, 0.1, 0.15, 1
        orientation: 'vertical'
        padding: "15dp"
        spacing: "10dp"

        MDTextField:
            hint_text: "Taper le titre..."
            on_text: app.ebook_title = self.text
            mode: "rectangle"

        MDBoxLayout:
            adaptive_height: True
            spacing: "10dp"
            MDRaisedButton:
                text: "STYLE"
                on_release: app.next_style()
            MDRaisedButton:
                text: "PAYSAGE" if app.is_portrait else "PORTRAIT"
                on_release: app.is_portrait = not app.is_portrait

        MDSlider:
            min: 0
            max: 1
            on_value: app.update_color(self.value)

<DragLabel@DragBehavior+MDLabel>
<DragImage@DragBehavior+MDCard>
"""

class IdeaSparkStudio(MDApp):
    bg_color = ListProperty([0.1, 0.5, 0.9, 1])
    ebook_title = StringProperty("BUSINESS")
    current_img = StringProperty("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500")
    img_scale = NumericProperty(200)
    is_portrait = BooleanProperty(True)
    font_style = StringProperty("H4")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def update_color(self, val):
        rgb = colorsys.hsv_to_rgb(val, 0.7, 0.8)
        self.bg_color = [rgb[0], rgb[1], rgb[2], 1]

    def next_style(self):
        styles = ["H3", "H4", "H5", "H6", "Button"]
        idx = styles.index(self.font_style)
        self.font_style = styles[(idx + 1) % len(styles)]

    def change_photo(self):
        self.current_img = "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=500"

if __name__ == "__main__":
    IdeaSparkStudio().run()

