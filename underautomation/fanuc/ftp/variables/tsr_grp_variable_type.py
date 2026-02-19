import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TsrGrpVariableType as tsr_grp_variable_type

class TsrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TSR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tsr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def mr_max_trq(self) -> typing.List[float]:
		'''Value of variable $MR_MAX_TRQ'''
		return self._instance.MrMaxTrq

	@property
	def mr_stal_trq(self) -> typing.List[float]:
		'''Value of variable $MR_STAL_TRQ'''
		return self._instance.MrStalTrq

	@property
	def mr_brk_trq(self) -> typing.List[float]:
		'''Value of variable $MR_BRK_TRQ'''
		return self._instance.MrBrkTrq

	@property
	def mr_brk_vel(self) -> typing.List[float]:
		'''Value of variable $MR_BRK_VEL'''
		return self._instance.MrBrkVel

	@property
	def mr_nold_vel(self) -> typing.List[float]:
		'''Value of variable $MR_NOLD_VEL'''
		return self._instance.MrNoldVel

	@property
	def ma_load_trq(self) -> typing.List[float]:
		'''Value of variable $MA_LOAD_TRQ'''
		return self._instance.MaLoadTrq

	@property
	def md_load_trq(self) -> typing.List[float]:
		'''Value of variable $MD_LOAD_TRQ'''
		return self._instance.MdLoadTrq

	@property
	def ma_grav_mgn(self) -> typing.List[float]:
		'''Value of variable $MA_GRAV_MGN'''
		return self._instance.MaGravMgn

	@property
	def ma_stal_mgn(self) -> typing.List[float]:
		'''Value of variable $MA_STAL_MGN'''
		return self._instance.MaStalMgn

	@property
	def ma_brk_mgn(self) -> typing.List[float]:
		'''Value of variable $MA_BRK_MGN'''
		return self._instance.MaBrkMgn

	@property
	def md_grav_mgn(self) -> typing.List[float]:
		'''Value of variable $MD_GRAV_MGN'''
		return self._instance.MdGravMgn

	@property
	def md_stal_mgn(self) -> typing.List[float]:
		'''Value of variable $MD_STAL_MGN'''
		return self._instance.MdStalMgn

	@property
	def md_brk_mgn(self) -> typing.List[float]:
		'''Value of variable $MD_BRK_MGN'''
		return self._instance.MdBrkMgn

	@property
	def mj_acc_mgn(self) -> typing.List[float]:
		'''Value of variable $MJ_ACC_MGN'''
		return self._instance.MjAccMgn

	@property
	def mc_acc_mgn(self) -> typing.List[float]:
		'''Value of variable $MC_ACC_MGN'''
		return self._instance.McAccMgn

	@property
	def mc_stal_mgn(self) -> typing.List[float]:
		'''Value of variable $MC_STAL_MGN'''
		return self._instance.McStalMgn

	@property
	def mc_brk_mgn(self) -> typing.List[float]:
		'''Value of variable $MC_BRK_MGN'''
		return self._instance.McBrkMgn

	@property
	def min_cyc_id(self) -> str:
		'''Value of variable $MIN_CYC_ID'''
		return self._instance.MinCycId

	@property
	def min_c_id_e1(self) -> str:
		'''Value of variable $MIN_C_ID_E1'''
		return self._instance.MinCIdE1

	@property
	def min_c_id_e2(self) -> str:
		'''Value of variable $MIN_C_ID_E2'''
		return self._instance.MinCIdE2

	@property
	def min_c_id_e3(self) -> str:
		'''Value of variable $MIN_C_ID_E3'''
		return self._instance.MinCIdE3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TsrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
