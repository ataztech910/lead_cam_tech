#!/bin/sh
pwd
cp /usr/src/app/shared/rules.conf /etc/nimble/
cd /usr/bin/
./nimble --conf-dir=/etc/nimble --log-dir=/var/log/nimble --pidfile=/var/run/nimble/nimble.pid