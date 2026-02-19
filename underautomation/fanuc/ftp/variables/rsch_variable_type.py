import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RschVariableType as rsch_variable_type

class RschVariableType(GenericVariableType):
	'''Describes the Fanuc type RSCH_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rsch_variable_type()
		else:
			self._instance = _internal

	@property
	def old_spec_sw(self) -> bool:
		'''Value of variable $OLD_SPEC_SW'''
		return self._instance.OldSpecSw

	@property
	def freefromsiz(self) -> int:
		'''Value of variable $FREEFROMSIZ'''
		return self._instance.Freefromsiz

	@property
	def target_dir(self) -> str:
		'''Value of variable $TARGET_DIR'''
		return self._instance.TargetDir

	@property
	def updt_map(self) -> int:
		'''Value of variable $UPDT_MAP'''
		return self._instance.UpdtMap

	@property
	def reptsk_enb(self) -> bool:
		'''Value of variable $REPTSK_ENB'''
		return self._instance.ReptskEnb

	@property
	def exp_enb(self) -> bool:
		'''Value of variable $EXP_ENB'''
		return self._instance.ExpEnb

	@property
	def exp_dir(self) -> str:
		'''Value of variable $EXP_DIR'''
		return self._instance.ExpDir

	@property
	def default_dev(self) -> bool:
		'''Value of variable $DEFAULT_DEV'''
		return self._instance.DefaultDev

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RschVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
