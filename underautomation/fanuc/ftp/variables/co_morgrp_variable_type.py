import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CoMorgrpVariableType as co_morgrp_variable_type

class CoMorgrpVariableType(GenericVariableType):
	'''Describes the Fanuc type CO_MORGRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = co_morgrp_variable_type()
		else:
			self._instance = _internal

	@property
	def flen(self) -> int:
		'''Value of variable $FLEN'''
		return self._instance.Flen

	@property
	def angle(self) -> float:
		'''Value of variable $ANGLE'''
		return self._instance.Angle

	@property
	def tba_mag(self) -> float:
		'''Value of variable $TBA_MAG'''
		return self._instance.TbaMag

	@property
	def tba_mag_pre(self) -> float:
		'''Value of variable $TBA_MAG_PRE'''
		return self._instance.TbaMagPre

	@property
	def tba_mag_max(self) -> float:
		'''Value of variable $TBA_MAG_MAX'''
		return self._instance.TbaMagMax

	@property
	def tba_magaxs(self) -> typing.List[float]:
		'''Value of variable $TBA_MAGAXS'''
		return self._instance.TbaMagaxs

	@property
	def tba_curaxs(self) -> typing.List[float]:
		'''Value of variable $TBA_CURAXS'''
		return self._instance.TbaCuraxs

	@property
	def tba_prvaxs(self) -> typing.List[float]:
		'''Value of variable $TBA_PRVAXS'''
		return self._instance.TbaPrvaxs

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CoMorgrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
