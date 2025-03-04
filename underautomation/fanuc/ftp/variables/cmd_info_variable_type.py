import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CmdInfoVariableType as cmd_info_variable_type

class CmdInfoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cmd_info_variable_type()
		else:
			self._instance = _internal
	@property
	def trq_cmd(self) -> typing.List[float]:
		return self._instance.TrqCmd
	@property
	def jnt_pos(self) -> typing.List[float]:
		return self._instance.JntPos
	@property
	def cart_pos(self) -> typing.List[float]:
		return self._instance.CartPos
	@property
	def cart_pos_uf(self) -> typing.List[float]:
		return self._instance.CartPosUf
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
