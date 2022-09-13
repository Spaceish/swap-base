from sys import argv as g
from intsus import obfuscate as into, decode as dec

# variabiles
file_name, import_dir, method, payload = g[1] + '.py', g[2], g[3], g[4]

# debug mode
debug: bool = g[5]
debug_prefix = '[TEST] '

# debug check (logs variabiles)
if debug: print(f'{debug_prefix}File name: {file_name}\nImport dir: {import_dir}\nChoosed method: {method}\nPayload: {payload}')

# methods
methods: dict = {
    'hex int': [hex(int(into(payload))), dec(int(hex(int(into(payload))), 16))], # hex int obfuscate and decode
    'int': [into(payload), dec(into(payload))] # int obfuscation and decode
}

# # escape imports with exec
# if debug: print(f'{debug_prefix}Escaping imports in payload .. lol')# debug check (escape imports)
# lols = payload.split('or')
# for i in range(len(lols)):
#     if lols[i].startswith('from' or 'import'):
#         lol = f'exec({word})'


code: str = f'from {import_dir} import decode as dec;eval(dec({methods[method][0]}))'

# debug check (logs generated code)
if debug: print(f'{debug_prefix}Code: {code}')

# make file with the choosed file name lol
if debug: print('{debug_prefix}Making file with the choosed file name lol.') # debug checks (making file)
with open(file_name, 'w') as f:
    # writing code to file
    if debug: print('{debug_prefix}Writing generated code to file xd ;)') # debug check (writing code to file)
    f.write(code)
    # debug check (done operation)
    if debug: print('{debug_prefix}Done writing specified code to file xddd.')
    # closing file 
    if debug: print('{debug_prefix}Closing file :)')
    f.close()