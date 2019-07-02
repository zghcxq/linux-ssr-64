


git clone https://github.com/zghcxq/Ssrbylinux.git

#进入 Ssrbylinux/shadowsocks/ 目录

cd Ssrbylinux/shadowsocks/


#进行初始化

./start.sh


安装混淆依赖 

sudo apt-get install build-essential

wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz

tar zxf LATEST.tar.gz

cd libsodium*

./configure

sudo make && sudo make install

echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf

ldconfig



#要在java环境中

java -jar Ssr.jar


#注意：添加节点失败，重启软件即可



# Ssrbylinux
