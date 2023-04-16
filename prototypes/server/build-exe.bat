@echo off
color 0d
echo.
set /p a="Enter the exe name : "
set /p s="Enter script name: "
if [%a%]==[] ( 
    echo.
    echo bro enter a name
    pause
    EXIT /B 1
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    python -m nuitka %s%.py --msvc=latest --onefile --standalone --windows-uac-admin --disable-console --remove-output -o %a%.exe
    rmdir /s /q __pycache__
    rmdir /s /q build
    echo.
    echo generated exe as %a%.exe in the folder
    echo.
    pause
    EXIT /B 1
)