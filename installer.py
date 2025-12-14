import os
import shutil
import subprocess

APP_NAME = "OfficerDuck"
FILES = [
    "client.exe",
    "BlockSites.exe",
    "TimeOfUse.exe",
    "apps_ControlSystem.exe",
    "settings.yml",
    "administrator.exe",
    "installer.exe",
    "OfficerDuck_Logo.ico",
    "OfficerDuck_Logo.jpg",
    "ListApps.txt"
]


USER_DIR = os.path.expanduser("~")
INSTALL_DIR = os.path.join(USER_DIR, APP_NAME)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ADMIN_PATH = os.path.join(INSTALL_DIR, "administrator.exe")
STARTUP_PATH = os.path.join(USER_DIR, "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

os.makedirs(INSTALL_DIR, exist_ok=True)

for item in FILES:
    src = os.path.join(BASE_DIR, item)
    dst = os.path.join(INSTALL_DIR, item)
    if os.path.exists(src):
        shutil.copy2(src, dst)

def add_to_startup():
    SOURCE = os.path.join(INSTALL_DIR, "client.exe")
    if(os.path.exists(SOURCE)):
        shutil.copy2(SOURCE, STARTUP_PATH)

def add_admin_to_folder():
    ADMIN_SAVE_DIR = os.path.join(USER_DIR, "AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
    if os.path.exists(ADMIN_PATH):
        shutil.copy2(ADMIN_PATH, ADMIN_SAVE_DIR)

    

add_to_startup()
add_admin_to_folder()

if os.path.exists(ADMIN_PATH):
  subprocess.Popen(
     ADMIN_PATH,
     cwd=INSTALL_DIR,
    creationflags=subprocess.CREATE_NEW_CONSOLE
  )

print("Installation completed successfully.")
