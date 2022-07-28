import os, subprocess
from pyautogui import press, typewrite, hotkey
from evdev import InputDevice, categorize, ecodes
import time as td

# Substitute Holder
dev = InputDevice('/dev/input/event7')
dev.grab()

for event in dev.read_loop():
    keymap = {
    'KEY_RESERVED':print(event),    #0 \
    'KEY_ESC':print(event),    #1 \
    'KEY_1':print(event),    #2 \
    'KEY_2':print(event),    #3 \
    'KEY_3':print(event),    #4 \
    'KEY_4':print(event),    #5 \
    'KEY_5':print(event),    #6 \
    'KEY_6':print(event),    #7 \
    'KEY_7':print(event),    #8 \
    'KEY_8':print(event),    #9 \
    'KEY_9':print(event),    #10 \
    'KEY_0':print(event),    #11 \
    'KEY_MINUS':print(event),    #12 \
    'KEY_EQUAL':print(event),    #13 \
    'KEY_BACKSPACE':print(event),    #14 \
    'KEY_TAB':print(event),    #15 \
    'KEY_Q':print(event),    #16 \
    'KEY_W':print(event),    #17 \
    'KEY_E':print(event),    #18 \
    'KEY_R':print(event),    #19 \
    'KEY_T':print(event),    #20 \
    'KEY_Y':print(event),    #21 \
    'KEY_U':print(event),    #22 \
    'KEY_I':print(event),    #23 \
    'KEY_O':print(event),    #24 \
    'KEY_P':print(event),    #25 \
    'KEY_LEFTBRACE':print(event),    #26 \
    'KEY_RIGHTBRACE':print(event),    #27 \
    'KEY_ENTER':print(event),    #28 \
    'KEY_LEFTCTRL':print(event),    #29 \
    'KEY_A':print(event),    #30 \
    'KEY_S':print(event),    #31 \
    'KEY_D':print(event),    #32 \
    'KEY_F':print(event),    #33 \
    'KEY_G':print(event),    #34 \
    'KEY_H':print(event),    #35 \
    'KEY_J':print(event),    #36 \
    'KEY_K':print(event),    #37 \
    'KEY_L':print(event),    #38 \
    'KEY_SEMICOLON':print(event),    #39 \
    'KEY_APOSTROPHE':print(event),    #40 \
    'KEY_GRAVE':print(event),    #41 \
    'KEY_LEFTSHIFT':print(event),    #42 \
    'KEY_BACKSLASH':print(event),    #43 \
    'KEY_Z':print(event),    #44 \
    'KEY_X':print(event),    #45 \
    'KEY_C':print(event),    #46 \
    'KEY_V':print(event),    #47 \
    'KEY_B':print(event),    #48 \
    'KEY_N':print(event),    #49 \
    'KEY_M':"""hotkey('ctrl','a')
    press('-')""",    #50 \
    'KEY_COMMA':    """hotkey('ctrl','a')
    press('|')""",    #51 \
    'KEY_DOT':print(event),    #52 \
    'KEY_SLASH':print(event),    #53 \
    'KEY_RIGHTSHIFT':print(event),    #54 \
    'KEY_KPASTERISK':print(event),    #55 \
    'KEY_LEFTALT':print(event),    #56 \
    'KEY_SPACE':print(event),    #57 \
    'KEY_CAPSLOCK':print(event),    #58 \
    'KEY_F1':print(event),    #59 \
    'KEY_F2':print(event),    #60 \
    'KEY_F3':print(event),    #61 \
    'KEY_F4':print(event),    #62 \
    'KEY_F5':print(event),    #63 \
    'KEY_F6':print(event),    #64 \
    'KEY_F7':print(event),    #65 \
    'KEY_F8':print(event),    #66 \
    'KEY_F9':print(event),    #67 \
    'KEY_F10':print(event),    #68 \
    'KEY_NUMLOCK':print(event),    #69 \
    'KEY_SCROLLLOCK':print(event),    #70 \
    'KEY_KP7':print(event),    #71 \
    'KEY_KP8':print(event),    #72 \
    'KEY_KP9':print(event),    #73 \
    'KEY_KPMINUS':print(event),    #74 \
    'KEY_KP4':print(event),    #75 \
    'KEY_KP5':print(event),    #76 \
    'KEY_KP6':print(event),    #77 \
    'KEY_KPPLUS':print(event),    #78 \
    'KEY_KP1':print(event),    #79 \
    'KEY_KP2':print(event),    #80 \
    'KEY_KP3':print(event),    #81 \
    'KEY_KP0':print(event),    #82 \
    'KEY_KPDOT':print(event),    #83 \
    'KEY_ZENKAKUHANKAKU':print(event),    #85 \
    'KEY_102ND':print(event),    #86 \
    'KEY_F11':print(event),    #87 \
    'KEY_F12':print(event),    #88 \
    'KEY_RO':print(event),    #89 \
    'KEY_KATAKANA':print(event),    #90 \
    'KEY_HIRAGANA':print(event),    #91 \
    'KEY_HENKAN':print(event),    #92 \
    'KEY_KATAKANAHIRAGANA':print(event),    #93 \
    'KEY_MUHENKAN':print(event),    #94 \
    'KEY_KPJPCOMMA':print(event),    #95 \
    'KEY_KPENTER':print(event),    #96 \
    'KEY_RIGHTCTRL':print(event),    #97 \
    'KEY_KPSLASH':print(event),    #98 \
    'KEY_SYSRQ':print(event),    #99 \
    'KEY_RIGHTALT':print(event),    #100 \
    'KEY_LINEFEED':print(event),    #101 \
    'KEY_HOME':print(event),    #102 \
    'KEY_UP':print(event),    #103 \
    'KEY_PAGEUP':print(event),    #104 \
    'KEY_LEFT':print(event),    #105 \
    'KEY_RIGHT':print(event),    #106 \
    'KEY_END':print(event),    #107 \
    'KEY_DOWN':print(event),    #108 \
    'KEY_PAGEDOWN':print(event),    #109 \
    'KEY_INSERT':print(event),    #110 \
    'KEY_DELETE':print(event),    #111 \
    'KEY_MACRO':print(event),    #112 \
    'KEY_MUTE':print(event),    #113 \
    'KEY_VOLUMEDOWN':print(event),    #114 \
    'KEY_VOLUMEUP':print(event),    #115 \
    'KEY_POWER':print(event),    #116  \
    'KEY_KPEQUAL':print(event),    #117 \
    'KEY_KPPLUSMINUS':print(event),    #118 \
    'KEY_PAUSE':print(event),    #119 \
    'KEY_SCALE':print(event),    #120     \
    'KEY_KPCOMMA':print(event),    #121 \
    'KEY_HANGEUL':print(event),    #122 \
    'KEY_HANGUEL':print(event),    #KEY_HANGEUL \
    'KEY_HANJA':print(event),    #123 \
    'KEY_YEN':print(event),    #124 \
    'KEY_LEFTMETA':print(event),    #125 \
    'KEY_RIGHTMETA':print(event),    #126 
    }
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode in keymap:
                keymap[(key.keycode)]
                td.sleep(1)

