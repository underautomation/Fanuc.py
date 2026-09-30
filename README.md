# Fanuc Robot Communication SDK for Python

[![UnderAutomation Fanuc communication SDK](https://raw.githubusercontent.com/underautomation/Fanuc.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com/fanuc)

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.Fanuc?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.Fanuc/)
[![PyPI downloads](https://img.shields.io/pypi/dm/UnderAutomation.Fanuc?label=Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.Fanuc/)
[![Python](https://img.shields.io/badge/Python-3.7_to_3.13-blue)](#compatibility)
[![Platforms](https://img.shields.io/badge/OS-Windows_Linux_macOS-informational)](#compatibility)
[![License](https://img.shields.io/badge/license-commercial-blue)](https://underautomation.com/fanuc/eula)

**UnderAutomation.Fanuc** is a Python package that communicates with Fanuc robot controllers (R-J3iB,
R-30iA, R-30iB, R-50iA) and with **ROBOGUIDE**. Nothing is installed on the robot. No PCDK and no Robot
Interface are needed on the PC.

Use it to read and write variables, registers and I/O, run and stop programs, read and reset alarms,
transfer files, read the state of the robot and move it, from a Python script. It also computes the
kinematics and plans trajectories offline.

- Product page: [underautomation.com/fanuc](https://underautomation.com/fanuc)
- Documentation: [underautomation.com/fanuc/documentation/get-started-python](https://underautomation.com/fanuc/documentation/get-started-python)
- Also available for .NET: [Fanuc.NET](https://github.com/underautomation/Fanuc.NET), and for LabVIEW: [Fanuc.vi](https://github.com/underautomation/Fanuc.vi)

## What you can do

| Feature | Protocol | Controller option |
| --- | --- | --- |
| Run, pause, hold, abort programs, read and write variables, set and simulate ports | Telnet KCL | none |
| Upload and download files, read variable files, registers, I/O, alarms, safety status, diagnostics | FTP | none |
| Fast read and write of registers, I/O, flags, system variables, current position, alarms | SNPX | R553 "HMI Device SNPX" on FANUC America controllers (R650 FRA), none on FANUC Ltd. controllers (R651 FRL) |
| Programs, source lines, variables, registers, I/O, comments, kinematics on the controller | CGTP (web server of the controller) | none |
| Motion instructions sent from the PC, with a status per instruction | RMI | R912 |
| Real-time motion at every communication cycle: trajectories, target tracking, I/O | Stream Motion | J519 |
| Forward and inverse kinematics, 82 arm models | offline | none |
| Motion planner: J, L, C motions, FINE, CNT, CR, splines, shapes, jerk limits | offline | none |

## How it works

The package wraps the .NET library `UnderAutomation.Fanuc.dll` with [pythonnet](https://github.com/pythonnet/pythonnet).
The DLL is inside the package: `pip install` installs everything, including pythonnet.

- **Windows:** the DLL runs on the .NET Framework 4.x of Windows. Nothing else to install.
- **Linux and macOS:** install the .NET runtime (for example .NET 8), then tell pythonnet to use it before
  you start Python:

  ```bash
  sudo apt-get install -y dotnet-runtime-8.0   # Ubuntu, for example
  export PYTHONNET_RUNTIME=coreclr
  ```

  Without this variable, pythonnet uses Mono, its default runtime on Linux and macOS. You can also choose
  the runtime in your code, before the first import of the package:

  ```python
  from pythonnet import load
  load("coreclr")
  ```

## Installation

Python 3.7 to 3.13 is supported (the limit of pythonnet 3.0.5). Install the package in a virtual
environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux and macOS
source .venv/bin/activate

pip install UnderAutomation.Fanuc
```

Or install it from the sources of this repository:

```bash
git clone https://github.com/underautomation/Fanuc.py.git
cd Fanuc.py
pip install -e .
```

## Getting started

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.common.languages import Languages

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# FanucRobot.register_license("Your Company", "your-license-key")

# IP address of the controller, or the folder of a ROBOGUIDE robot:
# ConnectionParameters(r"C:\Users\you\Documents\My Workcells\CRX 10iA L\Robot_1")
params = ConnectionParameters("192.168.0.1")
params.language = Languages.English  # Japanese and Chinese controllers are also supported

params.telnet.enable = True
params.telnet.telnet_kcl_password = "telnet_password"

params.ftp.enable = True
params.ftp.ftp_user = ""
params.ftp.ftp_password = ""

params.snpx.enable = True

robot = FanucRobot()
robot.connect(params)

if robot.snpx.connected:
    print(f"R[1] = {robot.snpx.numeric_registers.read(1)}")
    print(robot.snpx.current_position.read_world_position(1))

if robot.ftp.connected:
    safety = robot.ftp.get_safety_status()
    print(f"External E-Stop: {safety.external_e_stop}, TP enable: {safety.tp_enable}")

if robot.telnet.connected:
    speed_override = robot.telnet.get_variable("$MCR.$GENOVERRIDE")
    print(f"Speed override: {speed_override.raw_value}%")

robot.disconnect()
```

Enable only the protocols you use. Each protocol needs its own setup on the controller, see
[Robot configuration](#robot-configuration).

## From .NET names to Python names

The Python API is the .NET API with Python names. The [.NET documentation](https://underautomation.com/fanuc/documentation)
applies to Python.

| .NET | Python |
| --- | --- |
| Method `Snpx.NumericRegisters.Read(1)` | `snpx.numeric_registers.read(1)` |
| Property `Telnet.TelnetKclPassword` | `telnet.telnet_kcl_password` |
| Static method `FanucRobot.RegisterLicense(...)` | `FanucRobot.register_license(...)` |
| Enum value `CgtpIoPortType.DO` | `CgtpIoPortType.DO` (an `IntEnum`) |
| Array `JointsPosition[]` | list-like object, use `list(...)` to copy it |
| `Nullable<int>` | `int \| None` |

Each type is in the module named after it, in snake case:
`UnderAutomation.Fanuc.Common.JointsPosition` is `underautomation.fanuc.common.joints_position.JointsPosition`.
The motion planner, common to the UnderAutomation SDKs, is in `underautomation.robotics`.

## Features

### Telnet KCL

Telnet KCL (Karel Command Line) sends commands to the controller. It needs no option on the controller.

```python
from underautomation.fanuc.common.kcl.kcl_ports import KCLPorts

# Variables
result = robot.telnet.get_variable("$MCR.$GENOVERRIDE")
print(f"Speed override: {result.raw_value}%")
robot.telnet.set_variable("$MCR.$GENOVERRIDE", 50)

# Programs
robot.telnet.run("MyProgram")
robot.telnet.pause("MyProgram")
robot.telnet.abort("MyProgram", force=True)

info = robot.telnet.get_task_information("MAINPROG")
print(f"Status: {info.task_status_str}, Line: {info.current_line}")

# Ports: set DOUT[1], simulate DIN[3]
robot.telnet.set_port(KCLPorts.DOUT, 1, 1)
robot.telnet.simulate(KCLPorts.DIN, 3, 1)
robot.telnet.unsimulate(KCLPorts.DIN, 3)

# Current position
pose = robot.telnet.get_current_pose()
print(f"X={pose.position.x}, Y={pose.position.y}, Z={pose.position.z}")
```

### SNPX

SNPX (also known as SRTP or RobotIF) is the fastest way to read and write registers, I/O and variables.
Batch reads read several values in one request.

```python
# Numeric registers, one value or a batch (R[1] to R[10] in one request)
value = robot.snpx.numeric_registers.read(1)
robot.snpx.numeric_registers.write(1, 42.5)
batch = robot.snpx.numeric_registers.create_batch_assignment(1, 10)
values = batch.read()

# String and position registers
text = robot.snpx.string_registers.read(1)
robot.snpx.string_registers.write(1, "Hello Fanuc")
position = robot.snpx.position_registers.read(1)
print(f"PR[1]: X={position.cartesian_position.x}, Y={position.cartesian_position.y}")

# Digital I/O: read SDI[1] to SDI[8], write SDO[1] and SDO[2]
sdi_values = robot.snpx.sdi.read(1, 8)
robot.snpx.sdo.write(1, [True, False])

# Current position
pos = robot.snpx.current_position.read_world_position(1)

# Alarms and system variables
robot.snpx.clear_alarms()
speed = robot.snpx.integer_system_variables.read("$MCR.$GENOVERRIDE")
robot.snpx.set_variable("$MCR.$GENOVERRIDE", 50)
```

### FTP

FTP gives access to the files of the controller, and reads and decodes the variable files and the
diagnostic files.

```python
# Files
robot.ftp.direct_file_handling.upload_file_to_controller("local.tp", "/md:/remote.tp")
robot.ftp.direct_file_handling.download_file_from_controller("backup.va", "/md:/backup.va")
exists = robot.ftp.direct_file_handling.file_exists("/md:/summary.dg")

# Registers and system variables from the variable files
numreg = robot.ftp.known_variable_files.get_numreg_file()
for idx, val in enumerate(numreg.numreg, start=1):
    print(f"R[{idx}] = {val}")
system = robot.ftp.known_variable_files.get_system_file()
print(f"Robot: {system.robot_name}, Host: {system.hostname}")

# Current position of each motion group
for gp in robot.ftp.get_current_position().groups_position:
    print(f"J1={gp.joints_position.j1}, J2={gp.joints_position.j2}")

# Safety status, active alarms, I/O states, complete diagnostic
safety = robot.ftp.get_safety_status()
for err in robot.ftp.get_all_errors_list().filter_active_alarms():
    print(f"[{err.error_code}] {err.message}")
for signal in robot.ftp.get_io_state().states:
    print(f"{signal.port}[{signal.id}] = {'ON' if signal.value else 'OFF'}")
diag = robot.ftp.get_summary_diagnostic()
```

### CGTP (web server of the controller)

CGTP uses the web server of the controller. It gives access to the programs, the variables, the
registers, the I/O and the kinematics.

```python
from underautomation.fanuc.cgtp.cgtp_io_port_type import CgtpIoPortType
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_variables import CgtpBatchVariables
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition

params = ConnectionParameters("192.168.0.1")
params.cgtp.enable = True
params.cgtp.login = ""       # HTTP authentication, when the controller asks for it
params.cgtp.password = ""
robot.connect(params)

# Variables and registers
value = robot.cgtp.read_variable_as_string("$MCR.$GENOVERRIDE")
robot.cgtp.write_variable("$MCR.$GENOVERRIDE", 50)
reg = robot.cgtp.read_numeric_register_with_comment(1)
robot.cgtp.write_numeric_register_as_integer(1, 42)
robot.cgtp.write_string_register(1, "Hello CGTP")

# Programs
robot.cgtp.select_program("MAIN", 1)
robot.cgtp.run_program("MAIN")
robot.cgtp.pause_all_programs()
robot.cgtp.abort_task("MAIN")
for prog in robot.cgtp.list_tp_programs():
    print(prog)

# Source lines and positions of a TP program (firmware V9.10 or later, first motion group only)
robot.cgtp.insert_source_line("MY_PROGRAM", "L P[5] 100mm/sec FINE", 3)
robot.cgtp.replace_source_line("MY_PROGRAM", "J P[1] 50% FINE", 5)
robot.cgtp.delete_source_lines("MY_PROGRAM", 4, 2)
position = Position(0, 1, None, ExtendedCartesianPosition(500, 200, 300, 0, 90, 0, 0, 0, 0))
robot.cgtp.set_program_position("MY_PROG", 1, position)

# I/O
value = robot.cgtp.read_io(CgtpIoPortType.DO, 1)
robot.cgtp.write_io(CgtpIoPortType.DO, 1, 1)
robot.cgtp.simulate_io(CgtpIoPortType.DI, 3)

# Current position
cart = robot.cgtp.read_cartesian_position(1)
print(f"X={cart.x:.3f}, Y={cart.y:.3f}, Z={cart.z:.3f}")

# Several variables in one request
batch = CgtpBatchVariables()
batch.add_numeric_register(1)
batch.add_string_register(1)
batch.add_variable("$MCR.$GENOVERRIDE")
robot.cgtp.read_batch_variables(batch)
for var in batch:
    print(f"{var.name} = {var.string_value}")
```

### RMI (option R912)

RMI (Remote Motion Interface) sends TP motion instructions to the robot. The SDK manages the instruction
buffer of the controller and returns a response object for each instruction. The teach pendant must be
disabled and the controller in AUTO mode before `initialize()`.

```python
from underautomation.fanuc.rmi.tp_instructions.linear_motion_tp_instruction import LinearMotionTpInstruction
from underautomation.fanuc.rmi.tp_instructions.wait_time_tp_instruction import WaitTimeTpInstruction
from underautomation.fanuc.rmi.data.rmi_linear_speed_type import RmiLinearSpeedType
from underautomation.fanuc.rmi.data.rmi_termination_type import RmiTerminationType
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame

params = ConnectionParameters("192.168.0.1")
params.rmi.enable = True
robot.connect(params)

# Starts the RMI_MOVE program on the controller
robot.rmi.initialize()
robot.rmi.set_override(80)

# Linear motion to a Cartesian target (tool 1, frame 0)
instr = LinearMotionTpInstruction()
instr.speed_type = RmiLinearSpeedType.MmSec
instr.speed = 100
instr.term_type = RmiTerminationType.Fine
instr.target = CartesianPositionWithUserFrame(500, 200, 300, 0, 90, 0, 1, 0)
response = robot.rmi.send_tp_instruction(instr)
response.wait_for_completion()

# Wait 0.5 s
wait = WaitTimeTpInstruction()
wait.seconds = 0.5
robot.rmi.send_tp_instruction(wait)

# Stops the RMI_MOVE program
robot.rmi.abort()
```

### Stream Motion (option J519)

Stream Motion gives the position of the robot at every communication cycle (2 to 8 ms). The SDK does the
real-time part: it synchronizes the positions with the status of the robot, sends a few positions in
advance, and stops the robot smoothly when your script stops giving positions. The robot must run a TP
program with `IBGN start[1]` and `IBGN end[1]`, in AUTO mode at 100% override.

With Python, prefer the target tracking to the callback that computes each position: the timing of a
Python callback depends on the interpreter.

```python
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.robotics.motion.motion_planner import MotionPlanner
from underautomation.robotics.motion.position_format import PositionFormat

params = ConnectionParameters("192.168.0.1")
params.stream_motion.enable = True
params.stream_motion.protocol_version = 1  # 1, 2 or 3, not higher than $STMO.$USABLE_VER
robot.connect(params)
sm = robot.stream_motion

# Reads the limits of the robot, starts the status output and measures the communication cycle
sm.start_monitoring()
status = sm.last_status
print(f"J1={status.joint_position.j1:.3f} Moving={status.is_moving}")

# Reads DI[1] to DI[16] during the session
sm.add_io_monitor(IOType.DI, 1)

# J1 +10 degrees then back, at 20% of the velocity limits
start = sm.queue_end_joint_position
values = list(start.values)
values[0] += 10
target = JointsPosition(*values)
planner = MotionPlanner(sm.joint_limits, None)
trajectory = planner.create_joint_path(FanucMotion.to_joint_values(start)) \
    .move_joint(FanucMotion.to_joint_values(target), 20, FanucMotion.cnt(100)) \
    .move_joint(FanucMotion.to_joint_values(start), 20, FanucMotion.fine()) \
    .build()

# The motion starts when the TP program reaches IBGN start
motion_id = sm.enqueue(trajectory)
sm.wait_for_motion(motion_id, 60000)
sm.wait_for_idle(10000)

# Follow a target that can change at any time, at 30% of the velocity limits
sm.start_tracking(PositionFormat.Joint, 30)
sm.set_joint_tracking_target(target)
sm.wait_for_idle(10000)
sm.stop_tracking()

# Releases the TP program: it continues after IBGN end
sm.finish(10000)
robot.disconnect()
```

Documentation: [Stream Motion](https://underautomation.com/fanuc/documentation/stream-motion).

### Kinematics

The SDK computes the forward and inverse kinematics offline, with no connection and no license. It
contains the Denavit-Hartenberg parameters of 82 arm models (CRX cobots and OPW arms).

```python
import math
from underautomation.fanuc.kinematics.arm_kinematic_models import ArmKinematicModels
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from underautomation.fanuc.kinematics.kinematics_utils import KinematicsUtils
from underautomation.fanuc.common.cartesian_position import CartesianPosition

dh = DhParameters.from_arm_kinematic_model(ArmKinematicModels.CRX10iA)

# Forward kinematics: joint angles in radians to Cartesian position
joints_rad = [math.radians(j) for j in [0, -30, 45, 0, 60, 0]]
fk = KinematicsUtils.forward_kinematics(joints_rad, dh)
print(f"X={fk.x:.2f}, Y={fk.y:.2f}, Z={fk.z:.2f}, W={fk.w:.2f}, P={fk.p:.2f}, R={fk.r:.2f}")

# Inverse kinematics: every joint solution of a Cartesian position
target = CartesianPosition(fk.x, fk.y, fk.z, fk.w, fk.p, fk.r, None)
for i, sol in enumerate(KinematicsUtils.inverse_kinematics(target, dh), 1):
    print(f"IK #{i}: J1={sol.j1:.2f}, J2={sol.j2:.2f}, J3={sol.j3:.2f}, J4={sol.j4:.2f}, J5={sol.j5:.2f}, J6={sol.j6:.2f}")
```

The example [kinematics_forward_inverse.py](examples/kinematics/kinematics_forward_inverse.py) lets you
choose a model, type the joints, and prints the forward kinematics and the 8 solutions of the inverse
kinematics with their configuration.

### Motion planner

The motion planner creates trajectories offline, within velocity, acceleration and jerk limits. Motions
are described as in a TP program: J, L and C motions with FINE, CNT or CR termination. A trajectory can be
sent with Stream Motion, sampled for a simulation, or checked against the limits of the robot.

The planner is in the `underautomation.robotics` modules, common to the UnderAutomation robot SDKs.
`FanucMotion` (`underautomation.fanuc.motion.fanuc_motion`) converts the Fanuc positions and gives the
FINE, CNT and CR terminations and the I/O signals.

```python
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.robotics.motion.motion_planner import MotionPlanner

# Limits of each axis: read them with robot.stream_motion.read_limits().reference_limits
joint_limits = JointLimits(
    [120, 120, 180, 180, 180, 180],         # velocity, deg/s
    [300, 300, 450, 675, 675, 675],         # acceleration, deg/s2
    [1125, 1125, 1687, 2530, 1265, 2530])   # jerk, deg/s3
cartesian_limits = CartesianLimits(500, 2000, 10000, 90, 360, 1800)
planner = MotionPlanner(joint_limits, cartesian_limits)

# J P[1] 50% CNT100, J P[2] 50% FINE
home = JointValues([0, 0, 0, 0, -90, 0])
pick = JointValues([30, 20, -10, 0, -70, 30])
joint = planner.create_joint_path(home) \
    .move_joint(pick, 50, FanucMotion.cnt(100)) \
    .move_joint(home, 50, FanucMotion.fine()) \
    .build()

# L 200mm/sec CR10, then a circle of radius 30 mm at 150 mm/s
def wpr(x, y, z, w, p, r):
    return FanucMotion.to_cartesian_pose(XYZWPRPosition(x, y, z, w, p, r))

plane = wpr(600, 0, 250, 0, 0, 0)  # origin = center of the circle
cartesian = planner.create_cartesian_path(wpr(500, 0, 300, 180, 0, 0)) \
    .move_linear(wpr(600, 0, 300, 180, 0, 0), 200, FanucMotion.cr(10)) \
    .add_circle(plane, 30, 150, FanucMotion.fine()) \
    .build()

# Fanuc positions of the trajectory, with continuous W, P, R
positions = FanucMotion.sample_cartesian(cartesian, 0.008)

# Duration, one position per cycle
print(f"Duration: {joint.duration:.3f} s")
samples = joint.sample_joints(0.008)

# Velocity, acceleration and jerk of each axis, computed as the robot does
report = joint.check(joint_limits, 0.008, False)
print(report.is_valid)
```

Documentation: [Motion planner](https://underautomation.com/fanuc/documentation/motion).

## Examples

The folder [`examples`](examples) contains scripts ready to run, one folder per protocol. The first run
asks the address of the robot (or the path of the ROBOGUIDE robot) and the credentials, and saves them in
`examples/robot_config.json` (ignored by git). It also checks the license and asks a key when the trial
has ended.

Run a script from the root of the repository, or choose it in the menu of the launcher:

```bash
python examples/snpx/snpx_write_numeric_register.py
python examples/launcher.py
```

| File | Role |
| --- | --- |
| [`examples/launcher.py`](examples/launcher.py) | Menu that lists the examples by category and runs the one you choose. |
| [`examples/__init__.py`](examples/__init__.py) | Shared helpers: Python path, connection settings, license registration. |

The scripts that move the robot (RMI, Stream Motion) need the surroundings of the robot to be checked
first.

### FTP

| Script | What it does |
| --- | --- |
| [ftp_check_file_exists.py](examples/ftp/ftp_check_file_exists.py) | Checks if a file or a folder exists on the controller. |
| [ftp_current_position.py](examples/ftp/ftp_current_position.py) | Reads the current position (joints and Cartesian) of every motion group. |
| [ftp_download_file.py](examples/ftp/ftp_download_file.py) | Downloads a file from the controller. |
| [ftp_error_list.py](examples/ftp/ftp_error_list.py) | Reads the alarm history with codes, dates and active state. |
| [ftp_get_all_variables.py](examples/ftp/ftp_get_all_variables.py) | Browses all the variable files, searches and opens structures. |
| [ftp_io_state.py](examples/ftp/ftp_io_state.py) | Reads all the digital I/O states (DIN, DOUT, RI, RO, UI, UO, SI, SO, FLG). |
| [ftp_list_files.py](examples/ftp/ftp_list_files.py) | Lists the files and folders of the controller. |
| [ftp_program_states.py](examples/ftp/ftp_program_states.py) | Reads the state of the tasks and programs, with the call history. |
| [ftp_read_features.py](examples/ftp/ftp_read_features.py) | Lists the software options installed on the controller. |
| [ftp_read_numeric_registers.py](examples/ftp/ftp_read_numeric_registers.py) | Reads the numeric registers (R[1], R[2]...). |
| [ftp_read_position_registers.py](examples/ftp/ftp_read_position_registers.py) | Reads the position registers (PR[1], PR[2]...), Cartesian and joints. |
| [ftp_read_string_registers.py](examples/ftp/ftp_read_string_registers.py) | Reads the string registers (SR[1], SR[2]...). |
| [ftp_read_system_variables.py](examples/ftp/ftp_read_system_variables.py) | Reads common system variables (robot name, host name, language...). |
| [ftp_safety_status.py](examples/ftp/ftp_safety_status.py) | Reads the safety signals: E-Stop, deadman, fence, TP enable... |
| [ftp_summary_diagnostic.py](examples/ftp/ftp_summary_diagnostic.py) | Reads a complete diagnostic: position, safety, I/O, options, programs. |
| [ftp_upload_file.py](examples/ftp/ftp_upload_file.py) | Uploads a file to the controller. |

### CGTP

| Script | What it does |
| --- | --- |
| [cgtp_batch_read.py](examples/cgtp/cgtp_batch_read.py) | Reads several variables and registers in one request. |
| [cgtp_batch_write.py](examples/cgtp/cgtp_batch_write.py) | Writes several variables in one request. |
| [cgtp_change_active_program.py](examples/cgtp/cgtp_change_active_program.py) | Changes the active TP program. |
| [cgtp_create_delete_program.py](examples/cgtp/cgtp_create_delete_program.py) | Creates a TP program and deletes it. |
| [cgtp_http_files.py](examples/cgtp/cgtp_http_files.py) | Lists and downloads the variable files, TP programs and diagnostic files. |
| [cgtp_kinematics.py](examples/cgtp/cgtp_kinematics.py) | Computes the forward and inverse kinematics on the controller. |
| [cgtp_list_read_files.py](examples/cgtp/cgtp_list_read_files.py) | Lists the files of the controller and reads their content. |
| [cgtp_pause_abort.py](examples/cgtp/cgtp_pause_abort.py) | Pauses all the programs and aborts a task. |
| [cgtp_program_properties.py](examples/cgtp/cgtp_program_properties.py) | Reads and writes the properties of a program: comment, owner, stack size, ignore pause... |
| [cgtp_read_current_position.py](examples/cgtp/cgtp_read_current_position.py) | Reads the current Cartesian and joint position. |
| [cgtp_read_io_comments.py](examples/cgtp/cgtp_read_io_comments.py) | Reads the comments of the robot, digital, group or analog I/O. |
| [cgtp_read_numeric_registers.py](examples/cgtp/cgtp_read_numeric_registers.py) | Reads the numeric registers (R[]) with their comments. |
| [cgtp_read_position_register.py](examples/cgtp/cgtp_read_position_register.py) | Reads a position register with its comment. |
| [cgtp_read_set_comments.py](examples/cgtp/cgtp_read_set_comments.py) | Reads the comments of registers or I/O, and sets a comment. |
| [cgtp_read_string_registers.py](examples/cgtp/cgtp_read_string_registers.py) | Reads the string registers (SR[]) with their comments. |
| [cgtp_read_variable.py](examples/cgtp/cgtp_read_variable.py) | Reads a system or program variable, as a string or a typed value. |
| [cgtp_read_write_io.py](examples/cgtp/cgtp_read_write_io.py) | Reads and writes I/O ports (DI, DO, RI, RO, GI, GO, AI, AO, flags). |
| [cgtp_rename_program.py](examples/cgtp/cgtp_rename_program.py) | Renames a TP program. |
| [cgtp_select_run_program.py](examples/cgtp/cgtp_select_run_program.py) | Selects a TP program and runs it from a given line. |
| [cgtp_simulate_io.py](examples/cgtp/cgtp_simulate_io.py) | Simulates and unsimulates I/O ports, reads their simulation state. |
| [cgtp_user_alarms.py](examples/cgtp/cgtp_user_alarms.py) | Reads the user alarms and sets their severity. |
| [cgtp_write_numeric_register.py](examples/cgtp/cgtp_write_numeric_register.py) | Writes an integer or a real value to a numeric register. |
| [cgtp_write_string_register.py](examples/cgtp/cgtp_write_string_register.py) | Writes a string register. |
| [cgtp_write_variable.py](examples/cgtp/cgtp_write_variable.py) | Writes a numeric value to a system or program variable. |

### SNPX

| Script | What it does |
| --- | --- |
| [snpx_clear_alarms.py](examples/snpx/snpx_clear_alarms.py) | Clears the active alarms. |
| [snpx_read_alarm_history.py](examples/snpx/snpx_read_alarm_history.py) | Reads the alarm history with severity and cause. |
| [snpx_read_alarms.py](examples/snpx/snpx_read_alarms.py) | Reads the active alarms with ID, severity, message and cause. |
| [snpx_read_batch_flags.py](examples/snpx/snpx_read_batch_flags.py) | Reads several flags in one request. |
| [snpx_read_batch_registers.py](examples/snpx/snpx_read_batch_registers.py) | Reads several numeric registers in one request. |
| [snpx_read_current_position.py](examples/snpx/snpx_read_current_position.py) | Reads the current Cartesian and joint position. |
| [snpx_read_digital_io.py](examples/snpx/snpx_read_digital_io.py) | Reads digital signals (SDI, SDO, RDI, RDO, UI, UO, SI, SO, WI, WO). |
| [snpx_read_flag.py](examples/snpx/snpx_read_flag.py) | Reads a flag (FLG[i]). |
| [snpx_read_integer_sysvar.py](examples/snpx/snpx_read_integer_sysvar.py) | Reads integer system variables by name (`$MCR.$GENOVERRIDE`). |
| [snpx_read_numeric_io.py](examples/snpx/snpx_read_numeric_io.py) | Reads group and analog I/O (GI, GO, AI, AO). |
| [snpx_read_numeric_register.py](examples/snpx/snpx_read_numeric_register.py) | Reads a numeric register (R[i]). |
| [snpx_read_position_register.py](examples/snpx/snpx_read_position_register.py) | Reads a position register (PR[i]), Cartesian and joints. |
| [snpx_read_string_register.py](examples/snpx/snpx_read_string_register.py) | Reads a string register (SR[i]). |
| [snpx_write_digital_output.py](examples/snpx/snpx_write_digital_output.py) | Writes digital outputs (SDO, RDO, UO, SO, WO). |
| [snpx_write_flag.py](examples/snpx/snpx_write_flag.py) | Writes a flag and reads it back. |
| [snpx_write_numeric_register.py](examples/snpx/snpx_write_numeric_register.py) | Writes a numeric register and reads it back. |
| [snpx_write_position_register.py](examples/snpx/snpx_write_position_register.py) | Writes a position register, Cartesian or joints. |
| [snpx_write_string_register.py](examples/snpx/snpx_write_string_register.py) | Writes a string register and reads it back. |
| [snpx_write_sysvar.py](examples/snpx/snpx_write_sysvar.py) | Writes a system variable (speed override) with `set_variable`. |

### Telnet

| Script | What it does |
| --- | --- |
| [telnet_get_position.py](examples/telnet/telnet_get_position.py) | Reads the current Cartesian position (X, Y, Z, W, P, R). |
| [telnet_read_variable.py](examples/telnet/telnet_read_variable.py) | Reads a variable by name (`$MCR.$GENOVERRIDE`). |
| [telnet_set_port.py](examples/telnet/telnet_set_port.py) | Sets an output port (DOUT, RDO, OPOUT, TPOUT, GOUT). |
| [telnet_simulate_port.py](examples/telnet/telnet_simulate_port.py) | Simulates and unsimulates I/O ports. |
| [telnet_task_info.py](examples/telnet/telnet_task_info.py) | Reads the state of a task: status, current line, routine, program type. |
| [telnet_write_variable.py](examples/telnet/telnet_write_variable.py) | Writes a numeric value to a variable. |
| [telnet_program_control.py](examples/telnet/telnet_program_control.py) | Runs, pauses, resumes and aborts a program. |

### Kinematics and motion planner (offline, no robot)

| Script | What it does |
| --- | --- |
| [kinematics_forward_inverse.py](examples/kinematics/kinematics_forward_inverse.py) | Chooses a model, shows its DH parameters, computes the forward kinematics and every inverse kinematics solution. |
| [motion_frames_quaternions.py](examples/motion/motion_frames_quaternions.py) | Converts W, P, R to quaternions, interpolates orientations, changes frames. |
| [motion_joint_path.py](examples/motion/motion_joint_path.py) | Plans joint motions (J, CNT, FINE), reads the duration, the velocity, the acceleration and the jerk. |
| [motion_shapes.py](examples/motion/motion_shapes.py) | Creates a circle, a rounded rectangle, a helix and a spline through points. |
| [motion_timed_points.py](examples/motion/motion_timed_points.py) | Goes through joint positions at given times, checks the limits and slows down when needed. |

### Stream Motion (option J519)

These scripts need a TP program with `IBGN start[1]` and `IBGN end[1]` running on the robot, in AUTO mode
at 100% override.

| Script | What it does |
| --- | --- |
| [stream_motion_cartesian_circle.py](examples/stream_motion/stream_motion_cartesian_circle.py) | Draws a horizontal circle that starts and ends at the current position. |
| [stream_motion_io.py](examples/stream_motion/stream_motion_io.py) | Reads DI[1] to DI[16] during a session and sets DO[1] during a motion. |
| [stream_motion_joint_move.py](examples/stream_motion/stream_motion_joint_move.py) | Moves J1 back and forth within the limits of the robot. |
| [stream_motion_monitor.py](examples/stream_motion/stream_motion_monitor.py) | Reads the limits, then shows the position and the state of the robot (no motion). |
| [stream_motion_override_pause.py](examples/stream_motion/stream_motion_override_pause.py) | Changes the override, pauses, resumes and aborts a motion. |
| [stream_motion_tracking.py](examples/stream_motion/stream_motion_tracking.py) | The robot follows a J1 target that you type, also during the motion. |

### License

| Script | What it does |
| --- | --- |
| [license_info_example.py](examples/license/license_info_example.py) | Shows the license state, registers a license and shows its properties. |

## Robot configuration

### Telnet KCL

1. Go to **SETUP > Host Comm**.
2. Select **TELNET**, then **[DETAIL]**.
3. Set a password and restart the controller.

Tutorial: [underautomation.com/fanuc/documentation/telnet-enable-on-robot](https://underautomation.com/fanuc/documentation/telnet-enable-on-robot)

### FTP

1. Go to **SETUP > Host Comm > FTP**.
2. Set a user and a password.
3. Do a cold start.

### SNPX

- FANUC America parameters (R650 FRA): the controller needs option R553 "HMI Device SNPX".
- FANUC Ltd. parameters (R651 FRL): no option is needed.

### Stream Motion

1. Check that option J519 Stream Motion is installed (`features.has_stream_motion`).
2. Set `$PARAM_GROUP[1].$SV_OFF_ENB[*]` to `FALSE`.
3. Run a TP program with `IBGN start[1]` and `IBGN end[1]`, in AUTO mode at 100% override.

Tutorial: [underautomation.com/fanuc/documentation/stream-motion](https://underautomation.com/fanuc/documentation/stream-motion)

## Compatibility

- **Python:** 3.7 to 3.13, with pythonnet 3.0.5.
- **Operating systems:** Windows (.NET Framework), Linux and macOS (.NET runtime and `export PYTHONNET_RUNTIME=coreclr`).
- **Controllers:** R-J3iB, R-30iA, R-30iB, R-50iA, and ROBOGUIDE.

## License

This SDK needs a commercial license. A 30-day trial starts at the first use, no key needed. After the
trial, register your key in your code:

```python
from underautomation.fanuc.fanuc_robot import FanucRobot

license_info = FanucRobot.register_license("Your Company", "your-license-key")
print(license_info.state)
```

- License agreement: [underautomation.com/fanuc/eula](https://underautomation.com/fanuc/eula) and [License.md](License.md)
- Trial key: [underautomation.com/license](https://underautomation.com/license?sdk=fanuc)
- Prices and quote: [underautomation.com/fanuc](https://underautomation.com/fanuc)

## Support

- Documentation: [underautomation.com/fanuc/documentation](https://underautomation.com/fanuc/documentation)
- Issues: [GitHub Issues](https://github.com/underautomation/Fanuc.py/issues)
- Contact: [underautomation.com/contact](https://underautomation.com/contact)
