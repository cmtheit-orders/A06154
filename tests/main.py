from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):
    # When adding widgets, we need to specify the height manually
    # (disabling the size_hint_y) so the dropdown can calculate
    # the area it needs.
    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
# for each button, attach a callback that will call the select() method # on the dropdown. We'll pass the text of the button as the data of the # selection.
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    # then add the button inside the dropdown
    dropdown.add_widget(btn) # create a big main button
mainbutton = Button(text='Hello', size_hint=(None, None))
# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the # mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton.bind(on_release=dropdown.open)
# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
dropdown.dismiss()
class TestApp(App):
    def build(self):
        root = GridLayout()
        root.size = (1600, 1200)
        root.cols = 1
        dropdown.size = root.size
        dropdown.pos = (0, 0)
        root.add_widget(mainbutton)
        root.add_widget(dropdown)
        return root
TestApp().run()