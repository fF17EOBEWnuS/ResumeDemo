This project is for setting up fast available servers for shadowsocks on chinese server to create new IP locations for phones (genymotion android emulation) to purchase and cancel orders easily. 

Requirements:

	* Single script
	* Payload included
	* Single command executable extraction 

 

Single Script Payload Method:
https://stackoverflow.com/questions/29418050/package-tar-gz-into-a-shell-script

Site Example:

	#!/bin/bash
	# a self-extracting script header
	
	# this can be any preferred output directory
	mkdir ./output_dir
	
	# determine the line number of this script where the payload begins
	PAYLOAD_LINE=`awk '/^__PAYLOAD_BELOW__/ {print NR + 1; exit 0; }' $0`
	
	# use the tail command and the line number we just determined to skip
	# past this leading script code and pipe the payload to tar
	tail -n+$PAYLOAD_LINE $0 | tar xzv -C ./output_dir
	
	# now we are free to run code in output_dir or do whatever we want
	
	exit 0
	
	# the 'exit 0' immediately above prevents this line from being executed
	__PAYLOAD_BELOW__

Then you want to pipe the tar.gz file into the original script:

	cat extract.sh payload.tar.gz > final.sh
