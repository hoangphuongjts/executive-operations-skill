@echo off
setlocal
cd /d "%~dp0"
where git >nul 2>&1
if errorlevel 1 (
 echo CHUA CO Git. Cai tai https://git-scm.com/downloads
 pause
 exit /b 1
)
where gh >nul 2>&1
if errorlevel 1 (
 echo CHUA CO GitHub CLI. Cai tai https://cli.github.com/
 pause
 exit /b 1
)
where python >nul 2>&1
if errorlevel 1 (
 echo CHUA CO Python. Cai Python 3 tu trang chinh thuc.
 pause
 exit /b 1
)
gh auth status >nul 2>&1
if errorlevel 1 (
 echo Chua dang nhap GitHub. Mo quy trinh dang nhap tren trinh duyet...
 gh auth login --hostname github.com --git-protocol https --web
 if errorlevel 1 (
   echo Dang nhap khong thanh cong. Khong tao repo.
   pause
   exit /b 1
 )
)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\PUBLISH_PRIVATE_GITHUB.ps1"
if errorlevel 1 (
 echo Chua tao / day repo thanh cong. Xem thong bao phia tren.
 pause
 exit /b 1
)
echo Ket thuc quy trinh. Kiem tra link GitHub private o tren.
pause
