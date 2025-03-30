"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward, first version: 11/07/2016
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self,instance=None):
        """Create buttons from data and add them to the GUI."""
        names=['Alice','Charlie','Bob','Delilah','John','Isabel','Constantine']
        for name in names:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.on_button_click)
            self.root.ids.main_box.add_widget(temp_button)

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.main_box.clear_widgets()

    def on_button_click(self,instance):
        """To print to the console when dynamically modified button is clicked."""
        self.status_text=f"You clicked on {instance.text} button."

DynamicWidgetsApp().run()
