import typing
from underautomation.fanuc.ftp.variables.amp_coef_variable_type import AmpCoefVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CtrlCabVariableType as ctrl_cab_variable_type

class CtrlCabVariableType(GenericVariableType):
	'''Describes the Fanuc type CTRL_CAB_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ctrl_cab_variable_type()
		else:
			self._instance = _internal

	@property
	def trans_a(self) -> float:
		'''Value of variable $TRANS_A'''
		return self._instance.TransA

	@property
	def idle_pwr(self) -> float:
		'''Value of variable $IDLE_PWR'''
		return self._instance.IdlePwr

	@property
	def amp_coefb(self) -> float:
		'''Value of variable $AMP_COEFB'''
		return self._instance.AmpCoefb

	@property
	def sv_num(self) -> int:
		'''Value of variable $SV_NUM'''
		return self._instance.SvNum

	@property
	def sv_amp(self) -> typing.List[AmpCoefVariableType]:
		'''Value of variable $SV_AMP'''
		return [AmpCoefVariableType(x) for x in self._instance.SvAmp]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CtrlCabVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
