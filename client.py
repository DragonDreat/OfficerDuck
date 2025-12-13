import subprocess
import time
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODULES = [
    "modules/BlockSites.py",
    "modules/TimeOfUse.py",
    "modules/apps_ControlSystem.py"
]

processes = {}

def start_process(script):
    return subprocess.Popen(
        [sys.executable, os.path.join(BASE_DIR, script)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

for module in MODULES:
    processes[module] = start_process(module)

while True:
    for module, proc in processes.items():
        if proc.poll() is not None:
            processes[module] = start_process(module)
    time.sleep(2)
