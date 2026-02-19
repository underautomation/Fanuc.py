import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlidSvVariableType as plid_sv_variable_type

class PlidSvVariableType(GenericVariableType):
	'''Describes the Fanuc type PLID_SV_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_sv_variable_type()
		else:
			self._instance = _internal

	@property
	def cur_scrn(self) -> int:
		'''Value of variable $CUR_SCRN'''
		return self._instance.CurScrn

	@property
	def cur_group(self) -> int:
		'''Value of variable $CUR_GROUP'''
		return self._instance.CurGroup

	@property
	def save_done(self) -> bool:
		'''Value of variable $SAVE_DONE'''
		return self._instance.SaveDone

	@property
	def no_recover(self) -> bool:
		'''Value of variable $NO_RECOVER'''
		return self._instance.NoRecover

	@property
	def result_sav(self) -> typing.List[float]:
		'''Value of variable $RESULT_SAV'''
		return self._instance.ResultSav

	@property
	def payload(self) -> float:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def payload_x(self) -> float:
		'''Value of variable $PAYLOAD_X'''
		return self._instance.PayloadX

	@property
	def payload_y(self) -> float:
		'''Value of variable $PAYLOAD_Y'''
		return self._instance.PayloadY

	@property
	def payload_z(self) -> float:
		'''Value of variable $PAYLOAD_Z'''
		return self._instance.PayloadZ

	@property
	def payload_ix(self) -> float:
		'''Value of variable $PAYLOAD_IX'''
		return self._instance.PayloadIx

	@property
	def payload_iy(self) -> float:
		'''Value of variable $PAYLOAD_IY'''
		return self._instance.PayloadIy

	@property
	def payload_iz(self) -> float:
		'''Value of variable $PAYLOAD_IZ'''
		return self._instance.PayloadIz

	@property
	def armload1(self) -> float:
		'''Value of variable $ARMLOAD1'''
		return self._instance.Armload1

	@property
	def armload2(self) -> float:
		'''Value of variable $ARMLOAD2'''
		return self._instance.Armload2

	@property
	def do_default(self) -> bool:
		'''Value of variable $DO_DEFAULT'''
		return self._instance.DoDefault

	@property
	def mov_pos1(self) -> typing.List[float]:
		'''Value of variable $MOV_POS1'''
		return self._instance.MovPos1

	@property
	def mov_pos2(self) -> typing.List[float]:
		'''Value of variable $MOV_POS2'''
		return self._instance.MovPos2

	@property
	def speed_high(self) -> int:
		'''Value of variable $SPEED_HIGH'''
		return self._instance.SpeedHigh

	@property
	def speed_low(self) -> int:
		'''Value of variable $SPEED_LOW'''
		return self._instance.SpeedLow

	@property
	def accel_high(self) -> int:
		'''Value of variable $ACCEL_HIGH'''
		return self._instance.AccelHigh

	@property
	def accel_low(self) -> int:
		'''Value of variable $ACCEL_LOW'''
		return self._instance.AccelLow

	@property
	def do_def_pos(self) -> bool:
		'''Value of variable $DO_DEF_POS'''
		return self._instance.DoDefPos

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlidSvVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
