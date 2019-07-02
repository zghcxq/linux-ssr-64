sudo chmod 777 /etc

cp ../config.json /etc/shadowsocks.json

sudo chmod 777 /etc/shadowsocks.json

 
sudo apt-get install build-essential


cd libsodium*
./configure
sudo make && sudo make install
echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
ldconfig



