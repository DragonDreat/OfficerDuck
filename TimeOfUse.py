import time
import os
import ctypes
import yaml

with open("settings.yml", "r") as f:
    settings = yaml.safe_load(f)

TOTAL_TIME_SECONDS = settings.get("total_time_seconds", 20)
WARNING_BEFORE_SECONDS = settings.get("warning_before_seconds", 10)
SHUTDOWN_DELAY = settings.get("shutdown_delay", 10)

warning_shown = False
start_time = time.time()

def show_warning(seconds_left):
    ctypes.windll.user32.MessageBoxW(
        0,
        f"Your computer will shut down in {seconds_left} seconds.\nPlease save your work.",
        "Time Limit Warning",
        0x30
    )

def shutdown_computer():
    os.system(f"shutdown /s /t {SHUTDOWN_DELAY}")

while True:
    elapsed = int(time.time() - start_time)
    remaining = TOTAL_TIME_SECONDS - elapsed

    if remaining <= WARNING_BEFORE_SECONDS and not warning_shown:
        show_warning(remaining)
        warning_shown = True

    if remaining <= 0:
        shutdown_computer()
        break

    time.sleep(1)
