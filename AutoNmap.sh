#!/bin/bash

IP=$1

if [ $# -lt 1 ]
then
    echo "Usage : $0 <IP address>"
    exit 1
fi

if [ ! -d scans/ ]
then
    mkdir scans
fi

echo ""
echo "#############################################"
echo "[+] Starting quick TCP scan (1000 ports, T5)"
echo "#############################################"
echo ""

nmap -Pn -T5 $IP -oA scans/tcp_quick

echo ""
echo "#############################################"
echo "[+] Starting quick UDP scan (top 100 ports)"
echo "#############################################"
echo ""

nmap -Pn -sU --top-ports 100 --reason $IP -oA scans/udp_quick

echo ""
echo "#############################################"
echo "[+] Starting long TCP scan (full ports, sV, sC)"
echo "#############################################"
echo ""

nmap -Pn -p- -sC -sV -O --reason $IP -oA scans/tcp_full

echo ""
echo "#############################################"
echo "[+] Starting long UDP scan (full ports, sV)"
echo "#############################################"
echo ""

nmap -Pn -sU -p- --reason --min-rate 5000 $IP -oA scans/udp_full

echo ""
echo "#############################################"
echo "[+] Results" 
echo "#############################################"
# https://github.com/vdjagilev/nmap2md
/opt/nmap2md/nmap2md.py scans/tcp_full.xml
/opt/nmap2md/nmap2md.py scans/udp_full.xml
