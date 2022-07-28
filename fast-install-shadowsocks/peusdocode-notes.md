# generate-ss-accounts(ss03-01,)


General House cleaning:
	Generate folders:

	mkdir /root/ss-clients
	mkdir /root/ss-clients/config
	mkdir /root/ss-clients/pid





Input(Servername)





Generate files;

For each Configuration:

		servername-account#
			example

			ss03-01

		# password generator
		replacepass=$(openssl rand -base64 8)

		# port generator
		replaceport=$((RANDOM%15000+40000))

		Generate file
			cp template.json /root/ss-clients/config/<name>.json

		Substitute base with new ports & password
			sed -i "s/55342/$replaceport/g" <name>.json
			sed -i "s/k432qoe2/$replacepass/g" <name>.json

		Open ports on UFW
			ufw allow "$replaceport"/tcp

		Get Host IP address:
			tmp=$(ip -c a | grep inet| grep -v inet6 | grep -v '/8' | grep -v '/32' | awk '{print $2}')
			len=${#tmp}-3
			ipmain="${tmp:0:$len}"

		Generate the sscode:
			Format as follows:

		ss://method:password@ip:port
		encode to base64

			ss://chacha20-ietf-poly1305:$replacepass@$ipmain:$replaceport?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Dwww.bing.com
		example test:
			ss://chacha20-ietf-poly1305:+GpD7+JEOdc=@198.13.59.87:44097?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Dwww.bing.com

			Partial: 
				ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTorR3BENytKRU9kYz0@198.13.59.87:44097?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Dwww.bing.com

			import with port
				ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTorR3BENytKRU9kYz1AMTk4LjEzLjU5Ljg3OjQ0MDk3Cg==?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Dwww.bing.com



				

		Working Example:
				ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpydXNzaWE2NjY@198.13.58.65:54467?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Dwww.bing.com



				
