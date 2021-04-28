# automatic login to pulchowk campus internet
# replace USER value with your username and PASSWORD with your own
# the ETHERNET_CARD and WIFI_CARD are used in case you also want to 
# automatically open hotsopt if you connect from an ethernet cable

#!/usr/bin/bash

USER=pcampus_username
PASSWORD=password
ETHERNET_CARD=enp2s0
WIFI_CARD=wlp3s0

# to see specific hostspot uuid, $ nmcli connection show 
HOTSPOT_UUID=54f8331a-e76d-43b5-8298-8e9907adebac

curl -d "mode=191&username=$USER&password=$PASSWORD" http://10.100.1.1:8090/login.xml 

# check if the ethernet is connected and open hotspot automatically
# if you wifi driver/network card is active, do not open hotspot
# if you don't want to automatic hostspot comment out all code below
ETHERNET_CONNECTED=$(cat /sys/class/net/$ETHERNET_CARD/carrier)
WIFI_CONNECTED=$(cat /sys/class/net/$WIFI_CARD/carrier)
if [ $ETHERNET_CONNECTED -eq 1 ] && [ $WIFI_CONNECTED -eq 0 ]
then
  echo "Connected!"
  nmcli connection up $HOTSPOT_UUID
fi
