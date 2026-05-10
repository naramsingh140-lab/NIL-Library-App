from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.clock import Clock
from kivy.core.window import Window
import random
import time

# System UI Lockdown
Window.clearcolor = (0, 0, 0, 1)

KV = '''
ScreenManager:
    transition: NoTransition()
    SplashScreen:
    LockScreen:
    MainDashboard:
    AdminPortal:

<SplashScreen>:
    name: 'splash'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        Widget:
        Label:
            text: "N"
            font_size: '150sp'
            color: 0, 1, 1, 1
        Label:
            text: "NARAM LOGIC"
            font_size: '20sp'
            color: 0, 1, 1, 0.5
            bold: True
        Widget:
        Label:
            text: "© 2026 NARAM LOGIC"
            font_size: '12sp'
            color: 0, 1, 1, 0.2

<LockScreen>:
    name: 'lock'
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 30
        Label:
            text: "KERNEL_LOCKED"
            font_size: '28sp'
            color: 0, 1, 1, 1
            bold: True
        TextInput:
            id: vault_input
            password: True
            multiline: False
            hint_text: "INPUT AUTH-KEY"
            background_color: 0, 0, 0, 1
            foreground_color: 0, 1, 1, 1
            cursor_color: 0, 1, 1, 1
            size_hint_y: None
            height: 60
            padding: 15
        Button:
            text: "INITIALIZE_CORE"
            size_hint_y: None
            height: 80
            background_color: 0, 1, 1, 1
            color: 0, 0, 0, 1
            bold: True
            on_release: root.verify_access()
        Label:
            text: root.status_msg
            color: 1, 0, 0, 1 if "INVALID" in self.text else (0, 1, 1, 0.3)

<MainDashboard>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: "NIL-LIBRARY DASHBOARD"
            size_hint_y: None
            height: 100
            color: 0, 1, 1, 1
            bold: True
        Label:
            text: root.session_info
            color: 0, 1, 1, 0.5
        Button:
            text: "ADMIN_MENU"
            opacity: 1 if root.is_master else 0
            size_hint_y: None
            height: 60
            on_release: app.root.current = 'admin'
        Widget:
        Button:
            text: "TERMINATE_SESSION"
            size_hint_y: None
            height: 60
            background_color: 0.5, 0, 0, 1
            on_release: root.logout()

<AdminPortal>:
    name: 'admin'
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 20
        Label:
            text: "GUEST KEY MANAGER"
            bold: True
            color: 0, 1, 1, 1
        TextInput:
            id: label_input
            hint_text: "GUEST_NAME"
            size_hint_y: None
            height: 50
        Button:
            text: "GENERATE_TOKEN"
            background_color: 0, 1, 1, 1
            color: 0, 0, 0, 1
            on_release: root.generate_token()
        ScrollView:
            BoxLayout:
                id: token_list
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: "EXIT_ADMIN"
            on_release: app.root.current = 'dashboard'
'''

class SplashScreen(Screen):
    def on_enter(self): Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'lock'), 3)

class LockScreen(Screen):
    status_msg = StringProperty("SYSTEM_IDLE")
    def verify_access(self):
        val = self.ids.vault_input.text
        if val == "NIL-77-PCM-OMEGA-INFINITY":
            self.manager.get_screen('dashboard').is_master = True
            self.manager.get_screen('dashboard').session_info = "ROOT: MASTER ACCESS"
            self.manager.current = 'dashboard'
        else:
            self.status_msg = "INVALID_CREDENTIALS"

class MainDashboard(Screen):
    is_master = BooleanProperty(False)
    session_info = StringProperty("")
    def logout(self): self.manager.current = 'lock'

class AdminPortal(Screen):
    tokens = []
    def generate_token(self):
        t = f"NIL-{random.randint(1000, 9999)}"
        self.tokens.append(t)
        self.ids.token_list.add_widget(Button(text=f"TOKEN: {t}", size_hint_y=None, height=50))

class NIL_App(App):
    def build(self): return Builder.load_string(KV)

if __name__ == '__main__':
    NIL_App().run()