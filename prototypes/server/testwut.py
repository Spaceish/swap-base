# server python file
from flask import Flask, render_template, abort, safe_join, send_file
from pathlib import Path
import os
import datetime as dt

# create a server instance
app = Flask(__name__)

port = 80

FolderPath = r"c:\Users"

@app.route('/')
def index():
    return "Hei ce mai faci,<br><img src='https://cdn.discordapp.com/avatars/855745954803482635/12b33622a83e8061e52ed5a648566b92.png?size=1024'> <p style='font-size: 50px;'><b>0ProjectEAI - SUs server</b></p><br><p align='center'><a href=path ><button class=aqua style='height:75px;width:150px'>See files😍💕🥵</button></a></p>"

def getReadableByteSize(num, suffix='B') -> str:
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

def getTimeStampString(tSec: float) -> str:
    tObj = dt.datetime.fromtimestamp(tSec)
    tStr = dt.datetime.strftime(tObj, '%Y-%m-%d %H:%M:%S')
    return tStr

def getIconClassForFilename(fName):
    fileExt = Path(fName).suffix
    fileExt = fileExt[1:] if fileExt.startswith(".") else fileExt
    fileTypes = ["aac", "ai", "bmp", "cs", "css", "csv", "doc", "docx", "exe", "gif", "heic", "html", "java", "jpg", "js", "json", "jsx", "key", "m4p", "md", "mdx", "mov", "mp3",
                 "mp4", "otf", "pdf", "php", "png", "pptx", "psd", "py", "raw", "rb", "sass", "scss", "sh", "sql", "svg", "tiff", "tsx", "ttf", "txt", "wav", "woff", "xlsx", "xml", "yml"]
    fileIconClass = f"bi bi-filetype-{fileExt}" if fileExt in fileTypes else "bi bi-file-earmark"
    return fileIconClass

# route handler
@app.route('/path/', defaults={'reqPath': ''})
@app.route('/path/<path:reqPath>')
def getFiles(reqPath):
    # Join the base and the requested path
    # could have done os.path.join, but safe_join ensures that files are not fetched from parent folders of the base folder
    absPath = safe_join(FolderPath, reqPath)

    # Return 404 if path doesn't exist
    if not os.path.exists(absPath):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(absPath):
        return send_file(absPath)

    # Show directory contents
    def fObjFromScan(x):
        fileStat = x.stat()
        # return file information for rendering
        return {'name': x.name,
                'fIcon': "bi bi-folder-fill" if os.path.isdir(x.path) else getIconClassForFilename(x.name),
                'relPath': os.path.relpath(x.path, FolderPath).replace("\\", "/"),
                'mTime': getTimeStampString(fileStat.st_mtime),
                'size': getReadableByteSize(fileStat.st_size)}
    fileObjs = [fObjFromScan(x) for x in os.scandir(absPath)]
    # get parent directory url
    parentFolderPath = os.path.relpath(
        Path(absPath).parents[0], FolderPath).replace("\\", "/")
    return render_template('ls.html.j2', data={'files': fileObjs,
                                                 'parentFolder': parentFolderPath})

# run the server
app.run(host="192.168.1.7", port=port, debug=True)