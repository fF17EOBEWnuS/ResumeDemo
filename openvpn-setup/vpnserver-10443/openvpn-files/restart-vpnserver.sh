#!/bin/sh

sudo systemctl stop openvpn@server
sudo systemctl start openvpn@server
