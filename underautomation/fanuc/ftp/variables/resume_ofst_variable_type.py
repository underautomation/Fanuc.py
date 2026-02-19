import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ResumeOfstVariableType as resume_ofst_variable_type

class ResumeOfstVariableType(GenericVariableType):
	'''Describes the Fanuc type $RESUME_OFST'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = resume_ofst_variable_type()
		else:
			self._instance = _internal

	@property
	def ro_enable(self) -> bool:
		'''Value of variable $RO_ENABLE'''
		return self._instance.RoEnable

	@property
	def ro_max_itp(self) -> int:
		'''Value of variable $RO_MAX_ITP'''
		return self._instance.RoMaxItp

	@property
	def ro_nom_dist(self) -> float:
		'''Value of variable $RO_NOM_DIST'''
		return self._instance.RoNomDist

	@property
	def ro_nom_spd(self) -> float:
		'''Value of variable $RO_NOM_SPD'''
		return self._instance.RoNomSpd

	@property
	def ro_mode_sw(self) -> int:
		'''Value of variable $RO_MODE_SW'''
		return self._instance.RoModeSw

	@property
	def ro_tune_pam(self) -> float:
		'''Value of variable $RO_TUNE_PAM'''
		return self._instance.RoTunePam

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ResumeOfstVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
