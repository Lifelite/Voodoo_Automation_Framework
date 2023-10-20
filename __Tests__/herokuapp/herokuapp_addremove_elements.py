from Helpers.Voodoo import *


def test_element_addremove(page: Page):
    validate = Validate(page)
    interact = Interact(page)
    interact.navigate_to_url("https://the-internet.herokuapp.com/add_remove_elements/")

    # Quick Page Validation
    validate.text("Add/Remove Elements")
    validate.button_enabled("Add Element")

    # Validate Elements can be added
    delete_button = validate.page.get_by_role("button", name="Delete")
    for i in range(10):
        assert delete_button.count() == i
        interact.click_button("Add Element")

    # Validate Elements can be removed

    delete_count = delete_button.count()
    assert delete_count == 10

    for i in range(10, 0, -1):
        delete_button.nth(0).click()
        new_delete_count = delete_button.count()
        assert i - 1 == new_delete_count

    expect(delete_button).not_to_be_visible()
