import os
import sys
import ctypes
import yaml
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

SETTINGS_FILE = "settings.yml"

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


if not os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "w") as f:
        yaml.dump({
            "blocked_sites": [],
            "check_interval": 1,
            "log_file": "ListApps.txt",
            "processes": [],
            "redirect_ip": "127.0.0.1",
            "shutdown_delay": 10,
            "total_time_seconds": 3600,
            "warning_before_seconds": 300
        }, f)

with open(SETTINGS_FILE, "r") as f:
    settings = yaml.safe_load(f)

def save_settings():
    settings["blocked_sites"] = sites_text.get("1.0", tk.END).strip().splitlines()
    settings["processes"] = processes_text.get("1.0", tk.END).strip().splitlines()
    settings["check_interval"] = int(check_interval_entry.get())
    settings["log_file"] = log_file_entry.get()
    settings["redirect_ip"] = redirect_ip_entry.get()
    settings["shutdown_delay"] = int(shutdown_delay_entry.get())
    settings["total_time_seconds"] = int(total_time_entry.get())
    settings["warning_before_seconds"] = int(warning_before_entry.get())

    with open(SETTINGS_FILE, "w") as f:
        yaml.safe_dump(settings, f)

    messagebox.showinfo("Saved", "Settings saved successfully")

root = tk.Tk()
root.title("Parental Control - OfficerDuck")
root.geometry("500x700")
root.configure(bg="#1E1E2F")
root.iconbitmap("OfficerDuck_logo.ico")

# Logo
if os.path.exists("OfficerDuck_logo.jpg"):
    
    img = Image.open("OfficerDuck_logo.jpg")
    img = img.resize((150,150))
    logo = ImageTk.PhotoImage(img)
    logo_label = tk.Label(root, image=logo, bg="#1E1E2F")
    logo_label.pack(pady=10)

# Settings fields
tk.Label(root, text="Total Time (seconds)", bg="#1E1E2F", fg="white").pack()
total_time_entry = tk.Entry(root)
total_time_entry.pack()
total_time_entry.insert(0, settings.get("total_time_seconds", ""))

tk.Label(root, text="Warning Before (seconds)", bg="#1E1E2F", fg="white").pack()
warning_before_entry = tk.Entry(root)
warning_before_entry.pack()
warning_before_entry.insert(0, settings.get("warning_before_seconds", ""))

tk.Label(root, text="Shutdown Delay (seconds)", bg="#1E1E2F", fg="white").pack()
shutdown_delay_entry = tk.Entry(root)
shutdown_delay_entry.pack()
shutdown_delay_entry.insert(0, settings.get("shutdown_delay", ""))

tk.Label(root, text="Redirect IP", bg="#1E1E2F", fg="white").pack()
redirect_ip_entry = tk.Entry(root)
redirect_ip_entry.pack()
redirect_ip_entry.insert(0, settings.get("redirect_ip", ""))

tk.Label(root, text="Check Interval (seconds)", bg="#1E1E2F", fg="white").pack()
check_interval_entry = tk.Entry(root)
check_interval_entry.pack()
check_interval_entry.insert(0, settings.get("check_interval", ""))

tk.Label(root, text="Log File", bg="#1E1E2F", fg="white").pack()
log_file_entry = tk.Entry(root)
log_file_entry.pack()
log_file_entry.insert(0, settings.get("log_file", ""))

tk.Label(root, text="Blocked Sites (one per line)", bg="#1E1E2F", fg="white").pack()
sites_text = tk.Text(root, height=5)
sites_text.pack()
sites_text.insert(tk.END, "\n".join(settings.get("blocked_sites", [])))

tk.Label(root, text="Processes to Monitor (one per line)", bg="#1E1E2F", fg="white").pack()
processes_text = tk.Text(root, height=5)
processes_text.pack()
processes_text.insert(tk.END, "\n".join(settings.get("processes", [])))

tk.Button(root, text="Save Settings", command=save_settings, bg="#4B6EB1", fg="white").pack(pady=20)

root.mainloop()
