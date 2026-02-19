import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import EncStatVariableType as enc_stat_variable_type

class EncStatVariableType(GenericVariableType):
	'''Describes the Fanuc type ENC_STAT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enc_stat_variable_type()
		else:
			self._instance = _internal

	@property
	def enc_count(self) -> int:
		'''Value of variable $ENC_COUNT'''
		return self._instance.EncCount

	@property
	def enc_ros_tik(self) -> int:
		'''Value of variable $ENC_ROS_TIK'''
		return self._instance.EncRosTik

	@property
	def enc_rate(self) -> int:
		'''Value of variable $ENC_RATE'''
		return self._instance.EncRate

	@property
	def enc_average(self) -> int:
		'''Value of variable $ENC_AVERAGE'''
		return self._instance.EncAverage

	@property
	def enc_enable(self) -> bool:
		'''Value of variable $ENC_ENABLE'''
		return self._instance.EncEnable

	@property
	def enc_dspstat(self) -> int:
		'''Value of variable $ENC_DSPSTAT'''
		return self._instance.EncDspstat

	@property
	def enc_spcstat(self) -> int:
		'''Value of variable $ENC_SPCSTAT'''
		return self._instance.EncSpcstat

	@property
	def enc_sim_on(self) -> bool:
		'''Value of variable $ENC_SIM_ON'''
		return self._instance.EncSimOn

	@property
	def enc_sim_spd(self) -> int:
		'''Value of variable $ENC_SIM_SPD'''
		return self._instance.EncSimSpd

	@property
	def enc_value(self) -> int:
		'''Value of variable $ENC_VALUE'''
		return self._instance.EncValue

	@property
	def enc_head(self) -> int:
		'''Value of variable $ENC_HEAD'''
		return self._instance.EncHead

	@property
	def enc_multipl(self) -> int:
		'''Value of variable $ENC_MULTIPL'''
		return self._instance.EncMultipl

	@property
	def enc_thresh(self) -> int:
		'''Value of variable $ENC_THRESH'''
		return self._instance.EncThresh

	@property
	def enc_exists(self) -> bool:
		'''Value of variable $ENC_EXISTS'''
		return self._instance.EncExists

	@property
	def enc_hsdi(self) -> bool:
		'''Value of variable $ENC_HSDI'''
		return self._instance.EncHsdi

	@property
	def enc_abscnt(self) -> int:
		'''Value of variable $ENC_ABSCNT'''
		return self._instance.EncAbscnt

	@property
	def inctravdist(self) -> int:
		'''Value of variable $INCTRAVDIST'''
		return self._instance.Inctravdist

	@property
	def inctravcnts(self) -> int:
		'''Value of variable $INCTRAVCNTS'''
		return self._instance.Inctravcnts

	@property
	def inctrav_do(self) -> int:
		'''Value of variable $INCTRAV_DO'''
		return self._instance.InctravDo

	@property
	def convspd_go(self) -> int:
		'''Value of variable $CONVSPD_GO'''
		return self._instance.ConvspdGo

	@property
	def inctravres(self) -> bool:
		'''Value of variable $INCTRAVRES'''
		return self._instance.Inctravres

	@property
	def enc_buffer(self) -> typing.List[int]:
		'''Value of variable $ENC_BUFFER'''
		return self._instance.EncBuffer

	@property
	def enc_atr_axs(self) -> int:
		'''Value of variable $ENC_ATR_AXS'''
		return self._instance.EncAtrAxs

	@property
	def sc_grp_num(self) -> int:
		'''Value of variable $SC_GRP_NUM'''
		return self._instance.ScGrpNum

	@property
	def enc_comerct(self) -> int:
		'''Value of variable $ENC_COMERCT'''
		return self._instance.EncComerct

	@property
	def enc_fbcmpct(self) -> int:
		'''Value of variable $ENC_FBCMPCT'''
		return self._instance.EncFbcmpct

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EncStatVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
