import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MoptimizVariableType as moptimiz_variable_type

class MoptimizVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = moptimiz_variable_type()
		else:
			self._instance = _internal
	@property
	def data_out(self) -> bool:
		return self._instance.DataOut
	@property
	def cnt_dyn_acc(self) -> typing.List[bool]:
		return self._instance.CntDynAcc
	@property
	def dd_motor1(self) -> typing.List[bool]:
		return self._instance.DdMotor1
	@property
	def update_map3(self) -> typing.List[bool]:
		return self._instance.UpdateMap3
	@property
	def update_map7(self) -> bool:
		return self._instance.UpdateMap7
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
