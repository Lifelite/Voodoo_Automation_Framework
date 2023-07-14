import re
from playwright.sync_api import Page, expect


class Validate:

    @classmethod
    def text(cls, etext, page: Page):
        element = expect(page.get_by_text(etext))
        element.to_be_visible()

    @classmethod
    def label(cls, label, page: Page):
        element = expect(page.get_by_label(label))
        element.to_be_visible()

    @classmethod
    def id(cls, id, page: Page):
        locator = expect(page.locator('id=' + id))
        locator.to_be_visible()

    @classmethod
    def title(cls, title, page: Page):
        expect(page).to_have_title(re.compile(title))

    @classmethod
    def button(cls, name, page: Page):
        element = expect(page.get_by_role("button", name=name))
        element.to_be_visible()


class Interact:

    @classmethod
    def fill_by_label(cls, label, fill, page: Page):
        page.get_by_label(label).fill(fill)

    @classmethod
    def click_button(cls, button, page: Page):
        page.get_by_role("button", name=button).click()
