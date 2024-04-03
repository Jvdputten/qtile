#!/bin/sh
xrandr --output DP-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-2 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-3 --off --output DP-4 --off

# Set wallpaper
qtile_dir="$HOME/.config/qtile"
feh --bg-fill "$qtile_dir/fuji_wallpaper.jpg"
