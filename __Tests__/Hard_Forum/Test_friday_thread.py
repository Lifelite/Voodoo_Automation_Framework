from datetime import datetime

from Helpers.Voodoo import *


def test_post_friday_thread(page: Page):
    # Nav to page
    page.goto("https://hardforum.com/")

    # Validate page load

    # Log in with user
    uName = "lifelite"
    uPassword = secret1

    Interact.click_by_role("link", "Log in", page)
    Interact.fill_by_label("Your name or email address", uName, page)
    Interact.click_by_label("Password", page)
    Interact.fill_by_label("Password", uPassword, page)
    Interact.click_button("Log in", page)

    page.goto("https://hardforum.com/forums/general-mayhem.106/")
    Validate.url_matches("https://hardforum.com/forums/general-mayhem.106/", page)

    Interact.click_by_role("link", "Post thread", page)
    Validate.url_matches("https://hardforum.com/forums/general-mayhem.106/post-thread", page)

    # Fill Thread Title

    thread_body = """FILL IN HERE"""

    c_date = datetime.today()
    f_date = c_date.strftime("%m/%d/%y")
    thread_name = ["Friday ", f_date]
    Interact.fill_by_placeholder("Thread title", thread_name, page)
    Interact.fill_by_locator(".fr-element", thread_body, page)

    Interact.click_button("Post thread", page)
