import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ModemInfVariableType as modem_inf_variable_type

class ModemInfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = modem_inf_variable_type()
		else:
			self._instance = _internal
	@property
	def mdm_init(self) -> str:
		return self._instance.MdmInit
	@property
	def mdm_init1(self) -> str:
		return self._instance.MdmInit1
	@property
	def mdm_reset(self) -> str:
		return self._instance.MdmReset
	@property
	def mdm_hangup(self) -> str:
		return self._instance.MdmHangup
	@property
	def mdm_dial(self) -> str:
		return self._instance.MdmDial
	@property
	def mdm_answer(self) -> str:
		return self._instance.MdmAnswer
	@property
	def mdm_status(self) -> str:
		return self._instance.MdmStatus
	@property
	def mdm_ident(self) -> str:
		return self._instance.MdmIdent
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
