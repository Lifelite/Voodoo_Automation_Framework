from datetime import datetime

from Helpers.Voodoo import *


def post_friday_thread(date, page: Page):
    # Nav to page
    page.goto("https://hardforum.com/forums/general-mayhem.106/")

    # Validate page load

    Validate.title("Log in | [H]ard|Forum", page)
    Validate.text("Log in", page)

    # Log in with user

    Interact.fill_by_label("login", uName, page)
    Interact.fill_by_label("password", uPassword, page)
    Interact.click_button("Login", page)
    Validate.url_matches("https://hardforum.com/forums/general-mayhem.106/", page)

    # Start New Thread

    Interact.click_button("Post thread", page)
    Validate.url_matches("https://hardforum.com/forums/general-mayhem.106/post-thread", page)

    # Fill Thread Title

    c_date = datetime.today()
    c_date.strftime("%m/%d/%y")
    thread_name = str(["Friday", c_date])
    Interact.fill_by_label("Thread title", thread_name, page)

    # Compose Thread

    thread_body = "Fill Stuff here"
    Interact.fill_by_role("dir", "ltr", thread_body, page)
