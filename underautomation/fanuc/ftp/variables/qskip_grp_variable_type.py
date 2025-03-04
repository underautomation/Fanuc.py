import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import QskipGrpVariableType as qskip_grp_variable_type

class QskipGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = qskip_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def error_cnt2(self) -> typing.List[int]:
		return self._instance.ErrorCnt2
	@property
	def qskp_errcnt(self) -> typing.List[int]:
		return self._instance.QskpErrcnt
	@property
	def qskp_curang(self) -> float:
		return self._instance.QskpCurang
	@property
	def qskp_curan1(self) -> float:
		return self._instance.QskpCuran1
	@property
	def qskp_curan2(self) -> float:
		return self._instance.QskpCuran2
	@property
	def qskp_curan3(self) -> float:
		return self._instance.QskpCuran3
	@property
	def qskp_curan4(self) -> float:
		return self._instance.QskpCuran4
	@property
	def qskp_curan5(self) -> float:
		return self._instance.QskpCuran5
	@property
	def qskp_curan6(self) -> float:
		return self._instance.QskpCuran6
	@property
	def qskp_curan7(self) -> float:
		return self._instance.QskpCuran7
	@property
	def qskp_curan8(self) -> float:
		return self._instance.QskpCuran8
	@property
	def qskp_curan9(self) -> float:
		return self._instance.QskpCuran9
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
