## Asynchronous FTP methods

The .NET library adds an asynchronous version of each blocking FTP method. Python uses the synchronous methods, which do not change.

## FTP errors

When the controller refuses an FTP operation, the SDK raises an `FtpException` with the reply of the controller (`ReplyCode`, `ReplyMessage`) and what to do. `ProgramInUse` is true when the program is selected or runs ("Specified program is in use"): select another program on the teach pendant, or with `robot.cgtp.select_program(...)` (firmware V9.10 and later). Without an FTP user, the controller logs in at the OPERATOR level and can refuse the upload of a program ("Operation password protected"): the message says to use a user of a higher level.

```python
from UnderAutomation.Fanuc.Ftp import FtpException

try:
    robot.ftp.direct_file_handling.upload_file_to_controller(r"C:\Programs\MyPrg.ls", "md:/MyPrg.ls")
except FtpException as ex:
    if ex.ProgramInUse:
        robot.cgtp.select_program("OTHER")
```

`FtpException` derives from the .NET `Exception`: an `except Exception` still catches these errors.

## FTP fixes

- The FTP client was updated.
- Paths with a device (`fr:`, `md:job.ls`): `get_listing("fr:")` lists `fr:`, and no longer the current device. `file_exists` and `get_object_info` find `md:job.ls`, `md:/job.ls` and `job.ls`, with any case.
- `get_object_info` returns `None` for a missing file, as documented, instead of raising an error.
- `get_summary_diagnostic`, `get_variables_from_file`, `known_variable_files...` raise an `FtpException` when the download of the file fails, instead of returning an empty result.
- Setting `robot.ftp.language` changes the encoding of the connection at once. It used the previous language.
- `disconnect` releases the connection, so that a new `connect` does not leave the previous one open.
- `upload_file_to_controller` with `FtpExistsBehavior.Skip` or `Append` checks the existing file correctly on the devices of the controller.
- `robot.cgtp.http.download_as_bytes`: the controller can close the connection at the end of a binary file. The data received is now returned, as documented, instead of an error.
## Package information

The PyPI page links to the release notes and to the issues of `Fanuc.py`. The source distribution contains the license agreement (`License.md`).

## Linux and macOS

The README now sets the .NET runtime with `export PYTHONNET_RUNTIME=coreclr`. Without `export`, the variable does not reach Python and pythonnet uses Mono.
