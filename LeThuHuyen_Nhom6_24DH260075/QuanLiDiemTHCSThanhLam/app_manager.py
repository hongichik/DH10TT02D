from pages.login import LoginPage
from pages.register import RegisterPage
from pages.dashboard import DashboardPage
from pages.forgot import ForgotPage

class AppManager:
    def __init__(self, root):
        self.root = root
        self.current = None
        self.show_login()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def show_login(self):
        self.clear()
        self.current = LoginPage(self.root, self)

    def show_register(self):
        self.clear()
        self.current = RegisterPage(self.root, self)

    def show_dashboard(self):
        self.clear()
        self.current = DashboardPage(self.root, self)

    def show_forgot(self):
        self.clear()
        self.current = ForgotPage(self.root, self)