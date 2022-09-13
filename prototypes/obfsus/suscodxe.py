from intsus import obfuscate as into, decode as dec

imp: str = "from os import system as sys;from time import sleep as wait"
print(imp)

ah_imp: int = into(imp)
print(ah_imp)

ah_uau: str = dec(ah_imp)
print(ah_uau)

eval(f'exec("{ah_uau}") or print("fuck") or print("anish")')