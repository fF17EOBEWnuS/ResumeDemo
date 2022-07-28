hold=100 #ms
for arg in "$@"
do
	response=$(ping -c 1  -W5 "$arg")
	if [ $? -ne 0 ]; then
		#when ping is not successful
		echo -e "Device|Firewall|Ping|$arg\t0\t2\tThe Host, $arg cannot be pinged"
	else
		#temp=$(echo $response | awk -F= -vRS=" " '{if($1=="time"){print $2}}')
		#latency=$(printf '%i' ${temp})
		latency=$(echo "$response" | awk -F= -vRS=" " '{if($1=="time"){split($2, number, "."); print number[1]}}')
		#			echo "$latency"
		if [ $latency -gt $threshold ]; then
			echo -e "Device|Firewall|Ping|$arg\t0\t2\tPing MS is currently at $latency ms and is below the $threshold ms threshold. Please verify ping speed by logging into cacalpoller and ping $arg, and call IT Telcom if necessary."
		else
			echo -e "Device|Firewall|Ping|$arg\t$latency\t0\t0"
		fi
	fi
	#       echo "$latency"
done
