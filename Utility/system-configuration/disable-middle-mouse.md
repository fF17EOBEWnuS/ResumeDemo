### Disabling Middle Mouse button on XFCE Systems ### 

*https://wiki.ubuntu.com/X/Config/Input#Example%3a_Disabling_middle-mouse_button_paste_on_a_scrollwheel_mouse*

Scrollwheel mice support a middle-button click event when pressing the scrollwheel. This is a great feature, but you may find it irritating. Fortunately it can be disabled.

First, you need to know the id of the mouse, like this:


$ xinput list | grep 'id='

"Virtual core pointer"  id=0    [XPointer]
"Virtual core keyboard" id=1    [XKeyboard]
"AT Translated Set 2 keyboard"  id=2    [XExtensionKeyboard]
"Macintosh mouse button emulation"      id=3    [XExtensionPointer]
"Logitech USB-PS/2 Optical Mouse"       id=4    [XExtensionPointer]
My mouse has the Logitech logo printed on it, so I gather I need the last entry.

I can view the current button mapping thusly:


$ xinput get-button-map 4

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 10
Really, only the first three numbers have meaning for me. They represent the left, middle, and right mouse buttons.


$ xinput get-button-map 4
I can turn the middle mouse button off by setting it to 0:


$ xinput set-button-map 4 1 0 3
Or I can turn the middle-mouse button into a left-mouse button by setting it to 1:


$ xinput set-button-map 4 1 1 3
To make this set on a per-user basis, I can plug that line into my ~/.xstartup or other init file. It can also be done via configuring a matching InputClass section on xorg.conf.




