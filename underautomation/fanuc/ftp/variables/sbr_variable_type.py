import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SbrVariableType as sbr_variable_type

class SbrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sbr_variable_type()
		else:
			self._instance = _internal
	@property
	def svmtr_id(self) -> int:
		return self._instance.SvmtrId
	@property
	def robot_id(self) -> str:
		return self._instance.RobotId
	@property
	def grp_num(self) -> int:
		return self._instance.GrpNum
	@property
	def axis_num(self) -> int:
		return self._instance.AxisNum
	@property
	def mtr_id(self) -> str:
		return self._instance.MtrId
	@property
	def mtr_inf_id(self) -> str:
		return self._instance.MtrInfId
	@property
	def sv_param_id(self) -> str:
		return self._instance.SvParamId
	@property
	def param(self) -> typing.List[int]:
		return self._instance.Param
	@property
	def mot_spd_lim(self) -> int:
		return self._instance.MotSpdLim
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
