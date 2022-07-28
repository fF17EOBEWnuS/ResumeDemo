#!/bin/sh

tar zcvf default.tar.gz files/simple-obfs files/default.json 
cat files/extract.sh default.tar.gz > files/installer.sh
chmod +x files/installer.sh
rm default.tar.gz
