#!/bin/bash

#requires i3lock, scrot, imagemagick


blurpic="/tmp/screen.png" # temporary location for the screenshot
lockpic="/home/frank/bin/lock/lock_ring.png" # location for the lock icon, more: https://www.iconfinder.com/search/?q=lock&license=2&price=free

scrot $blurpic
convert $blurpic -scale 10% -scale 1000% $blurpic
convert $blurpic $lockpic -gravity center -composite -matte $blurpic

## use dbus to pause spotify:
dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop

i3lock -u -d -I 10 -i $blurpic
#xset dpms force off
rm $blurpic


#dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop

