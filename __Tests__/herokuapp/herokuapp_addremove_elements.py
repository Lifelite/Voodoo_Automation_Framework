from Helpers.Voodoo import *


def test_element_addremove(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Quick Page Validation
    Validate.text("Add/Remove Elements", page)
    Validate.button_enabled("Add Element", page)

    # Validate Elements can be added
    delete_button = page.get_by_role("button", name="Delete")
    for i in range(10):
        assert delete_button.count() == i
        Interact.click_button("Add Element", page)

    # Validate Elements can be removed

    delete_count = delete_button.count()
    assert delete_count == 10

    for i in range(10, 0, -1):
        delete_button.nth(0).click()
        new_delete_count = delete_button.count()
        assert i - 1 == new_delete_count

    expect(delete_button).not_to_be_visible()
