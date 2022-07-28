#!/bin/sh
sudo apt update
sudo apt install -y shadowsocks-libev
sudo apt-get install -y --no-install-recommends build-essential autoconf libtool libssl-dev libpcre3-dev libev-dev asciidoc xmlto automake

User=Joe


PAYLOAD_LINE=`awk '/^__PAYLOAD_BELOW__/ {print NR + 1; exit 0; }' $0`

tail -n+$PAYLOAD_LINE $0 | tar xzv -C /home/$User/ 

#git clone https://github.com/shadowsocks/simple-obfs.git
cd /home/$User/files/simple-obfs
#git submodule update --init --recursive
./autogen.sh
./configure && make
sudo make install

sudo systemctl stop shadowsocks-libev
sudo systemctl disable shadowsocks-libev

sudo ufw allow 54467
sudo /usr/bin/ss-server -c /home/$User/files/default.json -f /home/$User/files/default.pid -u 

exit 0

__PAYLOAD_BELOW__
