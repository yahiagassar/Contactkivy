import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore

kivy.require('1.11.1')

class MyApp(App):
    def build(self):
        self.store = JsonStore('data.json')
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.name_input = TextInput(hint_text='Enter Name', multiline=False)
        self.phone_input = TextInput(hint_text='Enter Phone Number', multiline=False)
        self.amount_input = TextInput(hint_text='Enter Amount', multiline=False)
        
        self.save_button = Button(text='Save', on_press=self.save_data)
        self.search_input = TextInput(hint_text='Search by Name', multiline=False)
        self.search_button = Button(text='Search', on_press=self.search_data)
        self.result_label = Label(text='', size_hint_y=None, height=44)
        
        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(self.amount_input)
        self.layout.add_widget(self.save_button)
        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.search_button)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def save_data(self, instance):
        name = self.name_input.text
        phone = self.phone_input.text
        amount = self.amount_input.text
        
        if name and phone and amount:
            self.store.put(name, phone=phone, amount=amount)
            self.clear_inputs()
            self.result_label.text = 'Data saved successfully!'
        else:
            self.result_label.text = 'Please fill all fields.'

    def search_data(self, instance):
        name = self.search_input.text
        if self.store.exists(name):
            phone = self.store.get(name)['phone']
            amount = self.store.get(name)['amount']
            self.result_label.text = f'Found: {name}, Phone: {phone}, Amount: {amount}'
        else:
            self.result_label.text = 'No data found.'

    def clear_inputs(self):
        self.name_input.text = ''
        self.phone_input.text = ''
        self.amount_input.text = ''
        self.search_input.text = ''

if __name__ == '__main__':
    MyApp().run()
