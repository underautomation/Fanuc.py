import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TsrGrpVariableType as tsr_grp_variable_type

class TsrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tsr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def mr_max_trq(self) -> typing.List[float]:
		return self._instance.MrMaxTrq
	@property
	def mr_stal_trq(self) -> typing.List[float]:
		return self._instance.MrStalTrq
	@property
	def mr_brk_trq(self) -> typing.List[float]:
		return self._instance.MrBrkTrq
	@property
	def mr_brk_vel(self) -> typing.List[float]:
		return self._instance.MrBrkVel
	@property
	def mr_nold_vel(self) -> typing.List[float]:
		return self._instance.MrNoldVel
	@property
	def ma_load_trq(self) -> typing.List[float]:
		return self._instance.MaLoadTrq
	@property
	def md_load_trq(self) -> typing.List[float]:
		return self._instance.MdLoadTrq
	@property
	def ma_grav_mgn(self) -> typing.List[float]:
		return self._instance.MaGravMgn
	@property
	def ma_stal_mgn(self) -> typing.List[float]:
		return self._instance.MaStalMgn
	@property
	def ma_brk_mgn(self) -> typing.List[float]:
		return self._instance.MaBrkMgn
	@property
	def md_grav_mgn(self) -> typing.List[float]:
		return self._instance.MdGravMgn
	@property
	def md_stal_mgn(self) -> typing.List[float]:
		return self._instance.MdStalMgn
	@property
	def md_brk_mgn(self) -> typing.List[float]:
		return self._instance.MdBrkMgn
	@property
	def mj_acc_mgn(self) -> typing.List[float]:
		return self._instance.MjAccMgn
	@property
	def mc_acc_mgn(self) -> typing.List[float]:
		return self._instance.McAccMgn
	@property
	def mc_stal_mgn(self) -> typing.List[float]:
		return self._instance.McStalMgn
	@property
	def mc_brk_mgn(self) -> typing.List[float]:
		return self._instance.McBrkMgn
	@property
	def min_cyc_id(self) -> str:
		return self._instance.MinCycId
	@property
	def min_c_id_e1(self) -> str:
		return self._instance.MinCIdE1
	@property
	def min_c_id_e2(self) -> str:
		return self._instance.MinCIdE2
	@property
	def min_c_id_e3(self) -> str:
		return self._instance.MinCIdE3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
