#!/usr/bin/python3
# Documentation for pyautogui:
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# Icons https://icons8.com/icons/

import os, subprocess
from pyautogui import press, typewrite, hotkey
from evdev import InputDevice, categorize, ecodes
import time as td
# Use evtest to determine which keyboard by testing
# you want "Hoksi Technology KB105"
# commandl = "grep -A 10 '\"Hoksi Technology KB105\"' /proc/bus/input/devices
# | grep devices | awk '{print substr($0,length,1)}'"
commandl = "~/Programming/development/secondkbd/shortcut-scripts/python-solution/helper.sh"
output = subprocess.getoutput(commandl)
inputpath = '/dev/input/event%s' % output
print(inputpath)
dev = InputDevice("%s" % inputpath)
dev.grab()

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_RESERVED':        #0
                print(event)
            elif key.keycode == 'KEY_ESC':    #1
                press('G')
                press('I')
            elif key.keycode == 'KEY_1':      #2
                commandl="sudo -u syeung thunar /media/syeung/Data/"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_2':      #3
                commandl="sudo -u syeung thunar /media/syeung/Data/syeung"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_3':      #4
                commandl="sudo -u syeung thunar ~"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_4':      #5
                commandl="sudo -u syeung firefox &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_5':      #6
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' /usr/bin/chromium-browser --profile-directory=Default --app-id=hmjkmjkepdijhoojdojkdfohbdgmmhki &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_6':      #7
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.twitch.tv &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_7':      #8
                commandl = "sudo -u syeung inkscape &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_8':      #9
                commandl = "sudo -u syeung audacity &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_9':      #10
                commandl = "env BAMF_DESKTOP_FILE_HINT=/var/lib/snapd/desktop/applications/obs-studio_obs-studio.desktop /snap/bin/obs-studio &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_0':      #11
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://mail.google.com/mail/u/0/#search/label%3Ainbox+label%3Aunread &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_MINUS':        #12
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://drive.google.com/drive/ &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_EQUAL':        #13
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://sysshep.harvestapp.com    ime &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_BACKSPACE':  #14
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://alarm.sscc01.systemshepherd.com/escalations &"
                subprocess.call(commandl,shell=True)
            ###########
            ## ROW 2 ##
            ###########
            elif key.keycode == 'KEY_TAB':    #15
                press('E')
            elif key.keycode == 'KEY_Q':      #16
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://mail.google.com/mail/u/0/#search/label%3Ainbox+label%3Aunread &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_W':      #17
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://mail.google.com/mail/u/0/#search/label%3Ainbox+label%3Aunread &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_E':      #18
                print(event)
            elif key.keycode == 'KEY_R':      #19
                commandl="filezilla &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_T':      #20
                commandl = "sudo -u syeung ~/.scripts/sndkbd.sh"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_Y':      #21
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.reddit.com &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_U':      #22
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.youtube.com/channel/UCcnyjTK4IheQN2ycsE7NZTQ &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_I':      #23
                commandl="~/Programming/development/Stocks/Stockscreens-setup/refined-44"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_O':      #24
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.reddit.com/r/options    op/ &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_P':      #25
                commandl = "sudo -u syeung remmina &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_LEFTBRACE':  #26
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://absperf.atlassian.net/wiki/spacedirectory/view.action &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHTBRACE':   #27
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://absperf.atlassian.net/issues/?filter=-1 &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_ENTER':        #28
                commandl = "sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Profile 1' https://alarm.sscc02.systemshepherd.com/escalations &"
                subprocess.call(commandl,shell=True)
                ###########
                ## ROW 3 ##
                ######################
            elif key.keycode == 'KEY_LEFTCTRL':   #29
                press('F')
            elif key.keycode == 'KEY_A':      #30
                commandl="export XDG_RUNTIME_DIR='/run/user/1000';sudo -u syeung /usr/bin/virtualbox &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_S':      #31
                hotkey('winleft','c')
            elif key.keycode == 'KEY_D':      #32
                hotkey('ctrl','alt','delete')
            elif key.keycode == 'KEY_F':      #33
                commandl="export XDG_RUNTIME_DIR='/run/user/1000';/opt/sublime_text_3/sublime_text &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_G':      #34
                commandl = "sudo -u syeung ~/.scripts/barrier.sh"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_H':      #35
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.reddit.com/r/wallstreetbets/ &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_J':      #36
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.reddit.com/r/investing    op/ &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_K':      #37
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts    imer 5m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_L':      #38
                print(event)
            elif key.keycode == 'KEY_SEMICOLON':  #39
                commandl="sudo -u syeung xflock4"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_APOSTROPHE':   #40
                hotkey('winleft','space')
            elif key.keycode == 'KEY_GRAVE':        #41
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3000,24,960,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_LEFTSHIFT':  #42
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3960,24,960,1068'
                subprocess.call(commandl,shell=True)
            ###########
            ## ROW 4 ##
            ###########
            elif key.keycode == 'KEY_BACKSLASH':  #43
                press('#')
            elif key.keycode == 'KEY_Z':      #44
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://web.wechat.com &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_X':      #45
                commandl="sudo -u syeung /usr/bin/calibre &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_C':      #46
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.google.com &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_V':      #47
                commandl="sudo -u syeung /usr/bin/libreoffice --writer &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_B':      #48
                commandl="sudo -u syeung /usr/bin/libreoffice --calc &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_N':      #49
                hotkey('winleft','z')
                sleep(0.05)
                hotkey('winleft','left')
                hotkey('ctrl','a')
                press('-')
                td.sleep(0.05)
                hotkey('ctrl','a')
                press('|')
                td.sleep(0.05)
                hotkey('ctrl','a')
                press('up')
                td.sleep(0.5)
                hotkey('ctrl','a')
                td.sleep(0.1)
                press('|')
            elif key.keycode == 'KEY_M':      #50
                hotkey('winleft','z')
                td.sleep(0.05)
                hotkey('winleft','right')
                hotkey('ctrl','a')
                press('-')
                td.sleep(0.05)
                hotkey('ctrl','a')
                press('|')
                td.sleep(0.05)
                hotkey('ctrl','a')
                press('up')
                td.sleep(0.5)
                hotkey('ctrl','a')
                td.sleep(0.1)
                press('|')
            elif key.keycode == 'KEY_COMMA':        #51
                hotkey('ctrl','a')
                press('-')
            elif key.keycode == 'KEY_DOT':    #52
                hotkey('ctrl','a')
                press('|')
            elif key.keycode == 'KEY_SLASH':        #53
                hotkey('ctrl','a')
                press(' ')
            elif key.keycode == 'KEY_RIGHTSHIFT':   #54
                hotkey('ctrl','a')
                press('x')
                td.sleep(0.2)
                press('y')
            elif key.keycode == 'KEY_KPASTERISK':   #55
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3000,1092,960,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_SYSRQ':        #99
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3960,1092,960,1068'
                subprocess.call(commandl,shell=True)
            ###########
            ## ROW 5 ##
            ###########
            elif key.keycode == 'KEY_F1':      #59
                press('Z')
            elif key.keycode == 'KEY_F2':      #60
                commandl="sudo -u syeung /usr/bin/discord >/dev/null &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F3':      #61
                hotkey('winleft','m')
            elif key.keycode == 'KEY_F4':      #62
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.youtube.com &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F5':      #63
                commandl="matlab"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F6':      #64
                #commandl="sudo wireshark &"
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 10m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F7':      #65
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 15m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F8':      #66
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 20m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F9':      #67
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 30m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F10':    #68
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 50m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F11':    #87
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/timer 25m &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_F12':    #88
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/alarm 480 &" # 8*60 (8:00)
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHTCTRL':  #97
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/alarm 1350 &" # 22*60+30 (22:30)
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KPSLASH':      #98
                commandl="sudo -u syeung ~/Programming/development/secondkbd/shortcut-scripts/hrly-chime/chime swap"
                subprocess.call(commandl,shell=True)
            ###########
            ## ROW 6 ##
            ###########
            elif key.keycode == 'KEY_KP1':    #79
                # press('R') Originally reply to email (Gmail)
                commandl="~/Programming/development/full-screen_osd/countdown"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP2':    #80
                commandl="~/Programming/development/full-screen_osd/long-countdown/25min"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP3':    #81
                commandl="~/Programming/development/secondkbd/shortcut-scripts/shutdown &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP7':    #71
                commandl="sudo -u syeung /usr/bin/proxychains chromium-browser --profile-directory='Default' https://www.coursera.org &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP8':    #72
                hotkey('ctrl','alt','left')
            elif key.keycode == 'KEY_KP9':    #73
                hotkey('ctrl','alt','right')
            elif key.keycode == 'KEY_KPMINUS':      #74
                commandl = "wmctrl -r :ACTIVE: -t 0"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP4':    #75
                commandl = "wmctrl -r :ACTIVE: -t 1"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP5':    #76
                commandl = "wmctrl -r :ACTIVE: -t 2"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP6':    #77
                commandl = "wmctrl -r :ACTIVE: -t 3"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KPPLUS':        #78
                commandl = "wmctrl -r :ACTIVE: -t 4"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KP0':    #82
                commandl = "wmctrl -r :ACTIVE: -t 5"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_KPDOT':        #83
                commandl = "wmctrl -r :ACTIVE: -t 6"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_COMPOSE':      #127
                commandl = "wmctrl -r :ACTIVE: -t 7"
                subprocess.call(commandl,shell=True)
            #################
            ## Rightside 4 ##
            #################
            elif key.keycode == 'KEY_LEFTMETA':   #125
                commandl="sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts/bloomberg-xdo' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_INSERT':        #110
                commandl = 'sudo -u syeung /usr/bin/ssh 10.223.192.150 "/opt/remote-scripts/vol-mute" &'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_HOME':  #102
                commandl = 'sudo -u syeung /usr/bin/ssh 10.223.192.150 "/opt/remote-scripts/vol-low" &'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_PAGEUP':        #104
                commandl = "sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts/vol-full' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHTMETA':  #126
                commandl="sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts    asty-xdo' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_DELETE':        #111
                commandl="sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts/reuter-xdo' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_END':    #107
                commandl ="sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts/cnn-xdo' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_PAGEDOWN':   #109
                commandl ="sudo -u syeung /usr/bin/ssh 10.223.192.150 '/opt/remote-scripts/close-ff' &"
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_LEFTALT':      #56
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,1080,24,1920,2136'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_SPACE':        #57
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3000,24,1920,2136'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHTALT':   #100
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,0,0,1080,1920'
                subprocess.call(commandl,shell=True)
            ############
            ## Arrows ##
            ############
            elif key.keycode == 'KEY_SCROLLLOCK':   #   70
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,1080,24,1920,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_UP':      #103
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3000,24,1920,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_PAUSE':  #   119
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,0,0,1080,960'
                subprocess.call(commandl,shell=True)
                td.sleep(0.05)
                hotkey('winleft','pageup')
            elif key.keycode == 'KEY_LEFT':  #105
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,1080,1092,1920,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHT':        #106
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,0,0,1080,960'
                subprocess.call(commandl,shell=True)
                td.sleep(0.05)
                hotkey('winleft','pagedown')
            elif key.keycode == 'KEY_DOWN':  #108
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,3000,1092,1920,1068'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_RIGHT':        #106
                commandl = 'wmctrl -r ":ACTIVE:" -e 0,0,960,1080,960'
                subprocess.call(commandl,shell=True)
            ############
            # Volumes  #
            ############
            elif key.keycode == 'KEY_VOLUMEDOWN':   #106
                commandl = 'pactl -- set-sink-volume 0 -10%'
                subprocess.call(commandl,shell=True)
            elif key.keycode == 'KEY_VOLUMEUP':     #106
                commandl = 'pactl -- set-sink-volume 0 +10%'
                subprocess.call(commandl,shell=True)
            else:
                print(event)


