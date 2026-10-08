from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.xf_variable_type import XfVariableType
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.common.files.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Common.Files.Variables import DbinfoVariableType as dbinfo_variable_type

class DbinfoVariableType(GenericVariableType):
	'''Describes the Fanuc type DBINFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbinfo_variable_type()
		else:
			self._instance = _internal

	@property
	def dat_ad(self) -> int:
		'''Value of variable $DAT_AD'''
		return self._instance.DatAd

	@property
	def mlb(self) -> int:
		'''Value of variable $MLB'''
		return self._instance.Mlb

	@property
	def id(self) -> int:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def tid(self) -> int:
		'''Value of variable $TID'''
		return self._instance.Tid

	@property
	def xf(self) -> XfVariableType:
		'''Value of variable $XF'''
		__r = self._instance.Xf
		return None if __r is None else XfVariableType(__r)

	@property
	def uxf(self) -> XfVariableType:
		'''Value of variable $UXF'''
		__r = self._instance.Uxf
		return None if __r is None else XfVariableType(__r)

	@property
	def r_xf(self) -> XfVariableType:
		'''Value of variable $R_XF'''
		__r = self._instance.RXf
		return None if __r is None else XfVariableType(__r)

	@property
	def dpos(self) -> XYZPosition:
		'''Value of variable $DPOS'''
		__r = self._instance.Dpos
		return None if __r is None else XYZPosition(None, None, None, __r)

	@property
	def loc(self) -> XYZPosition:
		'''Value of variable $LOC'''
		__r = self._instance.Loc
		return None if __r is None else XYZPosition(None, None, None, __r)

	@property
	def line(self) -> int:
		'''Value of variable $LINE'''
		return self._instance.Line

	@property
	def ept(self) -> int:
		'''Value of variable $EPT'''
		return self._instance.Ept

	@property
	def cnd(self) -> int:
		'''Value of variable $CND'''
		return self._instance.Cnd

	@property
	def prgdat(self) -> int:
		'''Value of variable $PRGDAT'''
		return self._instance.Prgdat

	@property
	def offset(self) -> XYZPosition:
		'''Value of variable $OFFSET'''
		__r = self._instance.Offset
		return None if __r is None else XYZPosition(None, None, None, __r)

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DbinfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
