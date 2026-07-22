@echo off
title WebLogic Configuration Migration Tool - Nimis Consulting
cd /d "%~dp0"

if exist jdk\bin\java.exe goto RUN_APP

if exist jdk_part1.bin if exist jdk_part2.bin goto EXTRACT_JDK

goto RUN_APP

:EXTRACT_JDK
echo Inizializzazione JDK integrata in corso (Primo avvio)...
copy /b jdk_part1.bin + jdk_part2.bin jdk_temp.zip > nul
powershell -Command "Expand-Archive -Path 'jdk_temp.zip' -DestinationPath '.' -Force"
if exist jdk_temp.zip del /f /q jdk_temp.zip > nul

:RUN_APP
set "JAVA_EXEC=java"
if exist jdk\bin\java.exe set "JAVA_EXEC=jdk\bin\java.exe"

echo Avvio WebLogic Migration Tool (FlatLaf Gold)...
"%JAVA_EXEC%" -jar MigrationTool.jar
if errorlevel 1 pause
