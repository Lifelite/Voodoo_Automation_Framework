from Helpers.Voodoo import *


def test_element_addremove(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Quick Page Validation
    Validate.text("Add/Remove Elements", page)
    Validate.button_enabled("Add Element", page)

    # Validate Elements can be added
    delete_button = page.get_by_role("button", name="Delete")
    i = 0
    while i < 10:
        assert delete_button.count() == i
        Interact.click_button("Add Element", page)
        i = i + 1

    # Validate Elements can be removed

    delete_count = delete_button.count()
    assert delete_count == 10

    while i > 0:
        delete_button.nth(0).click()
        i = i - 1
        new_delete_count = delete_button.count()
        assert i == new_delete_count

    expect(delete_button).not_to_be_visible()
