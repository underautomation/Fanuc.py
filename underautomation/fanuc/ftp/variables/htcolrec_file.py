import typing
from underautomation.fanuc.ftp.variables.auto_col_rec_variable_type import AutoColRecVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HtcolrecFile as htcolrec_file

class HtcolrecFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = htcolrec_file()
		else:
			self._instance = _internal
	@property
	def col_rec(self) -> bool:
		return self._instance.ColRec
	@property
	def col_recov(self) -> AutoColRecVariableType:
		return AutoColRecVariableType(self._instance.ColRecov)
	@property
	def col_dbg(self) -> bool:
		return self._instance.ColDbg
	@property
	def abort_delay(self) -> int:
		return self._instance.AbortDelay
