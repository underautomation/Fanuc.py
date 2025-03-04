import typing
from underautomation.fanuc.ftp.variables.xf_variable_type import XfVariableType
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbinfoVariableType as dbinfo_variable_type

class DbinfoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbinfo_variable_type()
		else:
			self._instance = _internal
	@property
	def dat_ad(self) -> int:
		return self._instance.DatAd
	@property
	def mlb(self) -> int:
		return self._instance.Mlb
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def tid(self) -> int:
		return self._instance.Tid
	@property
	def xf(self) -> XfVariableType:
		return XfVariableType(self._instance.Xf)
	@property
	def uxf(self) -> XfVariableType:
		return XfVariableType(self._instance.Uxf)
	@property
	def r_xf(self) -> XfVariableType:
		return XfVariableType(self._instance.RXf)
	@property
	def dpos(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Dpos)
	@property
	def loc(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Loc)
	@property
	def line(self) -> int:
		return self._instance.Line
	@property
	def ept(self) -> int:
		return self._instance.Ept
	@property
	def cnd(self) -> int:
		return self._instance.Cnd
	@property
	def prgdat(self) -> int:
		return self._instance.Prgdat
	@property
	def offset(self) -> XYZPosition:
		return XYZPosition(None, None, None, self._instance.Offset)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
