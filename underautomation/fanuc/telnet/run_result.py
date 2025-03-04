import typing
from underautomation.fanuc.telnet.program_command_result import ProgramCommandResult
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import RunResult as run_result

class RunResult(ProgramCommandResult):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = run_result()
		else:
			self._instance = _internal
