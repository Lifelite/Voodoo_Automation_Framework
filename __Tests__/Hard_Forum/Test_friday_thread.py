from datetime import datetime

from Helpers.Voodoo import *


def test_post_friday_thread(page: Page):
    validate = Validate(page)
    interact = Interact(page)
    # Nav to page
    interact.navigate_to_url("https://hardforum.com/")

    # Validate page load

    # Log in with user
    uName = "lifelite"
    uPassword = ""

    interact.click_by_role("link", "Log in", page)
    interact.fill_by_label("Your name or email address", uName, page)
    interact.click_by_label("Password", page)
    interact.fill_by_label("Password", uPassword, page)
    interact.click_button("Log in", page)

    interact.navigate_to_url("https://hardforum.com/forums/general-mayhem.106/")
    validate.url_matches("https://hardforum.com/forums/general-mayhem.106/")

    interact.click_by_role("link", "Post thread")
    validate.url_matches("https://hardforum.com/forums/general-mayhem.106/post-thread")

    # Fill Thread Title

    thread_body = """FILL IN HERE"""

    c_date = datetime.today()
    f_date = c_date.strftime("%m/%d/%y")
    thread_name = ["Friday ", f_date]
    interact.fill_by_placeholder("Thread title", thread_name)
    interact.fill_by_locator(".fr-element", thread_body)

    interact.click_button("Post thread")
