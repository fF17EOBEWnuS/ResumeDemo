#!/bin/sh
# Vpn service on function



connect(){
	sudo sed -i ' 32 s|[#]||g' /var/spool/cron/crontabs/$User
	/usr/bin/notify-send -t 3500 'VPN Autoconnect Enabled'
	/usr/bin/notify-send -t 3000 'Connecting to VPN'
	expressvpn connect
	/usr/bin/notify-send -t 3000 'Successfully connected to VPN'
}

disconnect(){
	sudo sed -i '32 s/^/#/' /var/spool/cron/crontabs/$User 
	expressvpn disconnect;
	/usr/bin/notify-send -t 3500 'VPN Autoconnect Disabled and Disconnected'
}



echo $1


if  [ "$1" -eq "0" ]; then
	disconnect
elif [ "$1" -eq "1" ]; then
	connect
else
	echo "Please Enter a proper command!"
fi
