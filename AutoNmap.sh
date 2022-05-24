#!/bin/bash

IP=$1

if [ $# -lt 1 ]
then
    echo "Usage : $0 <IP address>"
    exit 1
fi

mkdir scans

echo ""
echo "#############################################"
echo "[+] Starting quick TCP scan (1000 ports, T5)"
echo "#############################################"
echo ""

nmap -T5 $IP -oA scans/tcp_quick

echo ""
echo "#############################################"
echo "[+] Starting quick UDP scan (top 100 ports)"
echo "#############################################"
echo ""

nmap -sU --top-ports 100 --reason $IP -oA scans/udp_quick

echo ""
echo "#############################################"
echo "[+] Starting long TCP scan (full ports, sV, sC)"
echo "#############################################"
echo ""

nmap -p- -sC -sV --reason $IP -oA scans/tcp_full

echo ""
echo "#############################################"
echo "[+] Starting long UDP scan (full ports, sV)"
echo "#############################################"
echo ""

nmap -sU -p- --reason --min-rate 5000 $IP -oA scans/udp_full


echo ""
echo "#############################################"
echo "[+] Results" 
echo "#############################################"
echo ""

echo "TODO........"
