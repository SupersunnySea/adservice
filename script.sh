#!/bin/sh
#coding=utf8
set -v on

hostname
cat /etc/resolv.conf
uname -a
python -V

pwd

wget -c wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/59.0.2/linux-x86_64/en-US/firefox-59.0.2.tar.bz2
tar -xvf firefox-59.0.2.tar.bz2

rm -rf /usr/lib64/firefox
mv firefox /usr/lib64
ln -s /usr/lib64/firefox/firefox /usr/bin/firefox
chmod a+x /usr/lib64/firefox/firefox

echo $PATH
 
firefox -v

pip3 install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz

tar -zxvf geckodriver-v0.15.0-linux64.tar.gz
mv ./geckodriver /usr/local/bin/
chmod a+x /usr/local/bin/geckodriver
#geckodriver

lsb_release -a
cat /etc/issue

./microservices1.py