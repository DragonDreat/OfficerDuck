import psutil
import time
from datetime import datetime
import yaml

with open("settings.yml", "r") as f:
    settings = yaml.safe_load(f)

PROCESS_LIST = settings.get("processes", [])
LOG_FILE = settings.get("log_file", "List.txt")
CHECK_INTERVAL = settings.get("check_interval", 1)

already_running = {proc_name: False for proc_name in PROCESS_LIST}

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
            return True
    return False

with open(LOG_FILE, "a") as file:
    while True:
        for process_name in PROCESS_LIST:
            running = is_process_running(process_name)
            
            if running and not already_running[process_name]:
                file.write(f"Process started: {process_name}\n")
                file.write(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.flush()
                already_running[process_name] = True

            if not running and already_running[process_name]:
                file.write(f"Stopped: {process_name} at {datetime.now().strftime('%H:%M:%S')}\n")
                file.flush()
                already_running[process_name] = False

        time.sleep(CHECK_INTERVAL)
