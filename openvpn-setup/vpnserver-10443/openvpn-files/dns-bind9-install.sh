#!/bin/bash
## Internal DNS Setup for openvpn Server 

sudo apt-get --yes --force-yes update
sudo apt-get install  --yes --force-yes bind9 bind9utils bind9-doc

## configure bind9 startup
sed -i "6 s/bind/bind -4/" /etc/default/bind9
sudo systemctl restart bind9

ins1="\ \ \ \ \ \ \ \ allow-query { any; };"
ins2="\ \ \ \ \ \ \ \ recursion yes;"
ins3="\ \ \ \ \ \ \ \ listen-on { 10.8.0.1;};"
ins4="\ \ \ \ \ \ \ \ allow-transfer { none; };"
ins5="\ \ \ \ \ \ \ \ \ \ \ \ \ 8.8.8.8;"
ins6="\ \ \ \ \ \ \ \ \ \ \ \ \ 8.8.4.4;"
ins7="\ \ \ \ \ \ \ \ forward only;"

sed -i "3a$ins1" /etc/bind/named.conf.options
sed -i "4a$ins2" /etc/bind/named.conf.options
sed -i "5a$ins3" /etc/bind/named.conf.options
sed -i "6a$ins4" /etc/bind/named.conf.options
sed -i "17 s/\/\/ //" /etc/bind/named.conf.options
sed -i "19 s/\/\/ //" /etc/bind/named.conf.options
sed -i "18a$ins5" /etc/bind/named.conf.options
sed -i "19a$ins6" /etc/bind/named.conf.options
sed -i "21a$ins7" /etc/bind/named.conf.options

sudo systemctl restart bind9
sudo ufw allow Bind9

## Bind9 Adjustments for openvpn

sed -i "14 s/push/;push/" /etc/openvpn/server.conf
sed -i "15 s/push/;push/" /etc/openvpn/server.conf

ins8='push "dhcp-option DNS 10.8.0.1"'

sed -i "16a$ins8" /etc/openvpn/server.conf

sudo systemctl stop openvpn@server
sudo systemctl start openvpn@server

echo "DNS Server Installation Completed"
