#!/usr/bin/env python
"""
An interactive browser for resource data.
"""

from prompt_toolkit.application import Application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent

from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.key_binding.bindings.page_navigation import load_vi_page_navigation_bindings

from prompt_toolkit.layout import (
    HSplit,
    Layout,
    VSplit, Window, FormattedTextControl, WindowAlign, Dimension,
)
from prompt_toolkit.widgets import Frame, TextArea
from pacu.data import ResourceTable


def get_titlebar_text():
    return [
        ("class:title", " Resource Explorer "),
        ("class:title", " (Press [Ctrl-C] to quit.)"),
    ]


def browse():
    db = ResourceTable()
    resources = [r.doc_id for r in db.all()]

    detail_display = Frame(
        TextArea(text='<resource browser>'),
        width=Dimension(weight=4),
    )

    kb = KeyBindings()
    @kb.add('enter')
    def accept(event: 'KeyPressEvent') -> bool:
        resource = db.get(doc_id=event.current_buffer.document.current_line.strip())
        # print(resource)
        detail_display.body = TextArea(text=resource.to_json(indent=True))

    resource_display = Frame(
        TextArea(
            text='\n'.join(resources),
            read_only=True,
            multiline=True,
            scrollbar=True,
        ),
        width=Dimension(weight=3),
        key_bindings=kb,
    )

    main_container = VSplit(
        [
            resource_display,
            detail_display,
        ]
    )

    root_container = HSplit(
        [
            Window(
                height=1,
                content=FormattedTextControl(get_titlebar_text),
                align=WindowAlign.CENTER,
            ),
            # Horizontal separator.
            Window(height=1, char="-", style="class:line"),
            # The 'body', like defined above.
            main_container,
        ]
    )

    layout = Layout(container=root_container)

    kb = KeyBindings()
    kb.add("tab")(focus_next)
    kb.add("s-tab")(focus_previous)

    @kb.add("c-c")
    def exit(event) -> None:
        event.app.exit()

    load_vi_page_navigation_bindings()

    # Create and run app.
    app = Application(layout=layout, key_bindings=kb, full_screen=True, mouse_support=True)
    app.run()


if __name__ == "__main__":
    browse()
