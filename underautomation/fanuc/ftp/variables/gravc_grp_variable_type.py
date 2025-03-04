import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GravcGrpVariableType as gravc_grp_variable_type

class GravcGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gravc_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def mode_sw(self) -> int:
		return self._instance.ModeSw
	@property
	def spcons(self) -> typing.List[float]:
		return self._instance.Spcons
	@property
	def debug1(self) -> int:
		return self._instance.Debug1
	@property
	def debug2(self) -> typing.List[float]:
		return self._instance.Debug2
	@property
	def grv_status(self) -> int:
		return self._instance.GrvStatus
	@property
	def bkup_no116(self) -> typing.List[int]:
		return self._instance.BkupNo116
	@property
	def poff_no116(self) -> typing.List[int]:
		return self._instance.PoffNo116
	@property
	def grvcmp_sw(self) -> int:
		return self._instance.GrvcmpSw
	@property
	def grvmst_loop(self) -> int:
		return self._instance.GrvmstLoop
	@property
	def mst_smt_len(self) -> int:
		return self._instance.MstSmtLen
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
