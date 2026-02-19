import typing
from underautomation.fanuc.ftp.variables.auto_col_rec_variable_type import AutoColRecVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import HtcolrecFile as htcolrec_file

class HtcolrecFile(GenericVariableFile):
	'''Describes the Fanuc variable file htcolrec.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = htcolrec_file()
		else:
			self._instance = _internal

	@property
	def col_rec(self) -> bool:
		'''Value of variable COL_REC'''
		return self._instance.ColRec

	@property
	def col_recov(self) -> AutoColRecVariableType:
		'''Value of variable COL_RECOV'''
		return AutoColRecVariableType(self._instance.ColRecov)

	@property
	def col_dbg(self) -> bool:
		'''Value of variable COL_DBG'''
		return self._instance.ColDbg

	@property
	def abort_delay(self) -> int:
		'''Value of variable ABORT_DELAY'''
		return self._instance.AbortDelay

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HtcolrecFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
