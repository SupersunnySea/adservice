#!/bin/sh
#coding=utf8
set -v on
echo $PATH

hostname
cat /etc/resolv.conf

python -V

pwd
ls /usr/bin/firefox/

ls /usr/local/bin/firefox/
find  / -name firefox
pip3 install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz

tar -zxvf geckodriver-v0.15.0-linux64.tar.gz

./microservices1.py