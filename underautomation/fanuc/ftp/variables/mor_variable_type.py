import typing
from underautomation.fanuc.ftp.variables.amp_id_variable_type import AmpIdVariableType
from underautomation.fanuc.ftp.variables.fltr_ovrn_variable_type import FltrOvrnVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MorVariableType as mor_variable_type

class MorVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mor_variable_type()
		else:
			self._instance = _internal
	@property
	def brk_status(self) -> int:
		return self._instance.BrkStatus
	@property
	def pg_mctl(self) -> int:
		return self._instance.PgMctl
	@property
	def smh_done(self) -> bool:
		return self._instance.SmhDone
	@property
	def reg_dis_amp(self) -> typing.List[float]:
		return self._instance.RegDisAmp
	@property
	def safety_stat(self) -> int:
		return self._instance.SafetyStat
	@property
	def class1_stop(self) -> int:
		return self._instance.Class1Stop
	@property
	def t1_spd_ovrd(self) -> int:
		return self._instance.T1SpdOvrd
	@property
	def amp_id(self) -> typing.List[AmpIdVariableType]:
		return [AmpIdVariableType(x) for x in self._instance.AmpId]
	@property
	def trans_cur(self) -> typing.List[float]:
		return self._instance.TransCur
	@property
	def trans_itp(self) -> typing.List[float]:
		return self._instance.TransItp
	@property
	def cblcur_cur(self) -> typing.List[float]:
		return self._instance.CblcurCur
	@property
	def cblcur_itp(self) -> typing.List[float]:
		return self._instance.CblcurItp
	@property
	def cblcur_thm(self) -> typing.List[float]:
		return self._instance.CblcurThm
	@property
	def amp_svm(self) -> typing.List[str]:
		return self._instance.AmpSvm
	@property
	def amp_svmsrl(self) -> typing.List[str]:
		return self._instance.AmpSvmsrl
	@property
	def amp_psm(self) -> typing.List[str]:
		return self._instance.AmpPsm
	@property
	def amp_psmsrl(self) -> typing.List[str]:
		return self._instance.AmpPsmsrl
	@property
	def amp_maxcur(self) -> typing.List[str]:
		return self._instance.AmpMaxcur
	@property
	def amp_series(self) -> typing.List[str]:
		return self._instance.AmpSeries
	@property
	def amp_svmver(self) -> typing.List[str]:
		return self._instance.AmpSvmver
	@property
	def amp_psmver(self) -> typing.List[str]:
		return self._instance.AmpPsmver
	@property
	def fltr_ovrn(self) -> FltrOvrnVariableType:
		return FltrOvrnVariableType(self._instance.FltrOvrn)
	@property
	def fan_rotnum(self) -> typing.List[int]:
		return self._instance.FanRotnum
	@property
	def dspcode_id(self) -> typing.List[int]:
		return self._instance.DspcodeId
	@property
	def dspcode_ver(self) -> typing.List[str]:
		return self._instance.DspcodeVer
	@property
	def cmnd_exist(self) -> int:
		return self._instance.CmndExist
	@property
	def spc_cstp_sw(self) -> int:
		return self._instance.SpcCstpSw
	@property
	def end_motion(self) -> bool:
		return self._instance.EndMotion
	@property
	def override(self) -> int:
		return self._instance.Override
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
