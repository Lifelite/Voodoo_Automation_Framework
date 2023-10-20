from datetime import datetime
from Helpers.Voodoo import *


def test_page_submission(page: Page):
    v = Validate(page)
    i = Interact(page)


    i.navigate_to_url("http://localhost:5173/")


    v.text("Jeremy Huntsman")

    i.click_button("Event Information")
    # v.text("Event Information")
    # v.button_text("Gift")
    i.navigate_to_url("http://localhost:5173/")

    i.click_button("Join The Celebration")

    i.fill_by_label("Name", "Jeremy Test")
    i.fill_by_label("Email", "AlmostSept@none.com")
    i.fill_by_label("Message", f"it is {datetime.now()} mmkay")
    i.click_by_label("I'll Be There!")
    i.click_button("Send")


