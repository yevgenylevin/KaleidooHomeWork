import os
import time
from pages.base_page import BasePage

class PublishAdPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.asset_type_select = 'select[name="asset_type"]'
        self.asset_status_select = 'select[name="asset_status"]'
        self.city_select = 'select[name="city"]'
        self.street_number_input = 'input[name="street_number"]'
        self.floor_input = 'input[name="floor"]'
        self.floors_input = 'input[name="floors"]'
        self.room_num_select = 'select[name="room_num"]'
        self.terrace_select = 'select[name="terrace"]'
        self.parking_select = 'select[name="_parking"]'
        self.built_mr_input = 'input[name="built_mr"]'
        self.built_mr_input = 'input[name="built_mr"]'
        self.elevator_select = 'select[name="elevator_1"]'
        self.garden_area_input = 'input[name="garden_mr"]'
        self.page.click('label[aria-label="ריהוט"]')
        self.credits_input = 'input[name="credits"]'
        self.price_input = 'input[name="price"]'
        self.date_start_input = 'input[name="date_start"]'
        self.image_upload_input = 'input[type="file"][name="gallery[]"]'
        self.full_name_input = 'input[name="name_full"]'
        self.phone_input = 'input[name="phone_number"]'
        self.next_button = 'button[data-action="next"]'
        self.submit_button = 'button.publish-asset'

    def select_asset_type(self, asset_type):
        self.page.select_option(self.asset_type_select, label=asset_type)

    def select_asset_status(self, status):
        self.page.select_option(self.asset_status_select, label=status)

    def select_city(self, city_name):
        self.page.select_option(self.city_select, label=city_name)

    def fill_street_number(self, number):
        self.page.fill(self.street_number_input, number)

    def fill_floor(self, floor_value):
        self.page.fill(self.floor_input, floor_value)

    def fill_total_floors(self, total_floors):
        self.page.fill(self.floors_input, total_floors)

    def select_room_num(self, room_num):
        self.page.select_option(self.room_num_select, value=str(room_num))

    def select_terrace(self, terrace_value):
        self.page.select_option(self.terrace_select, value=str(terrace_value))

    def select_parking(self, parking_value):
        self.page.select_option(self.parking_select, value=str(parking_value))

    def fill_built_area(self, square_meters):
        self.page.fill(self.built_mr_input, str(square_meters))

    def select_elevator(self, elevator_option):
        self.page.select_option(self.elevator_select, value=elevator_option)

    def fill_garden_area(self, garden_area):
        self.page.fill(self.garden_area_input, str(garden_area))

    def select_asset_characteristic(self, label_text: str):
        self.page.locator(f"label[aria-label='{label_text}']").click()
        
    def fill_credits(self, credits_value):
        self.page.fill(self.credits_input, str(credits_value))

    def fill_price(self, price_value):
        self.page.fill(self.price_input, str(price_value))

    def set_entry_date(self, date_str: str):
        self.page.evaluate(
            """({ selector, value }) => {
                const input = document.querySelector(selector);
                if (input) {
                    input.removeAttribute('readonly');
                    input.value = value;
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                }
            }""",
            {
                "selector": self.date_start_input,
                "value": date_str
            }
    )
   
    def upload_images(self, image_paths: list[str]):
        abs_paths = [os.path.abspath(p) for p in image_paths]
        file_input = self.page.locator('input[name="pictures"]')
    
        file_input.wait_for(state="attached", timeout=10000)
    
        file_input.set_input_files(abs_paths)

    def fill_full_name(self, full_name):
        self.page.fill(self.full_name_input, full_name)

    def fill_phone_number(self, phone_number):
        self.page.fill(self.phone_input, phone_number)

    def click_next(self):
        next_button = self.page.locator('button[data-action="next"]').first
        next_button.wait_for(state="visible", timeout=5000)
        assert next_button.is_enabled(), "'Next' button is disabled"
        time.sleep(1)  # optional delay
        next_button.click()

    def submit_ad(self):
        # JavaScript click as last resort
        self.page.evaluate("""() => {
            const btn = document.querySelector('button.publish-asset');
            if (btn) btn.click();
        }""")






