from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag
from functions import (
    run_chatgpt,
    run_kitty,
    run_code,
    run_chrome,
    run_rofi,
    run_powermenu,
    go_to_group,
    go_to_group_and_move_window,
)
from groups import groups

terminal = "kitty"
mod = "mod4"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Launch browser
    Key([mod], "g", lazy.function(run_chrome), desc="Launch browser"),
    Key([mod], "c", lazy.function(run_code), desc="Launch code"),
    Key([mod], "a", lazy.function(run_chatgpt), desc="Launch chatgpt"),
    Key([mod], "Return", lazy.function(run_kitty), desc="Launch terminal"),
    Key(
        [mod],
        "p",
        lazy.function(run_rofi),
        desc="Run rofi",
    ),
    Key(
        [mod],
        "x",
        lazy.function(run_powermenu),
        desc="Run powermenu",
    ),
    # Scratchpads
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.function(go_to_group(i.name))),
            Key(
                [mod] + ["shift"],
                i.name,
                lazy.function(go_to_group_and_move_window(i.name)),
            ),
        ]
    )


def extend_scratchpad_keys():
    keys.extend(
        [
            Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("terminal")),
            Key([mod], "r", lazy.group["scratchpad"].dropdown_toggle("ranger")),
            Key([mod], "m", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        ]
    )


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
