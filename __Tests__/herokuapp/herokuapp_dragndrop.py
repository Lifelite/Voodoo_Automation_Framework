from Helpers.Voodoo import *


def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    Validate.text("Drag and Drop", page)

    # Identify elements and assign them to variable

    source = page.locator("#column-a")
    target = page.locator("#column-b")

    # Validate element text

    Validate.text_matches(source, "A", page)
    Validate.text_matches(target, "B", page)

    # Drag and drop one element onto the other

    source.drag_to(target)

    # Validate elements have changed

    Validate.text_matches(source, "B", page)
    Validate.text_matches(target, "A", page)

    # Other method for drag and drop using positions:
    # relative position:
    # source.drag_to(
    #     target,
    #     source_position={"x": 34, "y": 7},
    #     target_position={"x": 10, "y": 20}
    # )
