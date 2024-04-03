from colors import onedark
from libqtile import layout
from libqtile.config import Match

BORDER_WIDTH = 3
BORDER_COLOR = onedark["green"]

layouts = [
    layout.Columns(
        border_normal=onedark["black"],
        border_focus=BORDER_COLOR,
        border_width=BORDER_WIDTH,
        border_normal_stack=onedark["black"],
        border_focus_stack=BORDER_COLOR,
        border_on_single=1,
        margin=0,
        margin_on_single=0,
    ),
    layout.Max(
        border_normal=onedark["black"],
        border_focus=BORDER_COLOR,
        border_width=BORDER_WIDTH,
        num_stacks=2,
        margin=0,
    ),
]

floating_layout = layout.Floating(
    border_normal=onedark["bg"],
    border_focus=BORDER_COLOR,
    border_width=BORDER_WIDTH,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
    ],
)
