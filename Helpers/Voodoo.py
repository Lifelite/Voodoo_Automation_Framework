import re

import playwright.sync_api
from playwright.sync_api import Page, expect, sync_playwright, APIRequest, APIRequestContext
import Data
import json


class Validate:

    def __init__(self, page, impl_obj: Any):
        super().__init__(impl_obj)
        self.page = page

    @classmethod
    def text(cls, etext, page):
        element = expect(page.get_by_text(etext))
        element.to_be_visible()

    @classmethod
    def label(cls, label, page):
        element = expect(page.get_by_label(label))
        element.to_be_visible()

    @classmethod
    def id(cls, id, page):
        locator = expect(page.locator('id=' + id))
        locator.to_be_visible()

    @classmethod
    def title(cls, title, page):
        expect(page).to_have_title(re.compile(title))

    @classmethod
    def button_enabled(cls, name, page):
        element = expect(page.get_by_role("button", name=name))
        element.to_be_visible()
        element.to_be_enabled()

    @classmethod
    def text_matches(cls, locator, text, page):
        expect(locator).to_have_text(text)

    @classmethod
    def box_is_checked(cls, locator, page):
        expect(locator).to_be_checked()

    @classmethod
    def url_matches(cls, url, page):
        expect(page).to_have_url(url)


class Interact:

    @classmethod
    def fill_by_label(cls, label, fill, page: Page):
        page.get_by_label(label).fill(fill)

    @classmethod
    def click_button(cls, button, page: Page):
        page.get_by_role("button", name=button).click()

    @classmethod
    def specific_button_click(cls, button, number, page: Page):
        page.get_by_role("button", name=button).nth(number).click()

    @classmethod
    def label_check_box(cls, label, page: Page):
        page.get_by_label(label).check()

    @classmethod
    def fill_by_role(cls, role, name, fill, page: Page):
        page.get_by_role(role, name=name).fill(fill)


class JsonParse:

    @classmethod
    def load_data(cls, data):
        json.loads("testdata.json")


class API:

    @classmethod
    def api_push(cls, url, call, data, request: APIRequest):
        with sync_playwright() as p:
            api_request_context = p.request.new_context(
                base_url=url)
        response = api_request_context.post(
            call,
            headers={
                "Accept": "application/json"
            },
            data=data
        )
        assert response.ok
