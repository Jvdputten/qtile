from libqtile.config import Group, Match, ScratchPad, DropDown


groups = [
    Group(
        "1",
        label="1",
        matches=[Match(wm_class="google-chrome")],
        layout="columns",
        screen_affinity=0,
    ),
    Group(
        "3",
        label="3",
        layout="columns",
        matches=[Match(wm_class="crx_jckaldkomadaenmmgladeopgmfbahfjm")],
        screen_affinity=0,
    ),
    Group(
        "5",
        label="5",
        layout="columns",
        screen_affinity=0,
    ),
    Group(
        "7",
        label="7",
        layout="columns",
        screen_affinity=0,
    ),
    Group(
        "9",
        label="9",
        layout="columns",
        screen_affinity=0,
    ),
    Group(
        "2",
        label="2",
        matches=[Match(wm_class="code")],
        layout="columns",
        screen_affinity=1,
    ),
    Group(
        "4",
        label="4",
        layout="columns",
        matches=[Match(wm_class="kitty")],
        screen_affinity=1,
    ),
    Group(
        "6",
        label="6",
        layout="columns",
        screen_affinity=1,
    ),
    Group(
        "8",
        label="8",
        layout="columns",
        screen_affinity=1,
    ),
]


def append_scratchpad_group():
    scratchpad = ScratchPad(
        "scratchpad",
        [
            DropDown("terminal", "kitty", opacity=0.8, height=0.5),
            DropDown("mixer", "pavucontrol", width=0.5, x=0.25),
            # DropDown("ranger", "kitty -e ranger", width=0.6, height=0.6, x=0.2, y=0.2),
        ],
    )
    groups.append(scratchpad)
