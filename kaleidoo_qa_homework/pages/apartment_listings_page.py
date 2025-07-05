from pages.base_page import BasePage

class ApartmentListingsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.accept_policy_button = 'a:has-text("אני מסכים לתנאי השימוש באתר")'
        self.create_listing_button = 'a:has-text("פרסם מודעה")'

    def accept_policy(self):
        if self.page.is_visible(self.accept_policy_button, timeout=5000):
            self.page.click(self.accept_policy_button)

    def go_to_create_listing(self):
        self.page.wait_for_selector(self.create_listing_button, timeout=10000)
        self.page.click(self.create_listing_button)
