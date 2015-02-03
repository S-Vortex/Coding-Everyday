@echo off
start powershell.exe -noexit python server.py 1000
start powershell.exe -noexit python server.py 1001
start powershell.exe -noexit python server.py 1002
start powershell.exe -noexit python client.py 20 localhost 1000 localhost 1001 localhost 1002
pause