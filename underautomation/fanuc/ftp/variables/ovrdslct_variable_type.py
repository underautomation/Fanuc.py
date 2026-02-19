import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import OvrdslctVariableType as ovrdslct_variable_type

class OvrdslctVariableType(GenericVariableType):
	'''Describes the Fanuc type OVRDSLCT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ovrdslct_variable_type()
		else:
			self._instance = _internal

	@property
	def ovsl_enb(self) -> bool:
		'''Value of variable $OVSL_ENB'''
		return self._instance.OvslEnb

	@property
	def sdi_index1(self) -> int:
		'''Value of variable $SDI_INDEX1'''
		return self._instance.SdiIndex1

	@property
	def sdi_index2(self) -> int:
		'''Value of variable $SDI_INDEX2'''
		return self._instance.SdiIndex2

	@property
	def off_off_ovr(self) -> int:
		'''Value of variable $OFF_OFF_OVR'''
		return self._instance.OffOffOvr

	@property
	def off_on_ovrd(self) -> int:
		'''Value of variable $OFF_ON_OVRD'''
		return self._instance.OffOnOvrd

	@property
	def on_off_ovrd(self) -> int:
		'''Value of variable $ON_OFF_OVRD'''
		return self._instance.OnOffOvrd

	@property
	def on_on_ovrd(self) -> int:
		'''Value of variable $ON_ON_OVRD'''
		return self._instance.OnOnOvrd

	@property
	def dummy(self) -> int:
		'''Value of variable $DUMMY'''
		return self._instance.Dummy

	@property
	def dcs_ctl_enb(self) -> bool:
		'''Value of variable $DCS_CTL_ENB'''
		return self._instance.DcsCtlEnb

	@property
	def dcs_ovrd(self) -> int:
		'''Value of variable $DCS_OVRD'''
		return self._instance.DcsOvrd

	@property
	def ovrd_zero(self) -> bool:
		'''Value of variable $OVRD_ZERO'''
		return self._instance.OvrdZero

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, OvrdslctVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
