(
echo "------- USER INFO -------"


echo %username% || whoami /all


echo "[+] Local users"
net user


echo "[+] Local policy"
net accounts


echo "[+] Local groups"
net localgroup


echo "------- NETWORK INFO -------"


echo "[+] IP configuration"
ipconfig /all


echo "[+] Routing table"
route print


echo "[+] ARP table"
arp -a

echo "[+] Connections"
netstat -ano

) > %COMPUTERNAME%.txt 
