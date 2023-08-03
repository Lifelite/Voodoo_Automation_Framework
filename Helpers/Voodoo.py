import re

from playwright.sync_api import Page, expect, sync_playwright, APIRequest, APIRequestContext
import Data
import json


class Validate:

    def __init__(self, page):
        self.page = page

    def text(self, etext):
        element = expect(self.page.get_by_text(etext))
        element.to_be_visible()

    def label(self, label):
        element = expect(self.page.get_by_label(label))
        element.to_be_visible()

    def id(self, id):
        locator = expect(self.page.locator('id=' + id))
        locator.to_be_visible()

    def title(self, title):
        expect(self.page).to_have_title(re.compile(title))

    def button_enabled(self, name):
        element = expect(self.page.get_by_role("button", name=name))
        element.to_be_visible()
        element.to_be_enabled()

    @staticmethod
    def text_matches(locator, text):
        expect(locator).to_have_text(text)

    @staticmethod
    def box_is_checked(locator):
        expect(locator).to_be_checked()

    def url_matches(self, url):
        expect(self.page).to_have_url(url)


class Interact:

    def __init__(self, page):
        self.page = page

    def fill_by_label(self, label, fill):
        self.page.get_by_label(label).fill(fill)

    def click_button(self, button):
        self.page.get_by_role("button", name=button).click()

    def specific_button_click(self, button, number):
        self.page.get_by_role("button", name=button).nth(number).click()

    def label_check_box(self, label):
        self.page.get_by_label(label).check()

    def fill_by_role(self, role, name, fill):
        self.page.get_by_role(role, name=name).fill(fill)

    def click_by_role(self, role, name):
        self.page.get_by_role(role, name=name).click()

    def fill_by_id(self, id, fill):
        locator = self.page.locator('id=' + id)
        locator.fill(fill)

    def fill_by_name(self, name, fill):
        locator = self.page.locator('name=' + name)
        locator.fill(fill)

    def fill_by_placeholder(self, name, fill):
        self.page.get_by_placeholder(name).fill(fill)

    def fill_by_locator(self, name, fill):
        self.page.locator(name).fill(fill)

    def click_by_label(self, name):
        self.page.get_by_label(name).click()

    def navigate_to_url(self, url):
        self.page.goto(url)


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
