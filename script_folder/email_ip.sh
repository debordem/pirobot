#!/bin/sh
HOSTNAME=$(hostname)

SUBJ="$HOSTNAME Ip Address"
EMAIL="debordem@isdedu.de"
ip1=""
ip2=""

read ip1 < ip.txt
ip2=$(hostname -I | tr -d '[:space:]')

echo "$ip1"
echo "$ip2"
if [ "$ip1" = "$ip2" ]; 
then
  echo "exit"
  exit
else
  echo "update"
  echo "$ip2" > ip.txt
  echo "$ip2" | mail -s "$SUBJ" $EMAIL
  exit
fi
