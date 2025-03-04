import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbcsgGrpVariableType as tbcsg_grp_variable_type

class TbcsgGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbcsg_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def apprc_scl(self) -> typing.List[float]:
		return self._instance.ApprcScl
	@property
	def open_scl(self) -> typing.List[float]:
		return self._instance.OpenScl
	@property
	def close_scl(self) -> typing.List[float]:
		return self._instance.CloseScl
	@property
	def cls_minf2(self) -> typing.List[float]:
		return self._instance.ClsMinf2
	@property
	def cls_minacc(self) -> typing.List[float]:
		return self._instance.ClsMinacc
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
