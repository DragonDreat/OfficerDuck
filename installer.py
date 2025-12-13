import os
import sys
import shutil
import ctypes
import winreg
import subprocess

APP_NAME = "ParentalControl"
MODULES = [
    "client.exe",
    "site_blocker.exe",
    "time_of_use.exe",
    "process_monitor.exe",
    "settings.yml",
    "administrator.exe"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        " ".join(sys.argv),
        None,
        1
    )
    sys.exit(0)

USER_DIR = os.path.expanduser("~")
INSTALL_DIR = os.path.join(USER_DIR, APP_NAME)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.makedirs(INSTALL_DIR, exist_ok=True)

for item in MODULES:
    src = os.path.join(BASE_DIR, item)
    dst = os.path.join(INSTALL_DIR, item)
    if os.path.exists(src):
        shutil.copy2(src, dst)

def add_to_startup():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    client_path = os.path.join(INSTALL_DIR, "client.exe")

    winreg.SetValueEx(
        key,
        APP_NAME,
        0,
        winreg.REG_SZ,
        f'"{client_path}"'
    )

    winreg.CloseKey(key)

add_to_startup()

admin_path = os.path.join(INSTALL_DIR, "administrator.exe")
if os.path.exists(admin_path):
    subprocess.Popen(
        admin_path,
        cwd=INSTALL_DIR,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

print("Installation completed successfully.")
