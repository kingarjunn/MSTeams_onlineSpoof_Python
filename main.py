import subprocess
import platform
import os
import time

import pygetwindow as gw
import datetime

osystem = str(platform.system())
apps='\AppData\Local\Microsoft\WindowsApps'
app = "ms-teams.exe"
flag = True


def run_command(command):
    # Run the PowerShell command
    process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and errors
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        #print("Output:\n", stdout.decode())
        os.system(os.getenv("USERPROFILE") + apps + "\\" + app)
    return 0



if osystem == 'Windows':
    _user = os.getenv("USERPROFILE")
    applist=os.listdir(_user+apps)
    if applist.__contains__(app):
        #print('true')
        #run_command(f"Set-Location($ENV:USERPROFILE + {apps})")
        process=run_command(f"start {app}")
        time.sleep(10)
        window = gw.getWindowsWithTitle("Microsoft Teams")[0]
        while flag==True:
            window.maximize()
            time.sleep(30)
            window.minimize()
            time.sleep(30)
    else:
        pass
    #run_command("Set-Location($ENV:USERPROFILE + '\AppData\Local\Microsoft\WindowsApps')")"""
    #run_command(app)

