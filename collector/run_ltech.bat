@echo off
cd /d D:\projects\智能照明方案馆\collector
C:\Users\shzhangzhongze\AppData\Local\Programs\Python\Python313\python.exe -u scripts\collect_all_ltech.py > D:\temp\ltech_collect.log 2>&1
echo DONE >> D:\temp\ltech_collect.log
