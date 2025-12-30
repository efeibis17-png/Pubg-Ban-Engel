from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class PUBGApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        title = Label(text='PUBG Anti-Ban Sistemi', font_size='24sp', bold=True)
        status = Label(text='Durum: Hazır', color=(0, 1, 0, 1))
        btn = Button(text='Korumayı Başlat', size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: self.update_status(status))
        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(btn)
        return layout

    def update_status(self, label):
        label.text = 'Durum: Koruma Aktif!'
        label.color = (0, 1, 1, 1)

if __name__ == '__main__':
    PUBGApp().run()
