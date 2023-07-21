from Helpers.Voodoo import *


def test_herokuapp_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    # Quick Page Validation

    Validate.title("The Internet", page)
    Validate.text("Login Page", page)

    # Fill fields

    Interact.fill_by_label("Username", "tomsmith", page)
    Interact.fill_by_label("Password", "SuperSecretPassword!", page)
    Interact.click_button("Login", page)

    # Validate Login was Successful

    Validate.id("flash", page)
