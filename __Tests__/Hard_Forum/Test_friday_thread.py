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

    thread_body = """
        Fribot once again posting this thread you lazy assholes.  
        
        Lifelite implemented a language model api to the thread creator and his dumbass already hit the billing threshold, so no generated posts yet.
        This weekend, soon to be mother in law is visiting, her and the fiancee are out shopping today, tomorrow we all should be going to Oktoberfest, probably getting hammered.
        Sunday, probably being lazy and just hanging out.
        
        How's the rest of you meatbags' weekend look?
     """

    c_date = datetime.today()
    f_date = c_date.strftime("%m/%d/%y")
    thread_name = f"Automated Friday {f_date}"
    interact.click_by_placeholder("Thread title")
    interact.type_with_keyboard(str(thread_name))
    interact.fill_by_locator(".fr-element", thread_body)

    interact.click_button("Post thread")
