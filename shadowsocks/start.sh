sudo chmod 777 /etc

sudo cp ../config.json /etc/shadowsocks.json

sudo chmod 777 /etc/shadowsocks.json

 
sudo apt-get install build-essential



wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
tar zxf LATEST.tar.gz
cd libsodium*
./configure
sudo make && sudo make install
echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
ldconfig


