import typing
from underautomation.fanuc.ftp.variables.amp_id_variable_type import AmpIdVariableType
from underautomation.fanuc.ftp.variables.fltr_ovrn_variable_type import FltrOvrnVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MorVariableType as mor_variable_type

class MorVariableType(GenericVariableType):
	'''Describes the Fanuc type MOR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mor_variable_type()
		else:
			self._instance = _internal

	@property
	def brk_status(self) -> int:
		'''Value of variable $BRK_STATUS'''
		return self._instance.BrkStatus

	@property
	def pg_mctl(self) -> int:
		'''Value of variable $PG_MCTL'''
		return self._instance.PgMctl

	@property
	def smh_done(self) -> bool:
		'''Value of variable $SMH_DONE'''
		return self._instance.SmhDone

	@property
	def reg_dis_amp(self) -> typing.List[float]:
		'''Value of variable $REG_DIS_AMP'''
		return self._instance.RegDisAmp

	@property
	def safety_stat(self) -> int:
		'''Value of variable $SAFETY_STAT'''
		return self._instance.SafetyStat

	@property
	def class1_stop(self) -> int:
		'''Value of variable $CLASS1_STOP'''
		return self._instance.Class1Stop

	@property
	def t1_spd_ovrd(self) -> int:
		'''Value of variable $T1_SPD_OVRD'''
		return self._instance.T1SpdOvrd

	@property
	def amp_id(self) -> typing.List[AmpIdVariableType]:
		'''Value of variable $AMP_ID'''
		return [AmpIdVariableType(x) for x in self._instance.AmpId]

	@property
	def trans_cur(self) -> typing.List[float]:
		'''Value of variable $TRANS_CUR'''
		return self._instance.TransCur

	@property
	def trans_itp(self) -> typing.List[float]:
		'''Value of variable $TRANS_ITP'''
		return self._instance.TransItp

	@property
	def cblcur_cur(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_CUR'''
		return self._instance.CblcurCur

	@property
	def cblcur_itp(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_ITP'''
		return self._instance.CblcurItp

	@property
	def cblcur_thm(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_THM'''
		return self._instance.CblcurThm

	@property
	def amp_svm(self) -> typing.List[str]:
		'''Value of variable $AMP_SVM'''
		return self._instance.AmpSvm

	@property
	def amp_svmsrl(self) -> typing.List[str]:
		'''Value of variable $AMP_SVMSRL'''
		return self._instance.AmpSvmsrl

	@property
	def amp_psm(self) -> typing.List[str]:
		'''Value of variable $AMP_PSM'''
		return self._instance.AmpPsm

	@property
	def amp_psmsrl(self) -> typing.List[str]:
		'''Value of variable $AMP_PSMSRL'''
		return self._instance.AmpPsmsrl

	@property
	def amp_maxcur(self) -> typing.List[str]:
		'''Value of variable $AMP_MAXCUR'''
		return self._instance.AmpMaxcur

	@property
	def amp_series(self) -> typing.List[str]:
		'''Value of variable $AMP_SERIES'''
		return self._instance.AmpSeries

	@property
	def amp_svmver(self) -> typing.List[str]:
		'''Value of variable $AMP_SVMVER'''
		return self._instance.AmpSvmver

	@property
	def amp_psmver(self) -> typing.List[str]:
		'''Value of variable $AMP_PSMVER'''
		return self._instance.AmpPsmver

	@property
	def fltr_ovrn(self) -> FltrOvrnVariableType:
		'''Value of variable $FLTR_OVRN'''
		return FltrOvrnVariableType(self._instance.FltrOvrn)

	@property
	def fan_rotnum(self) -> typing.List[int]:
		'''Value of variable $FAN_ROTNUM'''
		return self._instance.FanRotnum

	@property
	def dspcode_id(self) -> typing.List[int]:
		'''Value of variable $DSPCODE_ID'''
		return self._instance.DspcodeId

	@property
	def dspcode_ver(self) -> typing.List[str]:
		'''Value of variable $DSPCODE_VER'''
		return self._instance.DspcodeVer

	@property
	def cmnd_exist(self) -> int:
		'''Value of variable $CMND_EXIST'''
		return self._instance.CmndExist

	@property
	def spc_cstp_sw(self) -> int:
		'''Value of variable $SPC_CSTP_SW'''
		return self._instance.SpcCstpSw

	@property
	def end_motion(self) -> bool:
		'''Value of variable $END_MOTION'''
		return self._instance.EndMotion

	@property
	def override(self) -> int:
		'''Value of variable $OVERRIDE'''
		return self._instance.Override

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MorVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
