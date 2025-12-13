🦆 OfficerDuck – Parental Control System

OfficerDuck Parental Control is a lightweight Windows‑based parental control and time‑management system designed to help parents monitor and limit computer usage in a clean, transparent, and configurable way.

Built with Python, powered by YAML configuration, and designed with modularity and safety in mind.

✨ Features
⏱ Time Of Use Control

Define total allowed computer usage time

Automatic warning before time expires

Safe system shutdown when time limit is reached

Fully configurable via settings.yml

🌐 Website Blocking (Hosts‑Based)

Block unwanted websites using the Windows hosts file

Simple configuration (no browser extensions needed)

Blocks apply system‑wide (Chrome, Firefox, Edge, etc.)

Automatic re‑apply on system startup

📊 Application & Process Monitoring

Monitor selected applications (games, browsers, launchers)

Detect when monitored processes start or stop

Centralized logging system

Supports multiple processes at once

🔁 Self‑Healing Client (Watchdog)

Background client that starts on Windows login

Automatically restarts protection modules if stopped

Designed to resist accidental termination

Uses legitimate Windows startup mechanisms

⚙️ Centralized Configuration (YAML)

All behavior is controlled from a single file:

blocked_sites:
- pornhub.com
- site.com

processes:
- FortniteLauncher.exe
- chrome.exe
- firefox.exe

check_interval: 1
log_file: ListApps.txt
redirect_ip: 127.0.0.1

total_time_seconds: 7200
warning_before_seconds: 300
shutdown_delay: 10


No code changes required — just edit the config.

🖥 Administrator Panel

Dedicated Administrator GUI

Runs with elevated permissions

Allows safe modification of settings

Designed for parents, not children


🚀 Installation

Run installer.exe

Approve Administrator permissions

The system installs automatically

Administrator Panel opens after installation

Protection starts on every login

🔐 Security & Transparency

No kernel drivers

No hidden system hooks

No data collection

No internet communication

Uses standard Windows APIs only

OfficerDuck is designed to be protective, not intrusive.

🧠 Philosophy

Good parental control is not about spying —
it’s about setting healthy boundaries.

OfficerDuck focuses on:

Predictability

Configurability

Stability

Respect for the system

🛠 Built With

Python

PyYAML

Windows API

Native Windows startup mechanisms

📜 License

This project is intended for educational and personal use.

🦆 OfficerDuck
<img src="https://i.imgur.com/U6tIH5a.jpeg" alt="OfficerDuck Logo" width="200"/>

OfficerDuck Parental Control
Simple rules. Strong boundaries.
