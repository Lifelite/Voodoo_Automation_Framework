from Helpers.Voodoo import *


def test_drag_and_drop(page: Page):
    validate = Validate(page)
    interact = Interact(page)
    interact.navigate_to_url("https://the-internet.herokuapp.com/drag_and_drop")

    validate.text("Drag and Drop")

    # Identify elements and assign them to variable

    source = page.locator("#column-a")
    target = page.locator("#column-b")

    # Validate element text

    validate.text_matches(source, "A")
    validate.text_matches(target, "B")

    # Drag and drop one element onto the other

    source.drag_to(target)

    # Validate elements have changed

    validate.text_matches(source, "B")
    validate.text_matches(target, "A")

    # Other method for drag and drop using positions:
    # relative position:
    # source.drag_to(
    #     target,
    #     source_position={"x": 34, "y": 7},
    #     target_position={"x": 10, "y": 20}
    # )
