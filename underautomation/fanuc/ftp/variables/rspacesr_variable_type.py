import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RspacesrVariableType as rspacesr_variable_type

class RspacesrVariableType(GenericVariableType):
	'''Describes the Fanuc type RSPACESR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspacesr_variable_type()
		else:
			self._instance = _internal

	@property
	def sr_enb_typ(self) -> typing.List[int]:
		'''Value of variable $SR_ENB_TYP'''
		return self._instance.SrEnbTyp

	@property
	def runner_axs(self) -> bool:
		'''Value of variable $RUNNER_AXS'''
		return self._instance.RunnerAxs

	@property
	def hand_lngth(self) -> float:
		'''Value of variable $HAND_LNGTH'''
		return self._instance.HandLngth

	@property
	def hand_thick(self) -> float:
		'''Value of variable $HAND_THICK'''
		return self._instance.HandThick

	@property
	def flip_enb(self) -> bool:
		'''Value of variable $FLIP_ENB'''
		return self._instance.FlipEnb

	@property
	def intference(self) -> bool:
		'''Value of variable $INTFERENCE'''
		return self._instance.Intference

	@property
	def hand_if_chk(self) -> bool:
		'''Value of variable $HAND_IF_CHK'''
		return self._instance.HandIfChk

	@property
	def handi_type(self) -> int:
		'''Value of variable $HANDI_TYPE'''
		return self._instance.HandiType

	@property
	def handi_indx(self) -> int:
		'''Value of variable $HANDI_INDX'''
		return self._instance.HandiIndx

	@property
	def sr_g1pos(self) -> typing.List[float]:
		'''Value of variable $SR_G1POS'''
		return self._instance.SrG1pos

	@property
	def sr_g1pos_in(self) -> typing.List[float]:
		'''Value of variable $SR_G1POS_IN'''
		return self._instance.SrG1posIn

	@property
	def sr_g1ang(self) -> typing.List[float]:
		'''Value of variable $SR_G1ANG'''
		return self._instance.SrG1ang

	@property
	def sr_g1ang_jf(self) -> typing.List[float]:
		'''Value of variable $SR_G1ANG_JF'''
		return self._instance.SrG1angJf

	@property
	def sr_prm(self) -> typing.List[int]:
		'''Value of variable $SR_PRM'''
		return self._instance.SrPrm

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RspacesrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
