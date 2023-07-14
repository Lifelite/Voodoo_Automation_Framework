import logging

from playwright.sync_api import Page


class Element:
    @classmethod
    def text(cls, text_name, page: Page):
        page.get_by_text(text_name)

    @classmethod
    def label(cls, label_name, page: Page):
        page.get_by_label(label_name)

    @classmethod
    def button(cls, button_name, page: Page):
        page.get_by_role("button", name=button_name)
