
#!/bin/bash

if [[ $1 = '1' ]]; 
then
	cd shadowsocks/
	sudo  python local.py -c/etc/shadowsocks.json -d start
elif [[ $1 = '2' ]] ;
then
	cd shadowsocks/
	sudo  python local.py -c/etc/shadowsocks.json -d stop

fi



