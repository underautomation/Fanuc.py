## RMI: complete API rewrite

The RMI client has been redesigned from scratch. The previous method-per-instruction API is replaced by an instruction object model.

### Instruction pipeline

Each call to `send_tp_instruction` returns an `RmiInstructionResponse` that you can block on:

```python
from underautomation.fanuc.rmi.tp_instructions.cartesian_linear_instructions import LinearMotionTpInstruction
from underautomation.fanuc.rmi.data.enums import RmiLinearSpeedType, RmiTerminationType
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame

instr = LinearMotionTpInstruction()
instr.speed_type = RmiLinearSpeedType.MM_SEC
instr.speed = 100
instr.term_type = RmiTerminationType.FINE
instr.target = CartesianPositionWithUserFrame(500, 200, 300, 0, 90, 0, 1, 0)

r = robot.rmi.send_tp_instruction(instr)

# Wait for the controller to confirm execution
r.wait_for_completion()
print(r.status)  # Completed or Error
```

The client manages the 8-slot controller buffer automatically. Instructions that exceed the limit are held in a local queue.

### New instruction classes

| Class                             | TP equivalent                                   |
| --------------------------------- | ----------------------------------------------- |
| `LinearMotionTpInstruction`       | `L P[] mm/sec FINE`                             |
| `LinearRelativeTpInstruction`     | `L P[] mm/sec FINE INC`                         |
| `JointMotionTpInstruction`        | `J P[] % FINE`                                  |
| `JointRelativeTpInstruction`      | `J P[] % FINE INC`                              |
| `CircularMotionTpInstruction`     | `C P[] P[] mm/sec FINE`                         |
| `CircularRelativeTpInstruction`   | `C P[] P[] mm/sec FINE INC`                     |
| `LinearMotionJRepTpInstruction`   | linear, joint-angle target                      |
| `LinearRelativeJRepTpInstruction` | incremental linear, joint-angle target          |
| `JointMotionJRepTpInstruction`    | joint, joint-angle target                       |
| `JointRelativeJRepTpInstruction`  | incremental joint, joint-angle target           |
| `SplineMotionTpInstruction`       | `S P[] mm/sec CNT` (requires MajorVersion >= 7) |
| `SplineMotionJRepTpInstruction`   | spline, joint-angle target                      |
| `WaitDinTpInstruction`            | `WAIT DI[n] = ON/OFF`                           |
| `WaitTimeTpInstruction`           | `WAIT t(sec)`                                   |
| `SetUFrameTpInstruction`          | `UFRAME_NUM = n`                                |
| `SetUToolTpInstruction`           | `UTOOL_NUM = n`                                 |
| `SetPayloadTpInstruction`         | `PAYLOAD[n]`                                    |
| `CallProgramTpInstruction`        | `CALL program`                                  |

### New admin methods

- `initialize(group_mask, rtsa, pltz_mode)`: starts RMI_MOVE with optional multi-group, singularity avoidance, and palletizing header.
- `auto_set_next_sequence_id()`: re-synchronizes the local sequence counter.
- `get_extended_status()`: returns drive state, control mode, and speed clamp.
- `read_numeric_register` / `write_numeric_register_as_integer` / `write_numeric_register_as_double`
- `read_variable` / `write_variable_as_integer` / `write_variable_as_double`
- `set_payload_value(...)` / `set_payload_compensation(...)` / `set_payload_schedule(n)`
- `read_io_port` / `write_io_port`
- `clear_completed_instructions()` / `clear_local_queued_instructions()`

### New events

- `connection_terminated`
- `system_fault_received`
- `recorded_cartesian_position_received` / `recorded_joint_position_received`

### Hold state detection

`is_in_hold_state` is now a property. Call `reset()` to exit the hold state.

---

## FTP: FtpExistsBehavior on upload methods

`upload_file_to_controller` now accepts an `exists_behavior` parameter:

```python
from underautomation.fanuc.ftp.ftp_exists_behavior import FtpExistsBehavior

robot.ftp.direct_file_handling.upload_file_to_controller(
    r"C:\Programs\MyPrg.tp",
    "md:/MyPrg.tp",
    exists_behavior=FtpExistsBehavior.SKIP)
```

| Value             | Behavior                               |
| ----------------- | -------------------------------------- |
| `NO_CHECK`        | Skip existence check.                  |
| `SKIP`            | Do nothing if the file already exists. |
| `OVERWRITE`       | Replace the file (default).            |
| `APPEND`          | Resume a partial upload.               |
| `APPEND_NO_CHECK` | Append without checking.               |

---

## CGTP: fix file download on some controllers

Fixed a bug where downloading files via CGTP could fail or return incomplete data on certain controllers.
