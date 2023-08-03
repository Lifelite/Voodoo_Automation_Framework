import time

from Helpers.VD_Connectors import Database
from Helpers.Voodoo import *
from Helpers.MySQL import Query
import time


def test_herokuapp_login(page: Page):
    validate = Validate(page)
    interact = Interact(page)
    q = Query(Database)
    # Retrieve Test Data using MySQL
    creds = q.credentials("herokuapp")
    uname = creds[0]
    upassword = creds[1]

    interact.navigate_to_url("https://the-internet.herokuapp.com/login")

    # Quick Page Validation

    validate.title("The Internet")
    validate.text("Login Page")

    # Fill fields

    interact.fill_by_label("Username", uname)
    interact.fill_by_label("Password", upassword)
    interact.click_button("Login")

    # Validate Login was Successful

    validate.id("flash")
