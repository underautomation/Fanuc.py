import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EncStatVariableType as enc_stat_variable_type

class EncStatVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enc_stat_variable_type()
		else:
			self._instance = _internal
	@property
	def enc_count(self) -> int:
		return self._instance.EncCount
	@property
	def enc_ros_tik(self) -> int:
		return self._instance.EncRosTik
	@property
	def enc_rate(self) -> int:
		return self._instance.EncRate
	@property
	def enc_average(self) -> int:
		return self._instance.EncAverage
	@property
	def enc_enable(self) -> bool:
		return self._instance.EncEnable
	@property
	def enc_dspstat(self) -> int:
		return self._instance.EncDspstat
	@property
	def enc_spcstat(self) -> int:
		return self._instance.EncSpcstat
	@property
	def enc_sim_on(self) -> bool:
		return self._instance.EncSimOn
	@property
	def enc_sim_spd(self) -> int:
		return self._instance.EncSimSpd
	@property
	def enc_value(self) -> int:
		return self._instance.EncValue
	@property
	def enc_head(self) -> int:
		return self._instance.EncHead
	@property
	def enc_multipl(self) -> int:
		return self._instance.EncMultipl
	@property
	def enc_thresh(self) -> int:
		return self._instance.EncThresh
	@property
	def enc_exists(self) -> bool:
		return self._instance.EncExists
	@property
	def enc_hsdi(self) -> bool:
		return self._instance.EncHsdi
	@property
	def enc_abscnt(self) -> int:
		return self._instance.EncAbscnt
	@property
	def inctravdist(self) -> int:
		return self._instance.Inctravdist
	@property
	def inctravcnts(self) -> int:
		return self._instance.Inctravcnts
	@property
	def inctrav_do(self) -> int:
		return self._instance.InctravDo
	@property
	def convspd_go(self) -> int:
		return self._instance.ConvspdGo
	@property
	def inctravres(self) -> bool:
		return self._instance.Inctravres
	@property
	def enc_buffer(self) -> typing.List[int]:
		return self._instance.EncBuffer
	@property
	def enc_atr_axs(self) -> int:
		return self._instance.EncAtrAxs
	@property
	def sc_grp_num(self) -> int:
		return self._instance.ScGrpNum
	@property
	def enc_comerct(self) -> int:
		return self._instance.EncComerct
	@property
	def enc_fbcmpct(self) -> int:
		return self._instance.EncFbcmpct
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
