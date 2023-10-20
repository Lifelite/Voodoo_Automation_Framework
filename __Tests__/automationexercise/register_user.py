from Helpers.Voodoo import *


def test_register_user(page: Page):
    v = Validate(page)
    i = Interact(page)

    i.navigate_to_url("https://automationexcercise.com")
    v.text("Full-Fledged practice website for Automation Engineers")
    v.title("Automation Exercise")
    i.click_by_label(" Signup / Login")
    v.text("New User Signup!")
    