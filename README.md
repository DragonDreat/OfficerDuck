<h1 align="center">🦆 OfficerDuck – Parental Control</h1>

<p align="center">
<b>Source Code Repository</b><br>
Windows-based parental control system
</p>

<hr>

<h2 align="center">🚧 Project Status</h2>

<p align="center">
<b>IN PROGRESS</b><br>
This project is under active development.
</p>

<p align="center">
Features, structure, and implementation details may change.<br>
This repository contains <b>source code only</b>.
</p>

<hr>

<h2 align="center">✨ Current Features</h2>

<ul>
  <li><b>Time Of Use Control</b> with warning and automatic shutdown</li>
  <li><b>System-wide Website Blocking</b> using the Windows hosts file</li>
  <li><b>Application & Process Monitoring</b></li>
  <li><b>Background Watchdog Client</b> with auto-restart logic</li>
  <li><b>Centralized YAML Configuration</b></li>
  <li><b>Administrator-level execution support</b></li>
</ul>

<hr>

<h2 align="center">⚙️ Configuration</h2>

<p align="center">
All system behavior is controlled via a single configuration file:
</p>

<pre>
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

total_time_seconds: 20
warning_before_seconds: 10
shutdown_delay: 10
</pre>

<hr>

<h2 align="center">🗂 Project Structure</h2>

<pre>
ParentalControl/
│
├── client.py
├── site_blocker.py
├── time_of_use.py
├── process_monitor.py
├── installer.py
├── administrator.py
├── settings.yml
</pre>

<p align="center">
Executable (<b>.exe</b>) builds are generated separately and are not included in this repository.
</p>

<hr>

<h2 align="center">🛠 Built With</h2>

<ul>
  <li>Python</li>
  <li>PyYAML</li>
  <li>psutil</li>
  <li>Windows API (ctypes, registry, system calls)</li>
</ul>

<hr>

<h2 align="center">📜 License</h2>

<p align="center">
<b>Unlicensed</b><br>
All rights reserved unless stated otherwise.<br>
License terms may be added in the future.
</p>

<hr>

<h2 align="center">ℹ️ Notes</h2>

<ul>
  <li>No kernel drivers or system exploits</li>
  <li>Uses standard Windows startup mechanisms</li>
  <li>Designed for development and testing purposes</li>
  <li>Not intended for production use in its current state</li>
</ul>

<hr>

<p align="center">
<b>OfficerDuck Parental Control</b><br>
Simple rules. Strong boundaries.
</p>
