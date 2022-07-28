#!/bin/bash

# Enter Application Name:

# Do Copy of Application name using template

if [ $1 == '--help' ]; then
	echo "AppMenu 'Application Name' '/path/to/application/my app.sh'"
else
	#Application name
	cp /home/syeung/.local/share/applications/template.desktop.bak /home/syeung/.local/share/applications/$1.desktop
	# Exec Command (Replace line)
	sed -i "s|ItemName|$1|g" /home/syeung/.local/share/applications/$1.desktop
	sed -i "s|Command|$2|g" /home/syeung/.local/share/applications/$1.desktop
	echo "$1 Link Created"
fi




#/home/syeung/.local/share/applications
