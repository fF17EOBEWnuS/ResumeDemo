#!/bin/sh
### BEGIN INIT INFO
# Provides:          Startup 
# Required-Start:   
# Required-Stop:     
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# X-Interactive:     false
# Short-Description: Escape Switch; wifi optimization off; power optimization off; qimpanel fix
### END INIT INFO



source ~/.aliases
# startup caps swap
#/usr/bin/setxkbmap -option "caps:swapescape"
#/usr/bin/setxkbmap -option "caps:escape"

#echo 'auto' > '/sys/bus/pci/devices/0000:6c:00.0/power/control';
#echo 1 | sudo tee /sys/module/snd_hda_intel/parameters/power_save > /dev/null
#echo '1500' > '/proc/sys/vm/dirty_writeback_centisecs';
#echo 'min_power' > '/sys/class/scsi_host/host0/link_power_management_policy';
#echo 'min_power' > '/sys/class/scsi_host/host1/link_power_management_policy';
#echo '0' > '/proc/sys/kernel/nmi_watchdog';
#echo 'auto' > '/sys/bus/usb/devices/1-7/power/control';
#echo 'auto' > '/sys/bus/usb/devices/1-2/power/control';
#echo 'auto' > '/sys/bus/i2c/devices/i2c-0/device/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1f.2/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1c.7/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1d.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:17.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1c.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:16.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:14.2/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:14.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:04.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:00.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1f.3/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1f.4/power/control';
#echo 'on' > '/sys/bus/pci/devices/0000:6c:00.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:6d:00.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:1f.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:6c:00.0/power/control';
#echo 'auto' > '/sys/bus/pci/devices/0000:00:16.3/power/control';

#kill -9 `ps -ef | grep qimpanel | grep -v grep | awk '{ print $2 }'` > /dev/null 2>&1

# Disable Middle Mouse button
#xinput set-button-map 12 1 0 3 5 4 6 7 8 9 10 11 12
#xinput set-button-map 11 1 0 3 5 4 6 7 8 9 10 11 12
#xinput set-button-map 13 1 0 3 4 5 6 7

#sudo iwconfig wlp108s0 power on
#sudo iwconfig wlp108s0 power off > /dev/null 2>&1
#sudo mount /dev/sda8 /data

#power wireless shortrange
#sudo iwconfig wlp108s0 txpower '0'

#echo min_power > /sys/class/scsi_host/host0/link_power_management_policy
#echo min_power > /sys/class/scsi_host/host1/link_power_management_policy

#xrandr --output eDP-1 --brightness 1;xbacklight -set 21
#sudo tlp start
#~/Programming/development/Utility/dns-fix/copy-script.sh
#pactl load-module module-bluetooth-discover
#sudo powertop --auto-tune --quiet
#echo 'auto' > '/sys/bus/usb/devices/1-13/power/control';



#sudo iwconfig wlp108s0 txpower '6'

# Fix annoying mousepad clicks
#synclient RTCornerButton=0
#synclient RBCornerButton=0
#synclient LTCornerButton=0
#synclient LBCornerButton=0
#synclient VertEdgeScroll=0

# Anbox Export startup
#export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
#LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libgtk3-nocsd.so.0
#
#sudo xinput set-prop "12" "Synaptics Palm Dimensions" 3, 3

# Disable symbols on startup for secondary Keyboard 
if [ $(ps -ef | grep set.py | grep -v grep | wc -l) -eq 0 ]; then
	sudo /usr/bin/python3 ~/Programming/development/secondkbd/shortcut-scripts/python-solution/set.py &
else
	findkill 'set.py'
	sudo /usr/bin/python3 ~/Programming/development/secondkbd/shortcut-scripts/python-solution/set.py &
fi

~/.scripts/barrier.sh


## Python Keyboard Extra Script 
xset r rate 450 50

sudo nvidia-smi -pm ENABLED
sudo nvidia-smi -pl 150 -i 0



#export DISPLAY=:0 

#sudo nvidia-settings -a [gpu:0]/GPUFanControlState=1 -a [fan:0]/GPUTargetFanSpeed=50
#sudo nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'

export QT_QPA_PLATFORMTHEME=qt5ct
# Fix Monitor positioning
xrandr --output DP-4 --mode 2560x1440 --rotate left --left-of HDMI-0

nohup picom >/dev/null 2>&1 &

# Terminal Position move
wmctrl -i -r  $(wmctrl -l | grep Terminal | awk -e '{print $1}') -e 0,1440,1092,1920,1068
# Skype

wmctrl -i -r  $(wmctrl -l | grep -i skype | awk -e '{print $1}') -e 0,0,0,1440,853

pulseeffects



path=$path:~/.scripts
export $path

# Startin up Chrome

nohup chromium-browser %U --proxy-server="socks5://localhost:1080" --proxy-bypass-list=192.168.1.2 --host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE localhost, EXCLUDE 192.168.1.2" >/dev/null 2>&1 &

sleep 5

~/.scripts/chromium-startup-fixer

# xdotool set_desktop 2 
# nohup /usr/bin/proxychains /usr/share/discord/Discord >/dev/null 2>&1 &
# 
# sleep 2 
# 
# xdotool set_desktop 8 
# nohup /usr/bin/proxychains /usr/bin/slack &U >/dev/null 2>&1 &
# 
# sleep 1 
# 
# sudo /usr/bin/ratbagctl Logi dpi set 12000

xdotool set_desktop 0

exit 0
