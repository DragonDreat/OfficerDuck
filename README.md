<h1 align="center">🦆 OfficerDuck – Parental Control System</h1>

<p align="center">
<b>Windows-based Parental Control & Time-of-Use System</b>
</p>

<hr>

<h2 align="center">✨ Features</h2>

<ul>
  <li><b>Time Of Use Control:</b> Set total allowed computer usage, show warnings before time expires, and perform safe shutdown automatically.</li>
  <li><b>Website Blocking:</b> Block unwanted websites system-wide using the Windows hosts file; works on all major browsers.</li>
  <li><b>Application & Process Monitoring:</b> Monitor multiple processes (games, browsers, launchers) and log usage to a central file.</li>
  <li><b>Background Client (Watchdog):</b> Automatically restarts protection modules if stopped to ensure continuous protection.</li>
  <li><b>Administrator GUI:</b> Run with elevated permissions to safely modify settings, including blocked sites, processes, and time limits.</li>
  <li><b>Centralized Configuration:</b> All parameters stored in a single YAML file for easy customization.</li>
  <li><b>Installer:</b> Automatically sets up the program, creates the ParentalControl folder in the user directory, and adds the client to startup.</li>
</ul>

<hr>

<h2 align="center">⚙️ Configuration</h2>

<p align="center">
All settings are stored in <b>settings.yml</b>.
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

total_time_seconds: 7200
warning_before_seconds: 300
shutdown_delay: 10
</pre>

<hr>

<h2 align="center">🗂 Project Structure</h2>

<pre>
ParentalControl/
│
├── client.py             # Watchdog client
├── site_blocker.py       # Hosts-based website blocking
├── time_of_use.py        # Time limit logic & shutdown
├── process_monitor.py    # Application monitoring
├── installer.py          # Installer script
├── administrator.py      # Admin GUI
├── settings.yml          # Configuration file
</pre>

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
MIT License<br>
</p>

<hr>

<h2 align="center">🚧 Project Status</h2>

<p align="center">
<b>IN PROGRESS</b><br>
Modules and features are actively being developed.<br>
This repository contains the source code and scripts for testing and development purposes.
</p>
<img src="https://i.imgur.com/U6tIH5a.jpeg" align="center">
