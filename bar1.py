from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from unicodes import left_half_circle, right_arrow, right_half_circle
from colors import onedark

BAR_HEIGHT = 28

left_group_names = ["1", "3", "5", "7", "9"]
right_group_names = ["2", "4", "6", "8", "0"]


def get_bar(screen: int):
    if screen == 0:
        visible_groups = left_group_names
    else:
        visible_groups = right_group_names

    return Bar(
        [
            GroupBox(
                visible_groups=visible_groups,
                disable_drag=True,
                active=onedark["fg"],
                inactive=onedark["bg_highlight"],
                highlight_method="border",
                block_highlight_text_color=onedark["blue"],
                borderwidth=2,
                background=onedark["bg"],
                spacing=2,
            ),
            left_half_circle(onedark["red"], onedark["bg"]),
            CurrentLayout(
                background=onedark["red"],
                foreground=onedark["black"],
                margin=10,
            ),
            right_arrow(onedark["fg_gutter"], onedark["red"]),
            WindowCount(
                text_format="\uf2d2 {num}",
                background=onedark["fg_gutter"],
                foreground=onedark["black"],
                show_zero=True,
            ),
            right_half_circle(onedark["fg_gutter"], onedark["bg"]),
            WindowName(background=onedark["bg"], foreground=onedark["fg"]),
            left_half_circle(onedark["black"], onedark["bg"]),
            CPU(
                format=" {freq_current}GHz {load_percent}%",
                background=onedark["black"],
                foreground=onedark["pink"],
            ),
            Memory(
                format=" {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
                background=onedark["black"],
                foreground=onedark["cyan"],
            ),
            Net(background=onedark["black"], foreground=onedark["green"]),
            Clock(
                background=onedark["black"],
                foreground=onedark["white"],
                format="\uf43a %Y-%m-%d %a %I:%M %p",
            ),
        ],
        background=onedark["bg"],
        size=BAR_HEIGHT,
        margin=0,
    )
