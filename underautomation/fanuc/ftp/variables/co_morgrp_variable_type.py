import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CoMorgrpVariableType as co_morgrp_variable_type

class CoMorgrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = co_morgrp_variable_type()
		else:
			self._instance = _internal
	@property
	def flen(self) -> int:
		return self._instance.Flen
	@property
	def angle(self) -> float:
		return self._instance.Angle
	@property
	def tba_mag(self) -> float:
		return self._instance.TbaMag
	@property
	def tba_mag_pre(self) -> float:
		return self._instance.TbaMagPre
	@property
	def tba_mag_max(self) -> float:
		return self._instance.TbaMagMax
	@property
	def tba_magaxs(self) -> typing.List[float]:
		return self._instance.TbaMagaxs
	@property
	def tba_curaxs(self) -> typing.List[float]:
		return self._instance.TbaCuraxs
	@property
	def tba_prvaxs(self) -> typing.List[float]:
		return self._instance.TbaPrvaxs
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
