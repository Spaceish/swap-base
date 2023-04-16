@echo off
color 0a
echo.
set /p a="Enter the exe name : "
set /p s="Enter the script name: "
if [%a%]==[] ( 
    echo.
    echo bro enter a name
    pause
    EXIT /B 1
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    echo Script is: %s%
    python -m nuitka prototypes/startupsus/%s%.py --msvc=latest --onefile --standalone --disable-console --remove-output -o %a%.exe
    rmdir /s /q __pycache__
    rmdir /s /q build
    echo.
    echo generated exe as %a%.exe in the folder
    echo.
    pause
    EXIT /B 1
)