import pytest
from pages.login_page import LoginPage
from pages.apartment_listings_page import ApartmentListingsPage
from pages.publish_ad_page import PublishAdPage
from utils.config import USERNAME, PASSWORD, BASE_URL


def test_publish_ad_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login(USERNAME, PASSWORD)

    listings_page = ApartmentListingsPage(page)
    listings_page.accept_policy()
    listings_page.go_to_create_listing()

    publish = PublishAdPage(page)

    asset_type = "דירה"
    asset_status = "משופץ"
    city = "כרמיאל"
    street_number = "20"
    floor = "1"
    floors = "4"
    room_num = 3
    terraces = "1"
    parking = "ללא"
    built_area = "60"
    elevator = "ללא"
    credits = "12"
    price = 5000
    entry_date = "01/08/2025"
    image_path = "tests/data/Among-Us-Step-10.png"
    full_name = "Yevgeny Levin"
    phone_number = "0501234567"

    publish.select_asset_type(asset_type)
    publish.select_asset_status(asset_status)
    publish.select_city(city)
    publish.fill_street_number(street_number)
    publish.click_next()
    publish.fill_floor(floor)
    publish.fill_total_floors(floors)
    publish.select_room_num(room_num)
    publish.select_terrace(terraces)
    publish.select_parking(parking)
    publish.fill_built_area(built_area)
    publish.select_elevator(elevator)
    publish.click_next()
    publish.select_asset_characteristic("ריהוט")
    publish.click_next()
    publish.fill_credits(credits)
    publish.fill_price(price)
    publish.set_entry_date(entry_date)
    publish.click_next()
    publish.upload_images([image_path])
    publish.click_next()
    publish.fill_full_name(full_name)
    publish.fill_phone_number(phone_number)
    publish.submit_ad()
    assert page.locator("text=המודעה פורסמה בהצלחה").is_visible()



 

    

