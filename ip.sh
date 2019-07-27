#!/bin/bash

for $ip in `seq 1 254`; 
	do nmap 192.168.1.$ip & cat ip.txt;

exit 0;
