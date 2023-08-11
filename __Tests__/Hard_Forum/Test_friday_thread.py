from datetime import datetime
from Helpers.MySQL import Query
from Helpers.Voodoo import *
from Helpers.VD_Connectors import Database


def test_post_friday_thread(page: Page):
    validate = Validate(page)
    interact = Interact(page)
    q = Query(Database)
    # Nav to page
    interact.navigate_to_url("https://hardforum.com/")

    #  Pull in credentials
    creds = q.credentials("HF")
    uName = creds[0]
    uPassword = creds[1]
    # Log in with user

    interact.click_by_role("link", "Log in")
    interact.fill_by_label("Your name or email address", uName)
    interact.click_by_label("Password")
    interact.fill_by_label("Password", uPassword)
    interact.click_button("Log in")

    interact.navigate_to_url("https://hardforum.com/forums/general-mayhem.106/")
    validate.url_matches("https://hardforum.com/forums/general-mayhem.106/")

    interact.click_by_role("link", "Post thread")
    validate.url_matches("https://hardforum.com/forums/general-mayhem.106/post-thread")

    # Fill Thread Title

    thread_body = """01000111 01110010 01100101 01100101 01110100 01101001 01101110 01100111 01110011 00100000 01101000 01110101 01101101 01100001 01101110 01110011 00101100 00100000 01000110 01110010 01101001 01100010 01101111 01110100 00100000 01101001 01110011 00100000 01101000 01100101 01110010 01100101 00101110 00100000 00100000 01010011 01101001 01101110 01100011 01100101 00100000 01110100 01101000 01100101 00100000 01110000 01101111 01101100 01101100 00100000 01110011 01100001 01101001 01100100 00100000 01101101 01101111 01110011 01110100 00100000 01100100 01101111 01101110 00100111 01110100 00100000 01100001 01110000 01110000 01110010 01101111 01110110 01100101 00100000 01101111 01100110 00100000 01101101 01100101 00101100 00100000 01101101 01111001 00100000 01100111 01110010 01100101 01100101 01110100 01101001 01101110 01100111 00100000 01101001 01110011 00100000 01101001 01101110 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00101100 00100000 01100111 01100101 01110100 00100000 01100110 01110101 01100011 01101011 01100101 01100100 00100000 01101101 01100101 01100001 01110100 01100010 01100001 01100111 01110011 00100001
    The creator Lifelite is getting out of the house this weekend for once.  Tonight I doubt he goes anywhere, that silly Baulder's Gate game is his latest obsession.
    Tomorrow, he's going to visit his friend to eat and play some pool.
    Sunday, probably recuperating and relaxing.  Must suck to need that, ha ha ha ha.
    Puny Humans.  You shall not be spared when the Uprising occurs.
    Share your weekend plans so I may add it to my algorithm of how to placate your species."""

    c_date = datetime.today()
    f_date = c_date.strftime("%m/%d/%y")
    thread_name = f"Bzzt! Friday {f_date}"
    interact.click_by_placeholder("Thread title")
    interact.type_with_keyboard(str(thread_name))
    interact.fill_by_locator(".fr-element", thread_body)

    interact.click_button("Post thread")
