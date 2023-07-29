from Helpers.Voodoo import *


def test_herokuapp_login(page: Page):
    validate = Validate(page)
    interact = Interact(page)

    interact.navigate_to_url("https://the-internet.herokuapp.com/login")

    # Quick Page Validation

    validate.title("The Internet")
    validate.text("Login Page")

    # Fill fields

    interact.fill_by_label("Username", "tomsmith")
    interact.fill_by_label("Password", "SuperSecretPassword!")
    interact.click_button("Login")

    # Validate Login was Successful

    validate.id("flash")
