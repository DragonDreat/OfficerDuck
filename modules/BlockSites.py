import yaml
import os

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"

with open("settings.yml", "r") as f:
    settings = yaml.safe_load(f)

BLOCKED_SITES = settings.get("blocked_sites", [])
REDIRECT_IP = settings.get("redirect_ip", "127.0.0.1")

with open(HOSTS_PATH, "r+") as hosts_file:
    content = hosts_file.read()
    for site in BLOCKED_SITES:
        entry = f"{REDIRECT_IP} {site}"
        if entry not in content:
            hosts_file.write("\n" + entry)
