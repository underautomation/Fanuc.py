import typing
from underautomation.fanuc.ftp.variables.cp_test_variable_type import CpTestVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpParamgpVariableType as cp_paramgp_variable_type

class CpParamgpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_paramgp_variable_type()
		else:
			self._instance = _internal
	@property
	def warnmessenb(self) -> bool:
		return self._instance.Warnmessenb
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def enb(self) -> bool:
		return self._instance.Enb
	@property
	def num_chn(self) -> int:
		return self._instance.NumChn
	@property
	def num_jbfset(self) -> int:
		return self._instance.NumJbfset
	@property
	def num_jbf(self) -> int:
		return self._instance.NumJbf
	@property
	def ext_num_jbf(self) -> int:
		return self._instance.ExtNumJbf
	@property
	def jbf_size(self) -> int:
		return self._instance.JbfSize
	@property
	def ext_jbf_siz(self) -> int:
		return self._instance.ExtJbfSiz
	@property
	def num_tf(self) -> int:
		return self._instance.NumTf
	@property
	def tf_size(self) -> int:
		return self._instance.TfSize
	@property
	def ext_tf_size(self) -> int:
		return self._instance.ExtTfSize
	@property
	def num_rsinfo(self) -> int:
		return self._instance.NumRsinfo
	@property
	def jnt_vel_lim(self) -> typing.List[float]:
		return self._instance.JntVelLim
	@property
	def jnt_acc_lim(self) -> typing.List[float]:
		return self._instance.JntAccLim
	@property
	def jnt_jrk_lim(self) -> typing.List[float]:
		return self._instance.JntJrkLim
	@property
	def t1segfl_sf(self) -> float:
		return self._instance.T1segflSf
	@property
	def t1gtfl_sf(self) -> float:
		return self._instance.T1gtflSf
	@property
	def crcmp_switc(self) -> int:
		return self._instance.CrcmpSwitc
	@property
	def acclim_sf(self) -> float:
		return self._instance.AcclimSf
	@property
	def jrklim_sf(self) -> float:
		return self._instance.JrklimSf
	@property
	def pspd_switch(self) -> int:
		return self._instance.PspdSwitch
	@property
	def max_pspd(self) -> int:
		return self._instance.MaxPspd
	@property
	def min_pspd(self) -> int:
		return self._instance.MinPspd
	@property
	def pspdacc_sf(self) -> float:
		return self._instance.PspdaccSf
	@property
	def pspdjrk_sf(self) -> float:
		return self._instance.PspdjrkSf
	@property
	def cdcomp_sw(self) -> int:
		return self._instance.CdcompSw
	@property
	def cdacc_sf(self) -> float:
		return self._instance.CdaccSf
	@property
	def cdjrk_sf(self) -> float:
		return self._instance.CdjrkSf
	@property
	def cddeltatol(self) -> float:
		return self._instance.Cddeltatol
	@property
	def cddistsf(self) -> float:
		return self._instance.Cddistsf
	@property
	def cdangtol(self) -> float:
		return self._instance.Cdangtol
	@property
	def cddevtol(self) -> float:
		return self._instance.Cddevtol
	@property
	def chkjntlim(self) -> bool:
		return self._instance.Chkjntlim
	@property
	def fdang_tol(self) -> float:
		return self._instance.FdangTol
	@property
	def fdlin_tol(self) -> float:
		return self._instance.FdlinTol
	@property
	def jntjbf_enb(self) -> bool:
		return self._instance.JntjbfEnb
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def extra_int(self) -> typing.List[int]:
		return self._instance.ExtraInt
	@property
	def extra_flt(self) -> typing.List[float]:
		return self._instance.ExtraFlt
	@property
	def cp_test(self) -> CpTestVariableType:
		return CpTestVariableType(self._instance.CpTest)
	@property
	def t1_vscale(self) -> int:
		return self._instance.T1Vscale
	@property
	def t1_ascale(self) -> int:
		return self._instance.T1Ascale
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
