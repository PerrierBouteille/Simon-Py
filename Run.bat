@echo off
set LOGFILE=ColorGame.log
call :LOG > %LOGFILE%
exit /B

:LOG
C:\EDUPYT~1\App\python.exe P:\Documents\Simon-Py-main\Game\main.py

