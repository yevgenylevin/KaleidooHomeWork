from utils.config import BASE_URL
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = 'input[id="user_login"]'
        self.password_input = 'input[id="user_pass"]'
        self.login_button = 'input[id="wp-submit"]'

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_load_state("networkidle")