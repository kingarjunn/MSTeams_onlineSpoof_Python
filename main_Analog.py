import pyautogui as pgui
import subprocess
import platform
import os
import time
import ctypes
import pygetwindow as gw
import datetime
from Utils import app1

osystem = str(platform.system())
apps = '\AppData\Local\Microsoft\WindowsApps'
app = "ms-teams.exe"
flag = True
s1 = False
process = ""


def run_command(command):
    # Run the PowerShell command
    process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and errors
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        # print("Output:\n", stdout.decode())
        os.system(os.getenv("USERPROFILE") + apps + "\\" + app)
    return 0

def getTeamsWindow():
    time.sleep(10)
    b = True
    count = 0
    while b == True:
        if count > 10:
            b = False
            app1("Please Manually open the teams and restart the script")
            raise Exception("Please Manually open the teams and restart the script")
        if count > 0:
            print(f"Retrying {count} : Getting teams info")
        try:
            win = gw.getWindowsWithTitle("Microsoft Teams")[0]
            return win
        except:
            pass
        count = count + 1

def run():
    if osystem == 'Windows':
        print("Windows Found...")
        _user = os.getenv("USERPROFILE")
        applist = os.listdir(_user + apps)
        if applist.__contains__(app):
            print('Teams Found')
            print("Getting Teams INFO...\n process as Started Sit back and relax")
            process = run_command(f"start {app}")
            Window = getTeamsWindow()
            x, y = pgui.size()
            if x >= 15 and y >= 15:
                pgui.FAILSAFE = False
                while True:
                    Window.maximize()
                    time.sleep(10)
                    pgui.click(x,y)
                    time.sleep(10)
                    Window.minimize()
                    time.sleep(10)
        else:
            app1("Please install the Teams")
            print("please install the team and then try")

try:
    run()
except Exception as ex:
    print(f"--------------------------------\n{str(ex)}\n-----------------------------------")
    print("ending task")
    print("Task completed")
    app1("Process Completed")