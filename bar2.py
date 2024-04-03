from libqtile import widget, qtile
from libqtile.bar import Bar

BAR_HEIGHT = 28


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/qtile/power")


# BAR_MARGIN = 5
bar = Bar(
    [
        widget.Spacer(
            length=15,
            background="#232A2E",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/launch_Icon.png",
            margin=2,
            background="#232A2E",
            mouse_callbacks={"Button1": power},
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/6.png",
        ),
        widget.GroupBox(
            fontsize=24,
            borderwidth=3,
            highlight_method="block",
            active="#86918A",
            block_highlight_text_color="#D3C6AA",
            highlight_color="#4B427E",
            inactive="#232A2E",
            foreground="#4B427E",
            background="#343F44",
            this_current_screen_border="#343F44",
            this_screen_border="#343F44",
            other_current_screen_border="#343F44",
            other_screen_border="#343F44",
            urgent_border="#343F44",
            rounded=True,
            disable_drag=True,
        ),
        widget.Spacer(
            length=8,
            background="#343F44",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/1.png",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/layout.png", background="#343F44"
        ),
        widget.CurrentLayout(
            background="#343F44",
            foreground="#86918A",
            fmt="{}",
            font="JetBrains Mono Bold",
            fontsize=13,
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/5.png",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/search.png",
            margin=2,
            background="#232A2E",
            mouse_callbacks={"Button1": search},
        ),
        widget.TextBox(
            fmt="Search",
            background="#232A2E",
            font="JetBrains Mono Bold",
            fontsize=13,
            foreground="#86918A",
            mouse_callbacks={"Button1": search},
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/4.png",
        ),
        widget.WindowName(
            background="#343F44",
            format="{name}",
            font="JetBrains Mono Bold",
            fontsize=13,
            foreground="#86918A",
            empty_group_string="Desktop",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/3.png",
        ),
        widget.Systray(
            background="#232A2E",
            fontsize=2,
        ),
        widget.TextBox(
            text=" ",
            background="#232A2E",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/6.png",
            background="#343F44",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/ram.png",
            background="#343F44",
        ),
        widget.Spacer(
            length=-7,
            background="#343F44",
        ),
        widget.Memory(
            background="#343F44",
            format="{MemUsed: .0f}{mm}",
            foreground="#86918A",
            font="JetBrains Mono Bold",
            fontsize=13,
            update_interval=5,
        ),
        widget.Volume(
            font="JetBrains Mono Bold",
            fontsize=13,
            theme_path="~/.config/qtile/Assets/Volume/",
            emoji=True,
            background="#343F44",
        ),
        widget.Spacer(
            length=-5,
            background="#343F44",
        ),
        widget.Volume(
            font="JetBrains Mono Bold",
            fontsize=13,
            background="#343F44",
            foreground="#86918A",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/5.png",
            background="#343F44",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/clock.png",
            background="#232A2E",
            margin_y=6,
            margin_x=5,
        ),
        widget.Clock(
            format="%I:%M %p",
            background="#232A2E",
            foreground="#86918A",
            font="JetBrains Mono Bold",
            fontsize=13,
        ),
        widget.Spacer(
            length=18,
            background="#232A2E",
        ),
    ],
    size=BAR_HEIGHT,
    margin=8,
)
