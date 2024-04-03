import os
import subprocess


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.grous_map[name].toscreen()
            return

        if name in "13579":
            qtile.focus_screen(0)
        else:
            qtile.focus_screen(1)

        qtile.groups_map[name].toscreen()

    return _inner


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        qtile.current_window.togroup(name, switch_group=False)
        qtile.focus_screen(0) if name in "13579" else qtile.focus_screen(1)
        qtile.groups_map[name].toscreen()

    return _inner


def run_rofi(qtile):
    script_path = os.path.expanduser("~/.config/rofi/launchers/type-1/launcher.sh")
    subprocess.call([script_path])


def run_powermenu(qtile):
    script_path = os.path.expanduser("~/.config/rofi/powermenu/type-1/powermenu.sh")
    subprocess.call([script_path])


def run_chatgpt(qtile):
    subprocess.Popen(["gtk-launch", "chatgpt.desktop"])
    qtile.focus_screen(0)
    qtile.groups_map["3"].toscreen()


def run_chrome(qtile):
    subprocess.Popen(["google-chrome"])
    qtile.focus_screen(0)
    qtile.groups_map["1"].toscreen()


def run_code(qtile):
    subprocess.Popen(["code"])
    qtile.focus_screen(1)
    qtile.groups_map["2"].toscreen()


def run_kitty(qtile):
    subprocess.Popen(["kitty"])
    qtile.focus_screen(1)
    qtile.groups_map["4"].toscreen()
