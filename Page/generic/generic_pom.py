from Helpers.Voodoo import *


class Login:

    @classmethod
    def generic_login(cls, uName, uPassword, page: Page):
        Interact.fill_by_label("Username", uName, page)
        Interact.fill_by_label("Password", uPassword, page)


