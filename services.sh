#!/bin/sh

# Else oocalc will crash
mknod /dev/random c 1 8 &
chmod a+rw /dev/tty /dev/ptmx

mkdir /var/lock/subsys
chmod 1777 /var/lock/subsys
mkdir /var/run/dbus &
mkdir /var/run/netreport &
mkdir /var/run/ConsoleKit &
mkdir /var/log &

/etc/init.d/network start
/etc/init.d/alsa start
/etc/init.d/sound start

sleep 20

/sbin/start_udev
PATH=/sbin:/bin /etc/rc.modules

/etc/init.d/haldaemon start

for i in /etc/rc5.d/S*; do
	$i status > /dev/null 2>&1 || $i start
done
