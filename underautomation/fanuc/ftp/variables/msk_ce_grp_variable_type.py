import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MskCeGrpVariableType as msk_ce_grp_variable_type

class MskCeGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = msk_ce_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def t1_usercart(self) -> float:
		return self._instance.T1Usercart
	@property
	def t1_userjnt(self) -> typing.List[float]:
		return self._instance.T1Userjnt
	@property
	def t1_cartvel(self) -> float:
		return self._instance.T1Cartvel
	@property
	def t1_jntvel(self) -> typing.List[float]:
		return self._instance.T1Jntvel
	@property
	def t1_warning(self) -> bool:
		return self._instance.T1Warning
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
