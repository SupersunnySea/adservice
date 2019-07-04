#!/bin/sh
#coding=utf8
set -v on
echo $PATH

hostname
cat /etc/resolv.conf

python -V

pwd

pip3 install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

tar -zxvf geckodriver-v0.24.0-linux64.tar.gz

./microservices1.py