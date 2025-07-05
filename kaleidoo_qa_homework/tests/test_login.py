import pytest
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_login_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login(USERNAME, PASSWORD)

    assert "wp-admin" in page.url or "התנתק" in page.content()

@pytest.mark.parametrize("username, password", [
    ("wronguser", "wrongpass"),
    ("", ""),
    ("tester", ""),
    ("", "tester123!@#qwe")
])
def test_login_failure(page, username, password):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    assert "error" in page.content().lower() or "login_error" in page.content().lower()