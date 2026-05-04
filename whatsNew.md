## CGTP: write position into a TP program

`CgtpClient` has a new `set_program_position` method. It writes a Cartesian or joint position to a given position index (P[n]) inside a TP program. Only the first motion group is supported via CGTP.

```python
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition

# Cartesian position
position = Position(0, 1, None, ExtendedCartesianPosition(500, 200, 300, 0, 90, 0, 0, 0, 0))
robot.cgtp.set_program_position("MY_PROG", 1, position)

# Joint position
joint_position = Position(0, 1, JointsPosition(j1=0, j2=0, j3=0, j4=0, j5=-90, j6=0), None)
robot.cgtp.set_program_position("MY_PROG", 2, joint_position)
```

## FTP connection timeout

The `FtpConnectParameters` class has a new `ftp_timeout_ms` property. It controls the connection, read, and data transfer timeouts for all FTP operations. The default is 30,000 ms (30 seconds).

```python
parameters.ftp.enable = True
parameters.ftp.ftp_timeout_ms = 10000  # 10 seconds
```

## CGTP: record current position into a program

`CgtpClient` has a new `set_program_position_to_current_cartesian_position` method. It writes the robot's current Cartesian position to a given position index inside a TP program and returns the recorded position.

```python
pos = robot.cgtp.set_program_position_to_current_cartesian_position("MY_PROG", 1)
print(f"Recorded: X={pos.x}, Y={pos.y}, Z={pos.z}")
```
