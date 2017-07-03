echo off
cls
echo Fazendo Backup
echo.
echo Inicio do processo = %time%
set T_INI = %time%
"C:\Program Files (x86)\pgAdmin III\1.22\pg_dump.exe" -U postgres -h localhost -d BD2 -p 5432 --format directory --file C:\Users\edson\Desktop\batfiles\outputfiles\BD2.backup
set T_FIM = %time%
set T_COM = T_INI - T_FIM
echo Fim do processo = %time%
REM echo Tempo decorrido = %T_COM%