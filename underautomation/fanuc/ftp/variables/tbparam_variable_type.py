import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbparamVariableType as tbparam_variable_type

class TbparamVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbparam_variable_type()
		else:
			self._instance = _internal
	@property
	def mr_max_trq(self) -> float:
		return self._instance.MrMaxTrq
	@property
	def mr_stal_trq(self) -> float:
		return self._instance.MrStalTrq
	@property
	def mr_brk_trq(self) -> float:
		return self._instance.MrBrkTrq
	@property
	def mr_brk_vel(self) -> float:
		return self._instance.MrBrkVel
	@property
	def mr_nold_vel(self) -> float:
		return self._instance.MrNoldVel
	@property
	def ma_load_trq(self) -> float:
		return self._instance.MaLoadTrq
	@property
	def md_load_trq(self) -> float:
		return self._instance.MdLoadTrq
	@property
	def max_trq_mgn(self) -> float:
		return self._instance.MaxTrqMgn
	@property
	def ma_grav_mgn(self) -> float:
		return self._instance.MaGravMgn
	@property
	def ma_stal_mgn(self) -> float:
		return self._instance.MaStalMgn
	@property
	def ma_brk_mgn(self) -> float:
		return self._instance.MaBrkMgn
	@property
	def ma_nold_mgn(self) -> float:
		return self._instance.MaNoldMgn
	@property
	def md_grav_mgn(self) -> float:
		return self._instance.MdGravMgn
	@property
	def md_stal_mgn(self) -> float:
		return self._instance.MdStalMgn
	@property
	def md_brk_mgn(self) -> float:
		return self._instance.MdBrkMgn
	@property
	def md_nold_mgn(self) -> float:
		return self._instance.MdNoldMgn
	@property
	def pth_grv_mgn(self) -> float:
		return self._instance.PthGrvMgn
	@property
	def pth_stl_mgn(self) -> float:
		return self._instance.PthStlMgn
	@property
	def pth_brk_mgn(self) -> float:
		return self._instance.PthBrkMgn
	@property
	def pth_nld_mgn(self) -> float:
		return self._instance.PthNldMgn
	@property
	def dyn_frc_mgn(self) -> float:
		return self._instance.DynFrcMgn
	@property
	def mr_nold_trq(self) -> float:
		return self._instance.MrNoldTrq
	@property
	def r_acc_mgn(self) -> float:
		return self._instance.RAccMgn
	@property
	def r_dec_mgn(self) -> float:
		return self._instance.RDecMgn
	@property
	def r_long_mgn(self) -> float:
		return self._instance.RLongMgn
	@property
	def j_acc(self) -> float:
		return self._instance.JAcc
	@property
	def j_dec(self) -> float:
		return self._instance.JDec
	@property
	def dt_mgn(self) -> float:
		return self._instance.DtMgn
	@property
	def sp1(self) -> float:
		return self._instance.Sp1
	@property
	def sp2(self) -> float:
		return self._instance.Sp2
	@property
	def sp3(self) -> float:
		return self._instance.Sp3
	@property
	def sp4(self) -> float:
		return self._instance.Sp4
	@property
	def sp5(self) -> float:
		return self._instance.Sp5
	@property
	def sp6(self) -> float:
		return self._instance.Sp6
	@property
	def sp7(self) -> float:
		return self._instance.Sp7
	@property
	def sp8(self) -> float:
		return self._instance.Sp8
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
