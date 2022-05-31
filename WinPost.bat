echo @off
(
echo.
echo ------- SYSTEM INFO -------
echo.
systeminfo
echo.
echo [+] Volumes
echo.
mountvol | find "\"
echo.
echo [+] Shares
echo.
net share
echo.
echo [+] Environment variable
echo.
set
echo.
echo ------- USER INFO -------
echo.
echo %username% || whoami /all
echo.
echo [+] Local users
echo.
net user
echo.
echo [+] Local policy
echo.
net accounts
echo.
echo [+] Local groups
echo.
net localgroup
echo.
echo ------- NETWORK INFO -------
echo.
echo [+] IP configuration
echo.
ipconfig /all
echo.
echo [+] Routing table
echo.
route print
echo.
echo [+] ARP table
echo.
arp -a
echo.
echo [+] Connections
echo.
netstat -ano
echo.
echo [+] Wifi
echo.
netsh wlan show profile
echo.
echo ------- PROCESS INFO -------
echo.
echo [+] Services
echo.
tasklist /svc
echo.
echo [+] Scheduled tasks
echo.
schtasks /query /fo LIST /v
echo.
) > %COMPUTERNAME%.txt 
