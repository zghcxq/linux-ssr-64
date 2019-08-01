


https://github.com/zghcxq/linux-ssr-64.git

#进入 Ssrbylinux/

cd Ssrbylinux/





安装混淆依赖 

sudo apt-get install build-essential

wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz

tar zxf LATEST.tar.gz

cd libsodium*

./configure

sudo make && sudo make install

sudo chmod 777 /etc/ld.so.conf.d/usr_local_lib.conf

echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf

ldconfig



#进行初始化

python3 main.py -i







# linux-ssr-64
