from Helpers.Voodoo import Interact, Validate

i = Interact()

class Check:

    def __init__(self, page):
        super().__init__(page)



class Do:

    def __init__(self, page):
        super().__init__(page)

    def signup(self):
        Interact.navigate_to_url("https://automationexcercise.com")
        Validate.text("Full-Fledged practice website for Automation Engineers")
        Validate.title("Automation Exercise")
        Interact.click_by_label()

