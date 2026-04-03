# Fanuc Communication SDK for Python

[![UnderAutomation Fanuc communication SDK](https://raw.githubusercontent.com/underautomation/Fanuc.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.Fanuc?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.Fanuc/)
[![Python](https://img.shields.io/badge/Python-3.7_|_3.8_|_3.9_|_3.10_|_3.11_|_3.12-blue?logo=python)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#)
[![License](https://img.shields.io/badge/License-Commercial-red)](https://underautomation.com/fanuc/eula)

### 🤖 Effortlessly Communicate with Fanuc Robots

The **Fanuc SDK for Python** enables seamless integration with Fanuc robots for automation, data exchange, and remote control through multiple native communication protocols.

> Whether you're building a custom application, integrating with a MES/SCADA system, or performing advanced diagnostics, this SDK provides the tools you need.

It supports communication with **real robots** and **ROBOGUIDE** simulation.

🔗 **More Information:** [https://underautomation.com/fanuc](https://underautomation.com/fanuc)  
🔗 Also available in **[🟦 .NET](https://github.com/underautomation/Fanuc.NET)** & **[🟨 LabVIEW](https://github.com/underautomation/Fanuc.vi)**

---

[⭐ Star this repo if it's useful to you!](https://github.com/underautomation/Fanuc.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/Fanuc.py/watchers)

---

## 🚀 TL;DR

- ✔️ **No PCDK needed** - Connect without Fanuc's Robot Interface
- 📖 **Read/write system variables**
- 🔄 **Register access** for numbers, strings, and positions
- 🎬 **Program control** (run, pause, abort, etc.)
- 🔔 **Alarm viewing and reset**
- ⚡ **I/O control** (UI, UO, GI, GO, SDI, SDO, etc.)
- 🔍 **State & diagnostics monitoring**
- 📂 **FTP file & variable access**
- 🌐 **CGTP Web Server** - programs, variables, registers, I/O, kinematics, batch operations
- 🏎️ **Remote motion:** Remote move the robot
- 📐 **Kinematics Calculations:** Perform forward and inverse kinematics offline (CRX and standard robots)

> No custom robot options or installations are required. The SDK uses **standard communication** protocols available on all Fanuc controllers.

---

## 🛠 Installation & Getting Started

### Prerequisites

- **Python 3.7** or higher
- A Fanuc robot or **ROBOGUIDE** simulation

### Step 1 - Create a Virtual Environment

We recommend using a virtual environment to keep your project dependencies isolated.

Open a terminal (Command Prompt, PowerShell, or your favorite terminal) and run:

```bash
# Create a project folder
mkdir my-fanuc-project
cd my-fanuc-project

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 2 - Install the SDK

The SDK is published on PyPI. Install it with a single command:

```bash
pip install UnderAutomation.Fanuc
```

That's it! All dependencies (including `pythonnet`) are installed automatically.

On **Linux**, you should also install .NET Core and set environment variable PYTHONNET_RUNTIME to coreclr :

```bash
sudo apt-get install -y dotnet-runtime-8.0
PYTHONNET_RUNTIME=coreclr
```

> **Alternative: install from source**
>
> ```bash
> git clone https://github.com/underautomation/Fanuc.py.git
> cd Fanuc.py
> pip install -e .
> ```

### Step 3 - Connect to Your Robot

Create a Python file (e.g. `main.py`) and write:

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.common.languages import Languages

# Create a robot instance
robot = FanucRobot()

# Connect (replace with your robot's IP address)
params = ConnectionParameters('192.168.0.1')

# Set the controller language among English, Japanese and Chinese (optional, defaults to English)
params.language = Languages.English

# Enable Telnet KCL
# Activate Telnet on your robot or ROBOGUIDE : https://underautomation.com/fanuc/documentation/enable-telnet
params.telnet.enable = True
params.telnet.telnet_kcl_password="telnet_password"


# Enable FTP
params.ftp.enable = True
params.ftp.ftp_user = ""
params.ftp.ftp_password = ""

# Enable CGTP Web Server
params.cgtp.enable = True
params.cgtp.login = ""
params.cgtp.password = ""

# Enable SNPX
# You need option R553 "HMI Device SNPX" for FANUC America (R650 FRA)
# No additional options needed for FANUC Ltd. (R651 FRL)
params.snpx.enable = True

# Connect to the robot
# If you get a license exception, ask a trial license here: https://underautomation.com/license and call FanucRobot.register_license(...) before connecting
robot.connect(params)

if robot.ftp.connected:
    safety = robot.ftp.get_safety_status()
    print(f"Safety Status:")
    print(f"  External E-Stop  : {safety.external_e_stop}")
    print(f"  SOP E-Stop       : {safety.sope_stop}")
    print(f"  TP E-Stop        : {safety.tpe_stop}")
    print(f"  TP Enable        : {safety.tp_enable}")
    print(f"  TP Deadman       : {safety.tp_deadman}")
    print()

if robot.snpx.connected:
    position = robot.snpx.current_position.read_world_position(1)
    print(position)
    r1 = robot.snpx.numeric_registers.read(1)
    print(f"  R[1] = {r1}")
    print()

if robot.telnet.connected:
    speed_override = robot.telnet.get_variable("$MCR.$GENOVERRIDE")
    print(f"Speed override: {speed_override.raw_value}%")
    print()

# Don't forget to disconnect
robot.disconnect()
```

Run it:

```bash
python main.py
```

> **Connecting to ROBOGUIDE?** Instead of an IP address, pass the workcell path:
>
> ```python
> params = ConnectionParameters(r"C:\Users\you\Documents\My Workcells\CRX 10iA L\Robot_1")
> ```

---

## 🔑 Licensing

The SDK works out of the box for **30 days** (trial period) - no registration needed.

After the trial, you can:

- **Buy a license** at [underautomation.com/order](https://underautomation.com/order?sdk=fanuc)
- **Get a new trial period immediately by email** at [underautomation.com/license](https://underautomation.com/license?sdk=fanuc)

To register a license in code:

```python
from underautomation.fanuc.fanuc_robot import FanucRobot

license_info = FanucRobot.register_license("your-licensee", "your-license-key")
print(license_info)
```

---

## 📂 Examples

The repository includes a complete set of ready-to-run examples in the [`examples/`](https://github.com/underautomation/fanuc.py/tree/main/examples) folder, organized by communication protocol.

### How the Examples Work

| File                                                                                                 | Role                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [`examples/launcher.py`](https://github.com/underautomation/fanuc.py/blob/main/examples/launcher.py) | **Interactive menu** - browse and run any example from a single launcher                                                               |
| [`examples/__init__.py`](https://github.com/underautomation/fanuc.py/blob/main/examples/__init__.py) | **Shared helpers** - sets up the Python path, manages robot connection settings, and handles license registration                      |
| `examples/robot_config.json`                                                                         | **Saved settings** (git-ignored) - remembers your robot IP, credentials, and license key so you don't have to re-enter them every time |

**Run manually each examples**

> The first time you run an example, it will ask for your robot IP (or ROBOGUIDE path) and credentials. These are saved in `robot_config.json` so you only enter them once.

```bash
# run any example directly
python examples/snpx/snpx_write_numeric_register.py
```

**Or browse examples with the launcher:**

Use the launcher to easily browse and run any example without needing to open each file.

```bash
# Launch the interactive menu
python examples/launcher.py
```

And you will get a menu like this to select and run any example with a single keystroke:

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                   ███████╗ █████╗ ███╗   ██╗██╗   ██╗ ██████╗                  ║
║                   ██╔════╝██╔══██╗████╗  ██║██║   ██║██╔════╝                  ║
║                   █████╗  ███████║██╔██╗ ██║██║   ██║██║                       ║
║                   ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║██║                       ║
║                   ██║     ██║  ██║██║ ╚████║╚██████╔╝╚██████╗                  ║
║                   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝                  ║
║                                                                                ║
║                    Python SDK - Interactive Example Launcher                   ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════════════╗
║                                SELECT A CATEGORY                               ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  📂  1. FTP          (16 examples)                                             ║
║         File Transfer Protocol - read/write files, registers, diagnostics      ║
║                                                                                ║
║  🌐  2. CGTP         (24 examples)                                             ║
║         CGTP Web Server - programs, variables, registers, I/O, kinematics      ║
║                                                                                ║
║  🦾  3. KINEMATICS   (1 example)                                               ║
║         Kinematics - offline forward & inverse kinematics, no connection needed║
║                                                                                ║
║  🔑  3. LICENSE      (1 example)                                               ║
║         License management - activation & status                               ║
║                                                                                ║
║  ⚡  4. SNPX         (19 examples)                                             ║
║         SNPX industrial protocol - fast real-time register & I/O access        ║
║                                                                                ║
║  🔌  5. TELNET       (7 examples)                                              ║
║         Telnet KCL - send commands, read variables, control I/O                ║
║                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  0. Exit                                                                       ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

  Enter category number [0-6]:
```

---

### 📋 Complete Example List

#### 📂 FTP - File Transfer & Variable Access

| #   | Example                                                                                                                             | Description                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1   | [ftp_check_file_exists.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_check_file_exists.py)             | Check if a file or directory exists on the robot controller                           |
| 2   | [ftp_current_position.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_current_position.py)               | Read the current robot position (joints + Cartesian) for all motion groups            |
| 3   | [ftp_download_file.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_download_file.py)                     | Download a file from the robot controller to your local machine                       |
| 4   | [ftp_error_list.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_error_list.py)                           | Retrieve the complete error/alarm history with codes, timestamps, and active status   |
| 5   | [ftp_get_all_variables.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_get_all_variables.py)             | Interactive navigator to browse all variable files, search, and drill into structures |
| 6   | [ftp_io_state.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_io_state.py)                               | Read all digital I/O states (DIN, DOUT, RI, RO, UI, UO, SI, SO, FLG)                  |
| 7   | [ftp_list_files.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_list_files.py)                           | Browse files and directories on the controller's file system                          |
| 8   | [ftp_program_states.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_program_states.py)                   | Read the state of all running tasks/programs with call history                        |
| 9   | [ftp_read_features.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_read_features.py)                     | List all installed software features/options on the controller                        |
| 10  | [ftp_read_numeric_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_read_numeric_registers.py)   | Read numeric registers (R[1], R[2], ...) from the NUMREG variable file                |
| 11  | [ftp_read_position_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_read_position_registers.py) | Read position registers (PR[1], PR[2], ...) with Cartesian and joint data             |
| 12  | [ftp_read_string_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_read_string_registers.py)     | Read string registers (SR[1], SR[2], ...) from the STRREG variable file               |
| 13  | [ftp_read_system_variables.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_read_system_variables.py)     | Read commonly used system variables (robot name, hostname, language, etc.)            |
| 14  | [ftp_safety_status.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_safety_status.py)                     | Read safety signals: E-Stop, deadman, fence open, TP enable, and more                 |
| 15  | [ftp_summary_diagnostic.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_summary_diagnostic.py)           | Get a complete diagnostic snapshot: position, safety, I/O, features, programs         |
| 16  | [ftp_upload_file.py](https://github.com/underautomation/fanuc.py/blob/main/examples/ftp/ftp_upload_file.py)                         | Upload a local file to the robot controller                                           |

#### 🌐 CGTP - Web Server Protocol

| #   | Example                                                                                                                              | Description                                                                               |
| --- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 1   | [cgtp_batch_read.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_batch_read.py)                         | Read multiple variables (numeric, string, position registers) in a single batch operation |
| 2   | [cgtp_batch_write.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_batch_write.py)                       | Write multiple variables to the controller in a single batch operation                    |
| 3   | [cgtp_change_active_program.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_change_active_program.py)   | Change the active TP program on the controller                                            |
| 4   | [cgtp_create_delete_program.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_create_delete_program.py)   | Create a new TP program and optionally delete it                                          |
| 5   | [cgtp_http_files.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_http_files.py)                         | List variable files, TP programs, diagnostic files via HTTP and download as string        |
| 6   | [cgtp_kinematics.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_kinematics.py)                         | Compute forward and inverse kinematics on the controller via CGTP                         |
| 7   | [cgtp_list_read_files.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_list_read_files.py)               | List files on the controller and read file content as string                              |
| 8   | [cgtp_pause_abort.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_pause_abort.py)                       | Pause all running programs and abort a specific task                                      |
| 9   | [cgtp_program_properties.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_program_properties.py)         | Read and write program properties: comment, owner, stack size, ignore pause, etc.         |
| 10  | [cgtp_read_current_position.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_current_position.py)   | Read the current Cartesian and joint position of the robot                                |
| 11  | [cgtp_read_io_comments.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_io_comments.py)             | Read input and output comments for Robot, Digital, Group, or Analog I/O                   |
| 12  | [cgtp_read_numeric_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_numeric_registers.py) | Read all numeric registers (R[]) with comments, or a single register                      |
| 13  | [cgtp_read_position_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_position_register.py) | Read a position register PR[index] with comment and position data                         |
| 14  | [cgtp_read_set_comments.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_set_comments.py)           | Read all comments for registers or I/O and set a comment                                  |
| 15  | [cgtp_read_string_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_string_registers.py)   | Read all string registers (SR[]) with comments and values                                 |
| 16  | [cgtp_read_variable.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_variable.py)                   | Read a system or program variable as string or typed value                                |
| 17  | [cgtp_read_write_io.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_read_write_io.py)                   | Read and write I/O ports (DI, DO, RI, RO, GI, GO, AI, AO, Flag)                           |
| 18  | [cgtp_rename_program.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_rename_program.py)                 | Rename a TP program on the controller                                                     |
| 19  | [cgtp_select_run_program.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_select_run_program.py)         | Select a TP program and run it from a given line                                          |
| 20  | [cgtp_simulate_io.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_simulate_io.py)                       | Simulate, unsimulate, and check simulation status of I/O ports                            |
| 21  | [cgtp_user_alarms.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_user_alarms.py)                       | Read user alarm definitions and set alarm severity                                        |
| 22  | [cgtp_write_numeric_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_write_numeric_register.py) | Write an integer or real value to a numeric register R[index]                             |
| 23  | [cgtp_write_string_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_write_string_register.py)   | Write a string value to string register SR[index]                                         |
| 24  | [cgtp_write_variable.py](https://github.com/underautomation/fanuc.py/blob/main/examples/cgtp/cgtp_write_variable.py)                 | Write a numeric value to a system or program variable                                     |

#### ⚡ SNPX - High-Speed Industrial Protocol

| #   | Example                                                                                                                                | Description                                                           |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1   | [snpx_clear_alarms.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_clear_alarms.py)                       | Clear all active alarms on the robot                                  |
| 2   | [snpx_read_alarm_history.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_alarm_history.py)           | Read the alarm history with severity and cause information            |
| 3   | [snpx_read_alarms.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_alarms.py)                         | Read currently active alarms with ID, severity, message, and cause    |
| 4   | [snpx_read_batch_flags.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_batch_flags.py)               | Read multiple flags at once using batch assignment (much faster)      |
| 5   | [snpx_read_batch_registers.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_batch_registers.py)       | Read a batch of numeric registers at once for high performance        |
| 6   | [snpx_read_current_position.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_current_position.py)     | Read real-time Cartesian and joint position via SNPX                  |
| 7   | [snpx_read_digital_io.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_digital_io.py)                 | Read digital I/O signals (SDI, SDO, RDI, RDO, UI, UO, SI, SO, WI, WO) |
| 8   | [snpx_read_flag.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_flag.py)                             | Read a single boolean flag (FLG[i])                                   |
| 9   | [snpx_read_integer_sysvar.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_integer_sysvar.py)         | Read integer system variables by name (e.g. `$MCR.$GENOVERRIDE`)      |
| 10  | [snpx_read_numeric_io.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_numeric_io.py)                 | Read numeric/analog I/O values (GI, GO, AI, AO)                       |
| 11  | [snpx_read_numeric_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_numeric_register.py)     | Read a single numeric register (R[i]) with fast direct access         |
| 12  | [snpx_read_position_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_position_register.py)   | Read a position register (PR[i]) with Cartesian and joint data        |
| 13  | [snpx_read_string_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_read_string_register.py)       | Read a string register (SR[i])                                        |
| 14  | [snpx_write_digital_output.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_digital_output.py)       | Write digital output signals (SDO, RDO, UO, SO, WO)                   |
| 15  | [snpx_write_flag.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_flag.py)                           | Write a boolean flag (FLG[i]) with read-back confirmation             |
| 16  | [snpx_write_numeric_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_numeric_register.py)   | Write a numeric register (R[i]) with read-back confirmation           |
| 17  | [snpx_write_position_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_position_register.py) | Write a position register (PR[i]) in Cartesian or Joint mode          |
| 18  | [snpx_write_string_register.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_string_register.py)     | Write a string register (SR[i]) with read-back confirmation           |
| 19  | [snpx_write_sysvar.py](https://github.com/underautomation/fanuc.py/blob/main/examples/snpx/snpx_write_sysvar.py)                       | Write a system variable (e.g. speed override) via `set_variable`      |

#### 🔌 Telnet - KCL Remote Control

| #   | Example                                                                                                                      | Description                                                       |
| --- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 1   | [telnet_get_position.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_get_position.py)       | Read the current Cartesian position (X, Y, Z, W, P, R)            |
| 2   | [telnet_read_variable.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_read_variable.py)     | Read any robot variable by name (e.g. `$MCR.$GENOVERRIDE`)        |
| 3   | [telnet_set_port.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_set_port.py)               | Set a digital output port (DOUT, RDO, OPOUT, TPOUT, GOUT)         |
| 4   | [telnet_simulate_port.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_simulate_port.py)     | Simulate/unsimulate I/O ports for testing without real hardware   |
| 5   | [telnet_task_info.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_task_info.py)             | Get task information: status, current line, routine, program type |
| 6   | [telnet_write_variable.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_write_variable.py)   | Write a numeric value to any robot variable                       |
| 7   | [telnet_program_control.py](https://github.com/underautomation/fanuc.py/blob/main/examples/telnet/telnet_program_control.py) | Program lifecycle control: run, pause, resume, task info, abort   |

#### 🦾 Kinematics - Offline FK & IK (no robot connection needed)

| #   | Example                                                                                                                                  | Description                                                                                                    |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1   | [kinematics_forward_inverse.py](https://github.com/underautomation/fanuc.py/blob/main/examples/kinematics/kinematics_forward_inverse.py) | Interactive forward & inverse kinematics: select a model, view DH parameters, compute FK then all IK solutions |

#### 🔑 License

| #   | Example                                                                                                                   | Description                                                                |
| --- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | [license_info_example.py](https://github.com/underautomation/fanuc.py/blob/main/examples/license/license_info_example.py) | Display license state, register a license, and view all license properties |

---

## 📌 Feature Documentation

### 🌐 CGTP - Web Server Protocol

CGTP (Controller Gateway Transfer Protocol) communicates with the robot controller's **built-in web server** via HTTP. It provides a comprehensive API for program management, variable access, register operations, I/O control, and kinematics — all through a single protocol.

**What you can do:**

- **Full program lifecycle** - create, delete, rename, select, run, pause, and abort TP programs
- **Read and write program properties** - comment, owner, stack size, ignore pause, write protect, sub-type
- **Read/write system and program variables** with type information
- **Read/write numeric registers** (R[]) as integer or real, with comments
- **Read/write string registers** (SR[]) with comments
- **Read position registers** (PR[]) with Cartesian and joint data
- **Read/write I/O ports** - DI, DO, RI, RO, GI, GO, AI, AO, Flag
- **Simulate and unsimulate I/O** for testing without physical devices
- **Read current Cartesian and joint position** of the robot
- **Forward and inverse kinematics** computed on the controller
- **Batch read/write** multiple variables in a single operation for maximum efficiency
- **Read and set comments** for registers, I/O ports, and user alarms
- **Read user alarm** definitions and set severity
- **List and read files** from the controller's file system
- **HTTP file access** - list and download variable files, TP programs, diagnostic files

**Quick example:**

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.cgtp.cgtp_io_port_type import CgtpIoPortType
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_variables import CgtpBatchVariables

robot = FanucRobot()
params = ConnectionParameters("192.168.0.1")
params.cgtp.enable = True
params.cgtp.login = ""       # HTTP Basic auth (optional)
params.cgtp.password = ""
robot.connect(params)

# Read/write variables
value = robot.cgtp.read_variable_as_string("$MCR.$GENOVERRIDE")
robot.cgtp.write_variable("$MCR.$GENOVERRIDE", 50)

# Read a numeric register
reg = robot.cgtp.read_numeric_register_with_comment(1)
print(f"R[1] = {reg}")

# Write registers
robot.cgtp.write_numeric_register_as_integer(1, 42)
robot.cgtp.write_string_register(1, "Hello CGTP")

# Program control
robot.cgtp.select_program("MAIN", 1)
robot.cgtp.run_program("MAIN")
robot.cgtp.pause_all_programs()
robot.cgtp.abort_task("MAIN")

# I/O
value = robot.cgtp.read_io(CgtpIoPortType.DO, 1)
robot.cgtp.write_io(CgtpIoPortType.DO, 1, 1)
robot.cgtp.simulate_io(CgtpIoPortType.DI, 3)

# Current position
cart = robot.cgtp.read_cartesian_position(1)
print(f"X={cart.x:.3f}, Y={cart.y:.3f}, Z={cart.z:.3f}")

# Batch operations (read multiple variables in one call)
batch = CgtpBatchVariables()
batch.add_numeric_register(1)
batch.add_numeric_register(2)
batch.add_string_register(1)
batch.add_variable("$MCR.$GENOVERRIDE")
robot.cgtp.read_batch_variables(batch)
for var in batch:
    print(f"{var.name} = {var.string_value}")

robot.disconnect()
```

---

### 🖥️ Telnet KCL - Remote Command Interface

Telnet KCL (Karel Command Language) lets you remotely send commands to the robot controller. It's the simplest way to control programs, read/write variables, and manage I/O.

**What you can do:**

- **Run, pause, hold, continue, and abort programs** remotely
- **Read and write any robot variable** (`$MCR.$GENOVERRIDE`, `$RMT_MASTER`, custom variables, etc.)
- **Set digital output ports** (DOUT, RDO, OPOUT, TPOUT, GOUT)
- **Simulate and unsimulate I/O ports** for testing without physical devices
- **Get task information** - which programs are running, their status, and current line
- **Read the current Cartesian position** of the robot

**Quick example:**

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.telnet.kcl_ports import KCLPorts

robot = FanucRobot()
params = ConnectionParameters("192.168.0.1")
params.telnet.enable = True
robot.connect(params)

# Read a variable
result = robot.telnet.get_variable("$MCR.$GENOVERRIDE")
print(f"Speed override: {result.raw_value}%")

# Write a variable
robot.telnet.set_variable("$MCR.$GENOVERRIDE", 50)

# Control programs
robot.telnet.run("MyProgram")
robot.telnet.pause("MyProgram")
robot.telnet.abort("MyProgram", force=True)

# Set a digital output
robot.telnet.set_port(KCLPorts.DOUT, 1, 1)  # DOUT[1] = ON

# Simulate an input for testing
robot.telnet.simulate(KCLPorts.DIN, 3, 1)   # DIN[3] simulated to ON
robot.telnet.unsimulate(KCLPorts.DIN, 3)     # Restore normal operation

# Get task info
info = robot.telnet.get_task_information("MAINPROG")
print(f"Status: {info.task_status_str}, Line: {info.current_line}")

# Read current position
pose = robot.telnet.get_current_pose()
print(f"X={pose.position.x}, Y={pose.position.y}, Z={pose.position.z}")

robot.disconnect()
```

---

### ⚡ SNPX (RobotIF) - High-Speed Industrial Protocol

SNPX provides **fast, structured data exchange** with the robot. It's the best choice for real-time monitoring and high-frequency register access. It supports batch reads for maximum throughput.

**What you can do:**

- **Read/write numeric registers** (R[1], R[2], ...) - single or batch
- **Read/write string registers** (SR[1], SR[2], ...)
- **Read/write position registers** (PR[1], PR[2], ...) with Cartesian and joint data
- **Read/write boolean flags** (FLG[1], FLG[2], ...) - single or batch
- **Read/write digital I/O** - SDI, SDO, RDI, RDO, UI, UO, SI, SO, WI, WO
- **Read/write numeric I/O** - GI, GO, AI, AO (group and analog signals)
- **Read/write system variables** (e.g. speed override)
- **Read the current robot position** in real-time (world and joint coordinates)
- **Read active alarms** and **alarm history** with severity and cause
- **Clear alarms** remotely

**Quick example:**

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters

robot = FanucRobot()
params = ConnectionParameters("192.168.0.1")
params.snpx.enable = True
robot.connect(params)

# Read a numeric register
value = robot.snpx.numeric_registers.read(1)
print(f"R[1] = {value}")

# Write a numeric register
robot.snpx.numeric_registers.write(1, 42.5)

# Batch read for maximum speed
batch = robot.snpx.numeric_registers.create_batch_assignment(1, 10)
values = batch.read()  # Reads R[1] through R[10] in one call

# Read/write string registers
text = robot.snpx.string_registers.read(1)
robot.snpx.string_registers.write(1, "Hello Fanuc")

# Read a position register
position = robot.snpx.position_registers.read(1)
print(f"PR[1]: X={position.cartesian_position.x}, Y={position.cartesian_position.y}")

# Digital I/O
sdi_values = robot.snpx.sdi.read(1, 8)     # Read SDI[1..8]
robot.snpx.sdo.write(1, [True, False])      # Write SDO[1]=ON, SDO[2]=OFF

# Current position
pos = robot.snpx.current_position.read_world_position(1)
print(f"X={pos.cartesian_position.x}, Y={pos.cartesian_position.y}")

# Alarms
robot.snpx.clear_alarms()

# System variables
speed = robot.snpx.integer_system_variables.read("$MCR.$GENOVERRIDE")
robot.snpx.set_variable("$MCR.$GENOVERRIDE", "50")

robot.disconnect()
```

---

### 📐 Kinematics - Offline Forward & Inverse Kinematics

The kinematics module lets you compute **forward kinematics** (joint angles → Cartesian position) and **inverse kinematics** (Cartesian position → all joint angle solutions) **entirely offline** — no robot connection or license required.

It includes built-in Denavit-Hartenberg parameters for **80+ FANUC robot models** (CRX collaborative and standard OPW arms).

**What you can do:**

- **List all supported robot models** and their DH parameters
- **Forward kinematics** - compute the TCP Cartesian pose from 6 joint angles
- **Inverse kinematics** - compute **all** valid joint configurations for a given Cartesian pose
- **No connection needed** - works fully offline, no robot or license required
- **Supports CRX and standard (OPW) kinematics categories**

**Quick example:**

```python
import math
from underautomation.fanuc.kinematics.arm_kinematic_models import ArmKinematicModels
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from underautomation.fanuc.kinematics.kinematics_utils import KinematicsUtils
from underautomation.fanuc.common.cartesian_position import CartesianPosition

# Get DH parameters for a specific robot model
dh = DhParameters.from_arm_kinematic_model(ArmKinematicModels.CRX10iA)
print(f"a1={dh.a1}, a2={dh.a2}, a3={dh.a3}, d4={dh.d4}, d5={dh.d5}, d6={dh.d6}")

# Forward kinematics: joint angles (radians) → Cartesian position
joints_rad = [math.radians(j) for j in [0, -30, 45, 0, 60, 0]]
fk = KinematicsUtils.forward_kinematics(joints_rad, dh)
print(f"FK → X={fk.x:.2f}, Y={fk.y:.2f}, Z={fk.z:.2f}, W={fk.w:.2f}, P={fk.p:.2f}, R={fk.r:.2f}")

# Inverse kinematics: Cartesian position → all joint solutions
target = CartesianPosition(fk.x, fk.y, fk.z, fk.w, fk.p, fk.r, None)
solutions = KinematicsUtils.inverse_kinematics(target, dh)
for i, sol in enumerate(solutions, 1):
    print(f"  IK #{i}: J1={sol.j1:.2f}, J2={sol.j2:.2f}, J3={sol.j3:.2f}, "
          f"J4={sol.j4:.2f}, J5={sol.j5:.2f}, J6={sol.j6:.2f}")
```

**TRY IT:**

To test IK and FK, you can run the complete example : [kinematics_forward_inverse.py](https://github.com/underautomation/fanuc.py/blob/main/examples/kinematics/kinematics_forward_inverse.py)

```bash
python .\examples\kinematics\kinematics_forward_inverse.py
```

And get this kind of output (with interactive model selection and joint input):

```
(.venv) PS Fanuc.py> python .\examples\kinematics\kinematics_forward_inverse.py
============================================================
  FANUC SDK - Forward & Inverse Kinematics (offline)
============================================================

Available robot models (82):

    1. ARCMate0iA               2. ARCMate0iB               3. ARCMate0iB_2
    4. ARCMate100iD             5. ARCMate100iD10L          6. ARCMate100iD16S
    7. ARCMate100iD8L           8. ARCMate120iD             9. ARCMate120iD12L
   10. ARCMate120iD35          11. CR14iAL                 12. CR15iA
   13. CR35iA                  14. CR7iA                   15. CR7iAL
   16. CRX10iA                 17. CRX10iAL                18. LRMate200iD
   19. LRMate200iD7C           20. LRMate200iD7L           21. LRMate200iD7LC
   22. LaserRobotHA            23. M10iA10M                24. M10iA10MS
   25. M10iA12                 26. M10iA12S                27. M10iA7L
   28. M10iA8L                 29. M2000iA1200             30. M2000iA1700L
   31. M2000iA2300             32. M2000iA900L             33. M20iA
   34. M20iA12L                35. M20iA20M                36. M20iA35M
   37. M20iB25                 38. M20iB25C                39. M20iB35S
   40. M410iC110               41. M410iC185               42. M410iC185_2
   43. M410iC500               44. M410iC500_2             45. M710iC12L
   46. M710iC20M               47. M710iC45M               48. M710iC50
   49. M800iA60                50. M900iB280L              51. M900iB330L
   52. M900iB360               53. M900iB400L              54. M900iB700
   55. M900iBKAI               56. P350iA45LeftHand        57. P350iA45RightHand
   58. P700iANewRightyArmRightOffset   59. R1000iA100F             60. R1000iA100F7
   61. R1000iA120F7B           62. R1000iA120F7BS          63. R1000iA120F7BS_2
   64. R1000iA120F7BS_3        65. R1000iA120F7B_2         66. R1000iA120F7B_3
   67. R1000iA130F             68. R1000iA80F              69. R2000iB125L
   70. R2000iB175L             71. R2000iB210FS            72. R2000iB220US
   73. R2000iC100S             74. R2000iC125L             75. R2000iC190U
   76. R2000iC210F             77. R2000iC210L             78. R2000iC210WE
   79. R2000iC210WEProto       80. R2000iC220U             81. R2000iC270F
   82. R2000iD100FH

Select a model number [1-82] (default 1): 16

→ Selected model: CRX10iA

Denavit-Hartenberg parameters for CRX10iA:
----------------------------------------
  a1 =     0.0000 mm
  a2 =   540.0000 mm
  a3 =     0.0000 mm
  d4 =  -540.0000 mm
  d5 =   150.0000 mm
  d6 =  -160.0000 mm
  Category: Crx

Enter joint angles in degrees (press Enter for 0):
  J1 (0.0000): 10
  J2 (0.0000): 20
  J3 (0.0000): 40
  J4 (0.0000): 10
  J5 (0.0000): -10
  J6 (0.0000):

Computing forward kinematics for J=[10.00, 20.00, 40.00, 10.00, -10.00, 0.00] deg ...

FK result — Cartesian position:
----------------------------------------
  X =     735.4571 mm
  Y =     -25.2181 mm
  Z =     954.8160 mm
  W =      14.8408 deg
  P =     -58.7116 deg
  R =     170.7749 deg
  Conf = N U T, 0, 0, 0

Enter cartesian position for IK (press Enter to keep FK value):
  X [mm] (735.4571):
  Y [mm] (-25.2181):
  Z [mm] (954.8160):
  W [deg] (14.8408):
  P [deg] (-58.7116):
  R [deg] (170.7749):

Computing inverse kinematics for X=735.4571, Y=-25.2181, Z=954.8160, W=14.8408, P=-58.7116, R=170.7749 ...

8 IK solution(s) found:
----------------------------------------------------------------------------------------------------
  #            J1         J2         J3         J4         J5         J6   Configuration
----------------------------------------------------------------------------------------------------
  1      -15.6154    48.3697    60.5986   142.0264    34.2715  -150.7098   F D T, 0, 0, 0
  2       10.2040    47.1644    69.1161     3.0266   -39.0031     7.6007   N D T, 0, 0, 0
  3        3.2969    19.0319    27.7002    58.2991     4.7830   -51.7280   F U T, 0, 0, 0
  4       10.0000    20.0000    40.0000    10.0000   -10.0000     0.0000   N U T, 0, 0, 0
  5      164.3846   -48.3697   119.4014   -37.9736    34.2715  -150.7098   F U B, 0, 0, 0
  6     -169.7960   -47.1644   110.8839  -176.9734   -39.0031     7.6007   N U B, 0, 0, 0
  7     -176.7031   -19.0319   152.2998  -121.7009     4.7830   -51.7280   F D B, 0, 0, 0
  8     -170.0000   -20.0000   140.0000  -170.0000   -10.0000     0.0000   N D B, 0, 0, 0
----------------------------------------------------------------------------------------------------

Done.
```

---

### 📂 FTP - File Transfer & Variable Management

FTP gives you access to the robot's **file system** and **internal variable files**. It's ideal for bulk data access, diagnostics, backups, and program management.

It not only allows you to upload/download files but also provides **structured** and **parsed** access to system files, variables files, and more. You can even get a complete diagnostic snapshot in one call.

**What you can do:**

- **Upload and download files** to/from the controller
- **Browse the controller's file system** - list files, check existence
- **Read all variable files at once** - navigate through an interactive explorer
- **Read numeric, string, and position registers** from variable files
- **Read system variables** (robot name, hostname, language, timers)
- **Get the complete error/alarm history** with codes and timestamps
- **Read all I/O states** (DIN, DOUT, RI, RO, UI, UO, SI, SO, FLG)
- **Get safety status** - E-Stop, deadman, fence open, TP enable
- **Get program/task states** - which programs are running and their call stacks
- **Read installed features/options** on the controller
- **Get a full summary diagnostic** - position, safety, I/O, features, programs in one call

**Quick example:**

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters

robot = FanucRobot()
params = ConnectionParameters("192.168.0.1")
params.ftp.enable = True
robot.connect(params)

# File operations
robot.ftp.direct_file_handling.upload_file_to_controller("local.tp", "/md:/remote.tp")
robot.ftp.direct_file_handling.download_file_from_controller("backup.va", "/md:/backup.va")
exists = robot.ftp.direct_file_handling.file_exists("/md:/summary.dg")

# Read registers from variable files
numreg = robot.ftp.known_variable_files.get_numreg_file()
for idx, val in enumerate(numreg.numreg, start=1):
    print(f"R[{idx}] = {val}")

posreg = robot.ftp.known_variable_files.get_posreg_file()
strreg = robot.ftp.known_variable_files.get_strreg_file()

# System variables
system = robot.ftp.known_variable_files.get_system_file()
print(f"Robot: {system.robot_name}, Host: {system.hostname}")

# Current position (all groups, all frames)
position = robot.ftp.get_current_position()
for gp in position.groups_position:
    print(f"J1={gp.joints_position.j1}, J2={gp.joints_position.j2}")

# Safety status
safety = robot.ftp.get_safety_status()
print(f"E-Stop: {safety.external_e_stop}, TP Enable: {safety.tp_enable}")

# Error history
errors = robot.ftp.get_all_errors_list()
for err in errors.filter_active_alarms():
    print(f"[{err.error_code}] {err.message}")

# I/O states (all ports at once)
io = robot.ftp.get_io_state()
for signal in io.states:
    print(f"{signal.port}[{signal.id}] = {'ON' if signal.value else 'OFF'}")

# Complete diagnostic in one call
diag = robot.ftp.get_summary_diagnostic()

robot.disconnect()
```

---

## 🔧 Robot Configuration

Some features require enabling protocols on the controller.

### ✅ Enable Telnet KCL

Read full tutorial: [underautomation.com/fanuc/documentation/enable-telnet](https://underautomation.com/fanuc/documentation/enable-telnet)

1. Go to **SETUP > Host Comm**
2. Select **TELNET** → **[DETAIL]**
3. Set a password and reboot

### ✅ Enable FTP

1. Go to **SETUP > Host Comm > FTP**
2. Set username/password
3. Perform a cold start

### ✅ Enable SNPX

- For **FANUC America (R650 FRA)**: Enable option R553 "HMI Device SNPX"
- For **FANUC Ltd. (R651 FRL)**: No additional options required

---

## 🔍 Compatibility

|                       | Supported                                   |
| --------------------- | ------------------------------------------- |
| **Robot Controllers** | R-J3iB, R-30iA, R-30iB, R-30iB+, R-50iA     |
| **OS**                | Windows, Linux, macOS                       |
| **Python**            | 3.7+                                        |
| **Dependency**        | `pythonnet 3.0.5` (installed automatically) |

---

## 📢 Contributing

We welcome your feedback and contributions!

- Report issues via [GitHub Issues](https://github.com/underautomation/Fanuc.py/issues)
- Submit pull requests with enhancements
- Suggest features and improvements

---

## 📜 License

**⚠️ This SDK requires a commercial license.**

- 🆓 **30-day free trial** included out of the box
- 🔄 **Get a new trial immediately** at [underautomation.com/license](https://underautomation.com/license?sdk=fanuc)
- 🛒 **Buy a license** at [underautomation.com/fanuc](https://underautomation.com/fanuc)
- 📄 **EULA**: [underautomation.com/fanuc/eula](https://underautomation.com/fanuc/eula)

---

## 📬 Need Help?

- 📖 **Documentation**: [underautomation.com/fanuc/documentation](https://underautomation.com/fanuc/documentation)
- 🐍 **Python Get Started Guide**: [underautomation.com/fanuc/documentation/get-started-python](https://underautomation.com/fanuc/documentation/get-started-python)
- 📦 **PyPI Package**: [pypi.org/project/UnderAutomation.Fanuc](https://pypi.org/project/UnderAutomation.Fanuc/)
- 📩 **Contact Us**: [underautomation.com/contact](https://underautomation.com/contact)
