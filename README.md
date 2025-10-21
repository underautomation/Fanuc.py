# Fanuc Communication SDK for Python

[![UnderAutomation Fanuc communication SDK](https://raw.githubusercontent.com/underautomation/Fanuc.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![Python](https://img.shields.io/badge/Python-3.5_|_3.6_|_3.7_|_3.8|_3.9_|_3.10_|_3.11_|_3.12_-blue)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/fanuc/eula)

### 🤖 Effortlessly Communicate with Fanuc robots

The **Fanuc SDK for Python** enables seamless integration with Fanuc robots for automation, data exchange, and remote control.  
It supports communication with **real robots** and **ROBOGUIDE**.

🔗 **More Information:** [https://underautomation.com/fanuc](https://underautomation.com/fanuc)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/Fanuc.NET)** & **[🟨 LabVIEW](https://github.com/underautomation/Fanuc.vi)**

---

[⭐ Star this repo if it's useful to you!](https://github.com/underautomation/Fanuc.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/Fanuc.py/watchers)

---

## 🚀 TL;DR

- ✔️ **No PCDK needed**: Connect without Fanuc’s Robot Interface
- 📖 **Read/write system variables**
- 🔄 **Register access for numbers, strings, and positions**
- 🎬 **Program control (run, pause, abort, etc.)**
- 🔔 **Alarm viewing and reset**
- ⚡ **I/O control (UI, UO, GI, GO, etc.)**
- 🔍 **State & diagnostics monitoring**
- 📂 **FTP file & variable access**

No additional robot options or installations are required.

---

## 📌 Features

### 🖥️ 1. Telnet KCL Remote Control

Remotely send commands to the robot controller via Telnet KCL.

```python
robot.telnet.reset()
robot.telnet.run("MyProgram")
robot.telnet.pause("MyProgram")
robot.telnet.hold("MyProgram")
robot.telnet.continue_("MyProgram")
robot.telnet.abort("MyProgram", force=True)

robot.telnet.set_variable("my_variable", 42)
robot.telnet.set_variable("$RMT_MASTER", 1)

robot.telnet.set_port("DOUT", 2, 0)
robot.telnet.simulate("DIN", 3, 1)
robot.telnet.unsimulate("DIN", 3)
```

---

### 🚀 2. High-Speed Data via SNPX (RobotIF)

SNPX provides fast, structured data exchange with the robot.

```python
# Read/write position registers
position = robot.snpx.position_registers.read(1)
robot.snpx.position_registers.write(2, {"x": 100, "y": 50, "z": 25})

# Read/write numeric registers
value = robot.snpx.registers.read(1)
robot.snpx.registers.write(2, 123.45)

# Digital signals
ui_1 = robot.snpx.ui.read(1)
robot.snpx.uo.write(3, True)

# Alarms & status
robot.snpx.clear_alarms()
position = robot.snpx.current_position.read_world_position()
user_frame = robot.snpx.current_position.read_user_frame_position(1)
```

---

### 📂 3. FTP File and Variable Management

Transfer files and manage internal robot data via FTP.

```python
# File transfer
robot.ftp.direct_file_handling.upload_file_to_controller("C:/Programs/MyPrg.tp", "md:/MyPrg.tp")
robot.ftp.direct_file_handling.download_file_from_controller("md:/Backup.va", "C:/Backup/Backup.va")
robot.ftp.direct_file_handling.delete_file("md:/OldProgram.tp")

# Variables
variables = robot.ftp.get_all_variables()
for var in variables:
    print(f"{var.name} = {var.value}")

# System variables
remote_mode = robot.ftp.known_variable_files.get_system_file().rmt_master

# Safety status
safety = robot.ftp.get_safety_status()
print(f"E-Stop: {safety.external_estop}, TP Enabled: {safety.tp_enable}")

# Position
position = robot.ftp.get_current_position()
print(f"X={position.cartesian.x}, Y={position.cartesian.y}, Z={position.cartesian.z}")
```

---

## 🔧 Robot Configuration

### ✅ Enable Telnet KCL

- Go to `SETUP > Host Comm`
- Select `TELNET` → `[DETAIL]`
- Set a password and reboot

### ✅ Enable FTP

- Go to `SETUP > Host Comm > FTP`
- Set username/password
- Perform a cold start

### ✅ Enable SNPX

- For **FANUC America (R650 FRA)**: Enable option R553 “HMI Device SNPX”
- For **FANUC Ltd. (R651 FRL)**: No additional options required

---

## 🛠 Installation

### 1️⃣ Clone or Download

This SDK is not on PyPI (yet). Clone this repository and install dependencies :

```bash
git clone https://github.com/underautomation/Fanuc.py.git
cd Fanuc.py
pip install -e .
```

### 2️⃣ Connect to Your Robot

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters

robot = FanucRobot()
robot.connect(ConnectionParameters("192.168.0.1"))
```

---

## 🔍 Compatibility

✅ **Robot Controllers:** R-J3iB, R-30iA, R-30iB  
✅ **OS:** Windows, Linux, macOS  
✅ **Python:** 3.5+

---

## 📢 Contributing

We welcome your feedback and contributions!

- Report issues via [GitHub Issues](https://github.com/underautomation/Fanuc.py/issues)
- Submit pull requests with enhancements
- Suggest features and improvements

---

## 📜 License

**⚠️ This SDK requires a commercial license.**  
🔗 Learn more: [UnderAutomation Licensing](https://underautomation.com/fanuc/eula)

## 📬 Need Help?

- 📖 **Documentation**: [https://underautomation.com/fanuc/documentation](https://underautomation.com/fanuc/documentation)
- 📩 **Contact Us**: [https://underautomation.com/contact](https://underautomation.com/contact)
