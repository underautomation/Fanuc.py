import typing
from underautomation.fanuc.ftp.variables.cp_test_variable_type import CpTestVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpParamgpVariableType as cp_paramgp_variable_type

class CpParamgpVariableType(GenericVariableType):
	'''Describes the Fanuc type CP_PARAMGP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_paramgp_variable_type()
		else:
			self._instance = _internal

	@property
	def warnmessenb(self) -> bool:
		'''Value of variable $WARNMESSENB'''
		return self._instance.Warnmessenb

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def enb(self) -> bool:
		'''Value of variable $ENB'''
		return self._instance.Enb

	@property
	def num_chn(self) -> int:
		'''Value of variable $NUM_CHN'''
		return self._instance.NumChn

	@property
	def num_jbfset(self) -> int:
		'''Value of variable $NUM_JBFSET'''
		return self._instance.NumJbfset

	@property
	def num_jbf(self) -> int:
		'''Value of variable $NUM_JBF'''
		return self._instance.NumJbf

	@property
	def ext_num_jbf(self) -> int:
		'''Value of variable $EXT_NUM_JBF'''
		return self._instance.ExtNumJbf

	@property
	def jbf_size(self) -> int:
		'''Value of variable $JBF_SIZE'''
		return self._instance.JbfSize

	@property
	def ext_jbf_siz(self) -> int:
		'''Value of variable $EXT_JBF_SIZ'''
		return self._instance.ExtJbfSiz

	@property
	def num_tf(self) -> int:
		'''Value of variable $NUM_TF'''
		return self._instance.NumTf

	@property
	def tf_size(self) -> int:
		'''Value of variable $TF_SIZE'''
		return self._instance.TfSize

	@property
	def ext_tf_size(self) -> int:
		'''Value of variable $EXT_TF_SIZE'''
		return self._instance.ExtTfSize

	@property
	def num_rsinfo(self) -> int:
		'''Value of variable $NUM_RSINFO'''
		return self._instance.NumRsinfo

	@property
	def jnt_vel_lim(self) -> typing.List[float]:
		'''Value of variable $JNT_VEL_LIM'''
		return self._instance.JntVelLim

	@property
	def jnt_acc_lim(self) -> typing.List[float]:
		'''Value of variable $JNT_ACC_LIM'''
		return self._instance.JntAccLim

	@property
	def jnt_jrk_lim(self) -> typing.List[float]:
		'''Value of variable $JNT_JRK_LIM'''
		return self._instance.JntJrkLim

	@property
	def t1segfl_sf(self) -> float:
		'''Value of variable $T1SEGFL_SF'''
		return self._instance.T1segflSf

	@property
	def t1gtfl_sf(self) -> float:
		'''Value of variable $T1GTFL_SF'''
		return self._instance.T1gtflSf

	@property
	def crcmp_switc(self) -> int:
		'''Value of variable $CRCMP_SWITC'''
		return self._instance.CrcmpSwitc

	@property
	def acclim_sf(self) -> float:
		'''Value of variable $ACCLIM_SF'''
		return self._instance.AcclimSf

	@property
	def jrklim_sf(self) -> float:
		'''Value of variable $JRKLIM_SF'''
		return self._instance.JrklimSf

	@property
	def pspd_switch(self) -> int:
		'''Value of variable $PSPD_SWITCH'''
		return self._instance.PspdSwitch

	@property
	def max_pspd(self) -> int:
		'''Value of variable $MAX_PSPD'''
		return self._instance.MaxPspd

	@property
	def min_pspd(self) -> int:
		'''Value of variable $MIN_PSPD'''
		return self._instance.MinPspd

	@property
	def pspdacc_sf(self) -> float:
		'''Value of variable $PSPDACC_SF'''
		return self._instance.PspdaccSf

	@property
	def pspdjrk_sf(self) -> float:
		'''Value of variable $PSPDJRK_SF'''
		return self._instance.PspdjrkSf

	@property
	def cdcomp_sw(self) -> int:
		'''Value of variable $CDCOMP_SW'''
		return self._instance.CdcompSw

	@property
	def cdacc_sf(self) -> float:
		'''Value of variable $CDACC_SF'''
		return self._instance.CdaccSf

	@property
	def cdjrk_sf(self) -> float:
		'''Value of variable $CDJRK_SF'''
		return self._instance.CdjrkSf

	@property
	def cddeltatol(self) -> float:
		'''Value of variable $CDDELTATOL'''
		return self._instance.Cddeltatol

	@property
	def cddistsf(self) -> float:
		'''Value of variable $CDDISTSF'''
		return self._instance.Cddistsf

	@property
	def cdangtol(self) -> float:
		'''Value of variable $CDANGTOL'''
		return self._instance.Cdangtol

	@property
	def cddevtol(self) -> float:
		'''Value of variable $CDDEVTOL'''
		return self._instance.Cddevtol

	@property
	def chkjntlim(self) -> bool:
		'''Value of variable $CHKJNTLIM'''
		return self._instance.Chkjntlim

	@property
	def fdang_tol(self) -> float:
		'''Value of variable $FDANG_TOL'''
		return self._instance.FdangTol

	@property
	def fdlin_tol(self) -> float:
		'''Value of variable $FDLIN_TOL'''
		return self._instance.FdlinTol

	@property
	def jntjbf_enb(self) -> bool:
		'''Value of variable $JNTJBF_ENB'''
		return self._instance.JntjbfEnb

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def extra_int(self) -> typing.List[int]:
		'''Value of variable $EXTRA_INT'''
		return self._instance.ExtraInt

	@property
	def extra_flt(self) -> typing.List[float]:
		'''Value of variable $EXTRA_FLT'''
		return self._instance.ExtraFlt

	@property
	def cp_test(self) -> CpTestVariableType:
		'''Value of variable $CP_TEST'''
		return CpTestVariableType(self._instance.CpTest)

	@property
	def t1_vscale(self) -> int:
		'''Value of variable $T1_VSCALE'''
		return self._instance.T1Vscale

	@property
	def t1_ascale(self) -> int:
		'''Value of variable $T1_ASCALE'''
		return self._instance.T1Ascale

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpParamgpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
