@echo off
cls
color 6
title Sus Writer
set /p "file= > Enter the name of the file: "
set /p "impdir= > Enter the import dir: "
set /p "method= > Enter the preferred method to use: ('hex int' or 'int') "
set /p "payload= > Enter the payload (as one line and compressed as possible if possible lmao 😶‍🌫️): "
set /p "debug= > Enter debug mode: ('True' or 'False') "
cd prototypes/obfsus
python test_writer.py "%file%" "%impdir%" "%method%" "%payload%" %debug%
title sus - done
echo Done