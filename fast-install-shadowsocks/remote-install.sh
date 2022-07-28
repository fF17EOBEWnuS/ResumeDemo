#!/bin/sh

if [ "$1" -eq "" ]; then
	exit 0
fi

./compile.sh
ssh-keygen -f "~/.ssh/known_hosts" -R "$1"

scp -P 3022 files/installer.sh $1:~

ssh -p 3022 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $1

rm files/installer.sh
