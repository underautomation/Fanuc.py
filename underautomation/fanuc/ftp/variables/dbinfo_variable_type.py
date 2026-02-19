import typing
from underautomation.fanuc.ftp.variables.xf_variable_type import XfVariableType
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DbinfoVariableType as dbinfo_variable_type

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
		return XfVariableType(self._instance.Xf)

	@property
	def uxf(self) -> XfVariableType:
		'''Value of variable $UXF'''
		return XfVariableType(self._instance.Uxf)

	@property
	def r_xf(self) -> XfVariableType:
		'''Value of variable $R_XF'''
		return XfVariableType(self._instance.RXf)

	@property
	def dpos(self) -> XYZPosition:
		'''Value of variable $DPOS'''
		return XYZPosition(None, None, None, self._instance.Dpos)

	@property
	def loc(self) -> XYZPosition:
		'''Value of variable $LOC'''
		return XYZPosition(None, None, None, self._instance.Loc)

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
		return XYZPosition(None, None, None, self._instance.Offset)

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
