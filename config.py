import os
import subprocess

from libqtile import hook, widget
from libqtile.config import Screen


from colors import onedark
from groups import groups, append_scratchpad_group  # noqa
from keys import keys, mouse, extend_scratchpad_keys  # noqa
from layouts import layouts, floating_layout  # noqa

from bar1 import get_bar


widget_defaults = dict(
    font="SauceCodePro Nerd Font Mono",
    fontsize=13,
    padding=10,
    background=onedark["bg"],
)
extension_defaults = widget_defaults.copy()
window_name = widget.WindowName()
screens = [
    Screen(top=get_bar(0)),
    Screen(top=get_bar(1)),
]


## Autostart (start only once - on boot)
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([script])


append_scratchpad_group()
extend_scratchpad_keys()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
