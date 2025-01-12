import subprocess
import platform
import os
import time
import ctypes
import pygetwindow as gw
import datetime
from Utils import app1

osystem = str(platform.system())
apps='\AppData\Local\Microsoft\WindowsApps'
app = "ms-teams.exe"
flag = True
s1=False
process=""

def getsleep():
    return s1
def setsleep():
    s1=True

def off_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    print("Turning off sleep in computer temporarily")

def on_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    print("Setting computer to normal sleep state")

def run_command(command):
    # Run the PowerShell command
    process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and errors
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        #print("Output:\n", stdout.decode())
        os.system(os.getenv("USERPROFILE") + apps + "\\" + app)
    return 0

def getTeamsWindow():
    print("Getting Teams INFO...")
    time.sleep(10)
    b=True
    count =0
    while b==True:
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
        count=count+1

def Activate(window):
    while flag == True:
        window.maximize()
        time.sleep(10)
        window.minimize()
        time.sleep(5)


def run():
    if osystem == 'Windows':
        print("Windows Found...")
        off_sleep()
        _user = os.getenv("USERPROFILE")
        applist=os.listdir(_user+apps)
        if applist.__contains__(app):
            print('Teams Found')
            #run_command(f"Set-Location($ENV:USERPROFILE + {apps})")
            process=run_command(f"start {app}")
            #time.sleep(10)
            #window = gw.getWindowsWithTitle("Microsoft Teams")[0]
            Window = getTeamsWindow()
            Activate(Window)

        else:
            app1("Please install the Teams")
            print("please install the team and then try")
            #pass
        #run_command("Set-Location($ENV:USERPROFILE + '\AppData\Local\Microsoft\WindowsApps')")"""
        #run_command(app)
try:
    run()
except:
    on_sleep()
    print("ending task")
    print("Task completed")
    app1("Process Completed")