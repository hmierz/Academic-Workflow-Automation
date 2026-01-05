@echo off
echo ================================================
echo Academic Workflow Automation Tool
echo ================================================
echo.
echo Make sure you have:
echo 1. Student ID copied to clipboard
echo 2. SLU system open to starting screen
echo.
echo Press any key to start automation...
pause >nul

cd /d "%~dp0"
python transcript_automation.py

echo.
echo ================================================
echo Press any key to close...
pause >nul
