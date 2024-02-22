@echo off

:loop
cd C:\Users\Administrator\Documents\GitHub\tkibots
git pull
timeout /t 10
goto loop
