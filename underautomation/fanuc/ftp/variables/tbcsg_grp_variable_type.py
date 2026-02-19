import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbcsgGrpVariableType as tbcsg_grp_variable_type

class TbcsgGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TBCSG_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbcsg_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def apprc_scl(self) -> typing.List[float]:
		'''Value of variable $APPRC_SCL'''
		return self._instance.ApprcScl

	@property
	def open_scl(self) -> typing.List[float]:
		'''Value of variable $OPEN_SCL'''
		return self._instance.OpenScl

	@property
	def close_scl(self) -> typing.List[float]:
		'''Value of variable $CLOSE_SCL'''
		return self._instance.CloseScl

	@property
	def cls_minf2(self) -> typing.List[float]:
		'''Value of variable $CLS_MINF2'''
		return self._instance.ClsMinf2

	@property
	def cls_minacc(self) -> typing.List[float]:
		'''Value of variable $CLS_MINACC'''
		return self._instance.ClsMinacc

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbcsgGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
